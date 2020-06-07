---
layout: post
title: Old habits die hard
date: '2017-08-07 17:07:00'
---

I just (re-)committed the cardinal sin of checking some app secrets into a Github repository! I had started a new project and did the usual hacky thing of hard-coding my Oauth client creds into the source code. Then I went ahead and checked it all in... **Whoops!**  

Admittedly the repo was private, and the secrets were only Oauth client secrets - easily regenerated. But still. My solution was to remove the secrets from the code, push to a brand new repo, and delete the old repo. Just checking in new clean versions of files obviously doesn't work since the secrets are still in the git history.

I probably need to create a new habit of where I store and access secrets. Maybe I'll try using [Vault](https://www.vaultproject.io/) locally and see how that works out.