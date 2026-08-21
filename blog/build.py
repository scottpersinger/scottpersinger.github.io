#!/usr/bin/env python3
"""Build the blog: render Markdown posts to HTML, then regenerate
blog/index.html's post list and blog/feed.xml.

Usage:  python3 blog/build.py      (run from anywhere)

Posts live in blog/posts/ and can be either:

  * NAME.md   — Markdown with a front-matter block (see _template.md). Rendered
                into NAME.html using _template.html. Don't edit the .html.
  * NAME.html — hand-written HTML (copy _template.html). Used as-is.

Files starting with "_" are ignored. The index/feed read each post's <h1> and
the <meta> tags description / date (YYYY-MM-DD) / tags (comma-separated).

The only dependency is the `markdown` package; on first run this script creates
blog/.venv, installs it there, and re-executes itself — nothing global changes.
"""
import html, os, re, subprocess, sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

BLOG = Path(__file__).resolve().parent

def _ensure_markdown():
    try:
        import markdown  # noqa: F401
        return
    except ImportError:
        pass
    venv = BLOG / ".venv"
    py = venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    in_venv = Path(sys.prefix).resolve() == venv.resolve() or os.environ.get("BLOG_BUILD_REEXEC")
    if in_venv:
        sys.exit("`markdown` is missing inside blog/.venv — run:  rm -rf blog/.venv && python3 blog/build.py")
    if not py.exists():
        print("first run: creating blog/.venv and installing `markdown`…")
        subprocess.check_call([sys.executable, "-m", "venv", str(venv)])
        subprocess.check_call([str(py), "-m", "pip", "install", "--quiet", "--disable-pip-version-check", "markdown"])
    os.environ["BLOG_BUILD_REEXEC"] = "1"
    sys.stdout.flush()
    os.execv(str(py), [str(py)] + sys.argv)

_ensure_markdown()
import markdown

SITE = "https://scottpersinger.com"
POSTS = BLOG / "posts"
TEMPLATE = POSTS / "_template.html"

def meta(src, name):
    m = re.search(r'<meta\s+name="%s"\s+content="([^"]*)"' % re.escape(name), src)
    return html.unescape(m.group(1)).strip() if m else ""

def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()

def read_post(path):
    src = path.read_text(encoding="utf-8")
    h1 = re.search(r"<h1>(.*?)</h1>", src, re.S)
    date = meta(src, "date")
    if not h1 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        sys.exit(f"{path.name}: needs an <h1> and <meta name=\"date\" content=\"YYYY-MM-DD\">")
    prose = re.search(r'<div class="prose">(.*?)</div>\s*<div class="foot">', src, re.S)
    words = len(strip_tags(prose.group(1)).split()) if prose else 0
    return {
        "file": path.name,
        "title": strip_tags(h1.group(1)),
        "desc": meta(src, "description"),
        "date": datetime.strptime(date, "%Y-%m-%d"),
        "tags": [t.strip() for t in meta(src, "tags").split(",") if t.strip()],
        "mins": max(1, round(words / 220)),
    }

FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)

def parse_front(src, path):
    m = FRONT.match(src)
    if not m:
        sys.exit(f"{path.name}: missing front matter (--- ... --- block at top)")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("title", "date", "description"):
        if not meta.get(k):
            sys.exit(f"{path.name}: front matter needs `{k}:`")
    return meta, src[m.end():]

def render_md(path):
    """Render posts/NAME.md -> posts/NAME.html using _template.html."""
    meta, body_md = parse_front(path.read_text(encoding="utf-8"), path)
    body = markdown.markdown(body_md, extensions=["extra", "sane_lists", "smarty"], output_format="html5")
    body = re.sub(r"\n{3,}", "\n\n", body)
    tpl = TEMPLATE.read_text(encoding="utf-8")
    esc = lambda s: html.escape(s, quote=True)
    tpl = tpl.replace("<title>POST TITLE — Scott Persinger</title>", f"<title>{esc(meta['title'])} — Scott Persinger</title>")
    tpl = tpl.replace('content="One-sentence summary shown in the index and in link previews."', f'content="{esc(meta["description"])}"')
    tpl = tpl.replace('<meta name="date" content="2026-01-01" />', f'<meta name="date" content="{esc(meta["date"])}" />')
    tpl = tpl.replace('<meta name="tags" content="ai-agents, startups" />', f'<meta name="tags" content="{esc(meta.get("tags", ""))}" />')
    tpl = tpl.replace('<meta property="og:title" content="POST TITLE" />', f'<meta property="og:title" content="{esc(meta["title"])}" />')
    tpl = tpl.replace("<h1>Post title</h1>", f"<h1>{esc(meta['title'])}</h1>")
    deck = meta.get("deck", "")
    tpl = tpl.replace('<p class="deck">A one-or-two sentence deck that sets up the piece.</p>',
                      f'<p class="deck">{deck}</p>' if deck else "")
    tpl = re.sub(r'<div class="prose">.*?</div>\n\n    <div class="foot">',
                 lambda _: '<div class="prose">\n' + body + '\n    </div>\n\n    <div class="foot">', tpl, count=1, flags=re.S)
    tpl = tpl.replace("<!-- ===== EDIT THESE ===== -->", f"<!-- GENERATED from posts/{path.name} by build.py — edit the .md, not this file -->")
    tpl = tpl.replace("<!-- ====================== -->\n", "")
    out = path.with_suffix(".html")
    out.write_text(tpl, encoding="utf-8")
    return out

def replace_between(text, start, end, body):
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pat.search(text):
        sys.exit(f"marker {start} … {end} not found")
    return pat.sub(lambda _: start + body + end, text)

def main():
    for md in sorted(POSTS.glob("*.md")):
        if not md.name.startswith("_"):
            render_md(md)
    posts = sorted((read_post(p) for p in POSTS.glob("*.html") if not p.name.startswith("_")),
                   key=lambda p: p["date"], reverse=True)

    # ---- index.html ----
    if posts:
        items = []
        for p in posts:
            tags = "".join(f'<span class="tag">{html.escape(t)}</span>' for t in p["tags"])
            items.append(f'''
    <a class="post" href="posts/{p["file"]}">
      <div class="when"><b>{p["date"].strftime("%b %d, %Y")}</b>{p["mins"]} min read</div>
      <div>
        <h2>{html.escape(p["title"])}</h2>
        <p>{html.escape(p["desc"])}</p>
        <div class="tags">{tags}</div>
      </div>
      <span class="arr">Read ↗</span>
    </a>''')
        body = "".join(items) + "\n"
    else:
        body = '\n    <p class="empty">Nothing here yet — check back soon.</p>\n'
    idx = BLOG / "index.html"
    text = idx.read_text(encoding="utf-8")
    text = replace_between(text, "<!-- POSTS:START -->", "<!-- POSTS:END -->", body)
    text = replace_between(text, "<!-- COUNT:START -->", "<!-- COUNT:END -->", str(len(posts)))
    idx.write_text(text, encoding="utf-8")

    # ---- feed.xml ----
    now = format_datetime(datetime.now(timezone.utc))
    entries = []
    for p in posts:
        url = f"{SITE}/blog/posts/{p['file']}"
        pub = format_datetime(p["date"].replace(hour=12, tzinfo=timezone.utc))
        cats = "".join(f"<category>{html.escape(t)}</category>" for t in p["tags"])
        entries.append(f"""  <item>
    <title>{html.escape(p['title'])}</title>
    <link>{url}</link>
    <guid isPermaLink="true">{url}</guid>
    <pubDate>{pub}</pubDate>
    <description>{html.escape(p['desc'])}</description>
    {cats}
  </item>""")
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>Scott Persinger — Blog</title>
  <link>{SITE}/blog/</link>
  <atom:link href="{SITE}/blog/feed.xml" rel="self" type="application/rss+xml" />
  <description>Writing on AI agents, travel tech, platforms, and building startups.</description>
  <language>en-us</language>
  <lastBuildDate>{now}</lastBuildDate>
{chr(10).join(entries)}
</channel>
</rss>
"""
    (BLOG / "feed.xml").write_text(feed, encoding="utf-8")

    print(f"built index.html + feed.xml with {len(posts)} post(s):")
    for p in posts:
        print(f"  {p['date']:%Y-%m-%d}  {p['title']}  ({p['mins']} min)")

if __name__ == "__main__":
    main()
