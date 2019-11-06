---
layout: post
title: AWS is a 1000 piece lego kit
date: '2017-08-25 00:07:56'
image: '/images/posts/millennium.jpg'
---

I've been spending time lately trying to get a deeper understanding of the current world of AWS. That platform grows and changes so quickly that it takes real effort just to keep up!

The breadth of AWS is pretty incredible:

* Elastic compute
* Networking services
* File storage
* Data storage and data services
* Messaging and event stream services
* Developer tools and services
* Security tools
* Metrics and monitoring
* Business applications

Just wrapping your head around all these services is a challenge. Then trying to build a mental model of how these services fit together and how you might leverage them for your work is a whole project unto itself - if not a whole career. 

AWS these days reminds me of a modern-day, 1000 piece Lego set. Back when I was a kid there were like 10 different lego pieces. That was it! You built everything from this small set of interchangeable blocks.

But somewhere along the way Lego mastered bespoke lego-piece engineering and brand licensing. 

![millennium](https://s3-us-west-1.amazonaws.com/assets-scottp-org/2017/08/millennium.jpg)

The result are lego sets comprising hundreds of specialized pieces. Once one of my kids received a 976 piece lego set from his grandmother. He was so excited that while I was out of the room he set about opening **every single** bag of pieces in the box and dumping them all out of the floor! Woe betide the parent who has to assemble a thousand random lego pieces into a recognizable structure!

And this is what AWS reminds me of today. Not because many of the services don't have important, unique features. For sure they do. The problem is, how do I know which ones to use for my particular problem? 

Should I use Mysql, Mariadb, or Aurora? 

I need to dispatch some background jobs. Should I use SQS or Kinesis? In the past I've used Redis for lightweight queuing so maybe I should just use Elasticache?

Hmm... I just want to deploy a new app. Should I use Lightsail and just do it by hand? Or maybe Elastic Beanstalk - it's designed for that (although it seems to have fallen into disrepair). Or should I go with the new hotness and wire up Code Build and Code Deploy with Code Pipeline and target the EC2 Container Service? Nah, containers is already old school, maybe I should go all in with serverless and use Lambda instead...

And assuming that I can pick the technologies I want to use, now I've got to wrestle with IAM and my VPC settings to get it all working together. 

I have no doubt that Amazon knows that approachability and usability are significant barriers on AWS. They've done a lot to improve dashboards, and added smart wizards and getting started guides. But they still seem to struggle with a key idea: introducing **abstractions**. They need to introduce higher level concepts that hide details underneath them so they can give me a simpler mental model to work with. As it stands I can click the buttons in Code Pipeline to make all the hamsters run, but as soon as I run into a problem I'm back reading the minute rules around IAM policy files.

In fact it almost seems like there are **no abstractions** on AWS. (This isn't quite true - Lambda is a significant one.) But so many of the services include and expose every option, every knob, and every security setting.

Car manufacturers don't build cars like those 5000 piece lego sets. They don't custom design every piece of your car. Much of their manufacturing and design is geared towards designing components they can re-use in multiple vehicle designs. But building on AWS still feels like building that Millennium Falcon...
