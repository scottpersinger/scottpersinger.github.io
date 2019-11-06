---
layout: post
title: Fun with RabbitMQ
date: '2012-10-26 22:14:00'
---

I’ve been using a Rabbit MQ in anger these days at my latest startup. It’s anchoring a large async, distributed system we’re building. I’ve taken to saying about Rabbit: “When it’s working, I love it. When it’s not, there’s nothing I hate more”.

The first big issue we ran into was using rabbit over SSL. The issue wasn’t with rabbit the server, but rather finding a python client that worked with both Celery (which is awesome) and Rabbit over SSL. With some judicious hacking on Kombu we got it working.

As an aside, one issue that vexed us for a number of hours was the failure to connect to rabbit over ssl when running on Heroku, even though everything ran fine locally. Turns out the issue came from the fact that opening the first socket connection from your Heroku app can take up to 10 seconds, and thus our rabbit connection was timing out. Upping the timeout got around this problem.

My current bedevilment comes from an issue that I see fairly frequently during development. The issue is that if you’re rabbit client doesn’t cleanly close its connection (like it may if you hit Ctrl-C to stop it), then you may end up with “phantom” rabbit connections/consumers. It seems that rabbit can take a long time (like multiple minutes) to decide that these consumers are really gone.

In the meantime, rabbit will attempt to deliver messages to clients which have disconnected. This can be really disconcerting, because the symptom is that you publish a message to the broker, and then it disappears. If you do connect a consumer to the broker, it may receive some of your messages, and eventually they will all be delivered, but it can take minutes for that to happen, which feels like an eternity when you’re sitting there waiting for your program to do something!

So first, some hints on figuring out what’s going on. First of all, you can list the current client connections to your broker:

<code>
sudo rabbitmqctl list_connections pid name vhost

<rabbit@rabbit1.2.18388.5> 10.141.128.228:36052 -> 10.70.70.119:5671 qa
<rabbit@rabbit1.2.18460.5> 10.87.109.52:39282 -> 10.70.70.119:5671 qa
</code>

If you see lots more connections that you think you actually have active, then you know you’ve got a problem. You can also see how many un'acked messages you’ve got lying around:

<code>
sudo rabbitmqctl list_queues -p dev2 name consumers messages_unacknowledged owner_pid
List queues…
queue1  0      4
</code>

So now we can clearly see we have un'acked messages sitting there. To cleanup, it is possible to force close our phantom connections like this:
<code>sudo rabbitmqctl close_connection “<rabbit@rabbit1.2.22974.4>” “die”
</code>

This will force close the connection, although it can take a while (like a few seconds) for it to actually happen. If you close all your connections like this, and then re-connect your client, then it will suddenly receive all the un'acked messages.

I don’t know offhand if this phantom connection problem is made worse by using SSL, although I believe I saw it even over non-SSL connections. But clearly the big message is, make sure you’re closing your rabbit connections properly. 
Good times.

Published on October 26, 2012


