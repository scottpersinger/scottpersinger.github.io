---
layout: post
title: Software cohesion and it’s organizational impact
date: '2015-05-23 22:18:00'
---

The typical software company builds and maintains a single, monolithic tarball of code. Certainly this is true for most startups. And if your startup becomes successful then eventually the high cohesion within that code base will make it tremendously hard to keep innovating your product. This is the point when many companies launch efforts to attempt to start breaking down the monolith into separately maintainable services (i.e. 'micro services'). 

That effort is necessary, but very painful. While it’s going on it becomes really difficult to continue to innovate in your product, because not only is the effort consuming a lot of engineering resources, but the nature of the effort (refactoring functionality out into separate services) runs counter to any efforts to improve or change the product. I have heard of at least one major vendor which launched no new features for 12 months while a large refactoring was completed.

The good news about this process is that it generally mirrors what’s happening organizationally in your engineering team. The team is transitioning from single logical entity to multiple distributed teams. 

But what if you built things the right way from the start? When I joined Heroku I learned that the Heroku platform was built from micro services almost from the start. And our engineering team reflects that low cohesion — we have lots of small, autonomous teams. There is no monolith for us to break up.

But not surprisingly, we now have a distributed systems challenge writ large. Not only do we have to worry about runtime coordination amongst a large number of independent services, but we have to coordinate the work of a large number of small teams. Mostly those teams can execute independently, but launching features that cross functional teams requires coordination. Resource allocation is also challenging. Smaller, independent teams makes it harder for developers to move across subsystems. Allocating new headcount is similarly difficult because every team feels like it needs “just one more person”. 

One solution to this problem is to inject some cohesion into the system. That is, group multiple teams into larger entities that have internal cohesion and expose a single “management API” to the rest of the org. We are also experimenting with feature teams, eng groups that own and develop an entire feature-set across systems.

One of our best approaches is to try to standardize our frameworks and tooling for building, deploying, and integrating new services. This helps make new service development much closer to traditional new module development for a monolithic application. Netflix and Amazon are leaders in this kind of effort and their long experience offers a lot of wisdom for organizations looking to build with a micro services approach.