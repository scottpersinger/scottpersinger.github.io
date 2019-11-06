---
layout: post
title: Self-hosting
date: '2015-05-21 22:08:00'
---

Truly, the perennial question, is where to host my blog? Having been through Blogger, Wordpress and Tumblr, I think I've finally realized that you've got to host it yourself. So I'm trying out Ghost which is very much au currant with the Hacker News kids these days. Naturally I'm hosting on Heroku. I recommend trying out the "Heroku Button" for one-click install of Ghost. It don't get any easier than that!

Ghost is a very cool, open source blogging app written in Node.js. I have it running using Postgres for persistence and Amazon S3 for asset storage. The basic steps to getting everything running were pretty easy:

* Create new Heroku app via Ghost Heroku Button
* Use heroku git:clone to pull down the code locally, then install a theme package into the content/themes directory. I'm using Ghostium at the time of writing.
* Do git push heroku master to deploy the code with theme.
* Setup my config vars for S3 access using heroku config:set. This restarts the app automatically.
* Visit the Ghost admin panel to configure settings.
* Upload a home page image and whatnot.
* Tear hair out for 30 minutes configuring g#da!!m public access on the S3 bucket including CORS.

The hardest part, by far, was getting the S3 bucket configured correctly. It makes sense that AWS locks down bucket access by default, but cutting-and-pasting XML config files into the AWS console is definitely not the "developer experience" one hopes to have in 2015. For your copy-and-paste pleasure here are the settings I configured:

```
Bucket policy
{ 
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "AllowPublicRead",
            "Effect": "Allow",
            "Principal": {
                "AWS": ""
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::scottp.blog/"
        }
    ]
}
```

CORS
 
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>https://scottpblog.herokuapp.com</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Content-</AllowedHeader>
        <AllowedHeader>Host</AllowedHeader>
    </CORSRule>
    <CORSRule>
        <AllowedOrigin>https://scottpblog.herokuapp.com</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Content-</AllowedHeader>
        <AllowedHeader>Host</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

And yes, I had to HTML escape all that config to paste it into the Ghost markdown editor. You're welcome.

**Update**

Don't forget to schedule automatic backups for your Postgres database on Heroku:

$ heroku pg:backups schedule --at '04:00 UTC' DATABASE_URL