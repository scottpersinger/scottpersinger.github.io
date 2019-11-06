---
layout: post
title: 'Platform migration: personal blog edition'
date: '2019-11-04 00:07:56'
image: 'https://jekyllrb.com/img/logo-2x.png'
---

Every few years I update my blog to a new system, both as a learning opportunity and to avoid getting stuck on something unmaintained. Last time I migrated from [Wordpress](https://wordpress.com) to [Ghost blog](https://ghost.org/), and this time I migrated to [Jekyll](https://jekyllrb.com/).

Jekyll is a static site generator. All the dynamic page generation happens in a compile step which generates static files for serving to the browser. This results in a very fast site, but doesn't play so well if you want to easily create, edit, and publish lots of posts. Fortunately I don't need anything that dynamic, and keeping my posts in source control is a great strategy for long term maintenance. 

Jekyll is roughly one cycle old on the technology curve. It's into the 'early majority' part of the [tech adoption cycle](https://en.wikipedia.org/wiki/Technology_adoption_life_cycle). I assume the innnovators for blogs are React-based systems like [Gastby](https://www.gatsbyjs.org/). But I don't really need a lot of React-style interactivity. I'm a fan of sticking with the early majority strategy to strike the right balance between innovation benefits and system maturity. This is usually my approach with phones and OS's - give me the last major release where all the bugs have been worked out!

I think this is also a good approach in general when picking a new technology stack for an app or service. Taking up the bleeding edge has a lot of risk (go talk to the people on Angular 1) that you pick something that ultimately doesn't reach a stable level of maturity. But always picking "tried and true" (the late majority stage) often leaves you on an older technology that isn't innovating anymore.

# Rise of the front-end developers

Static site generators came out of a reaction to the rising complexity of the standard CMS systems (Wordpress, Drupal, etc...). But their theory and rise dovetails with the development of React and the general explosion of front-end development as a truly specialized profession. Much of this world is working to reduce the importance of back-end development and leverage the browser as a first-class app delivery platform.

I'm intrigued to see how richer "site generator" systems like Gatsby evolve over time. Can they actually introduce richer interactivity and persistent state without dragging the full complexity of back-end engineering into the picture?



