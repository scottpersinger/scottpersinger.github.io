# scottpersinger.com

Source for [scottpersinger.com](https://scottpersinger.com) — a personal portfolio site plus
a blog. Static HTML/CSS, hosted on GitHub Pages from the `master` branch of this repo.
No framework; the only build step is a small Python script for the blog.

```
index.html          ← portfolio homepage (single self-contained page)
images/             ← logos, project screenshots, profile photo (shared by homepage + blog)
blog/
  index.html        ← post listing (generated section)
  feed.xml          ← RSS (generated)
  blog.css          ← shared blog styles, mirrors the homepage's design tokens
  build.py          ← renders Markdown posts and regenerates index + feed
  posts/
    _template.md    ← starting point for a new Markdown post
    _template.html  ← starting point for a hand-written HTML post
    YYYY-MM-DD-slug.md / .html
CNAME               ← custom domain for GitHub Pages
.nojekyll           ← tells Pages to serve files as-is
```

The homepage was generated with the
[portfolio-builder](https://github.com/scottpersinger/portfolio-builder) Claude Code skill.

## Local preview

```sh
python3 -m http.server 8765
# → http://127.0.0.1:8765/        homepage
# → http://127.0.0.1:8765/blog/   blog
```

Any static server works; there's nothing to compile for the homepage.

## Blog: publishing a post

1. Copy the template:
   `cp blog/posts/_template.md blog/posts/YYYY-MM-DD-my-slug.md`
2. Fill in the front matter and write the article in Markdown below it:
   ```markdown
   ---
   title: Post title
   description: One sentence shown in the index, RSS, and link previews.
   date: 2026-01-01
   tags: ai-agents, startups
   deck: Optional italic sub-headline under the title.
   ---
   Body in Markdown…
   ```
   Headings, lists, links, quotes, fenced code, images, and tables are all styled.
3. Build:
   `python3 blog/build.py`
   Renders each `.md` → `.html`, then regenerates `blog/index.html`'s list and `blog/feed.xml`.
   On first run it creates `blog/.venv` and installs the `markdown` package there — nothing
   global is touched (Homebrew's Python blocks `pip install` otherwise).
4. Commit and push to `master`. GitHub Pages redeploys in about a minute.

Or just tell Claude Code: *"add a blog post titled X about Y"*.

### Blog notes

- A post's `.html` is **generated** from its `.md` — edit the Markdown, then rebuild.
  The generated file starts with a `<!-- GENERATED … -->` comment as a reminder.
- Posts with no `.md` (e.g. the ones cloned from LinkedIn) are hand-written HTML and are used
  as-is; `_template.html` is the starting point for those.
- Files in `blog/posts/` starting with `_` are ignored by the build.
- Date, reading time, and tag chips on a post page are derived from its `<meta>` tags by a
  few lines of JS, so nothing is duplicated by hand.
- Images go in `/images/`; reference them from a post as `../../images/foo.png`.
- Everything inside `<div class="prose">` is styled by `blog/blog.css`.

## Deploying

GitHub Pages serves `master` at the root. Pushing is the deploy:

```sh
git add -A && git commit -m "New post: …" && git push
```

Custom domain (`scottpersinger.com`) and HTTPS are configured in the repo's Pages settings;
`CNAME` must stay in the repo root.
