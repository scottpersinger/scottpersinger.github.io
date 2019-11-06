---
layout: post
title: Playing with Spark
date: '2015-07-17 22:02:00'
---

I've been playing around with Apache Spark recently and ran into a strange issue the very first time I tried to boot up the Spark Shell:

```
java.net.UnknownHostException: spersinger-
ltm1.internal.salesforce.com: spersinger-
ltm1.internal.salesforce.com: nodename nor servname
provided, or not known 
    at java.net.InetAddress.getLocalHost(InetAddress.java:1475)
    Caused by: java.net.UnknownHostException 
```

Ah, so intuitive! Turns out the problem is described here and the answer was simple. I needed to add an entries to my hosts file mapping the loopback address to my laptop machine name. I guess this is something the JVM expects that isn't configured automatically by OS X.
