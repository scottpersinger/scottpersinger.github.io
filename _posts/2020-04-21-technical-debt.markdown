---
layout: post
title: 'Technical Debt'
date: '2020-04-21 00:07:56'
featured_image: 'assets/images/posts/debt.jpg'
featured: true
---
I have had the great fortune of starting a few companies and products from scratch. These were true mythic *green field* opportunities - not a line of code existed when we started. For most companies, however, and most developers, there is some legacy of code written some time in the 
past. And some of this code may now be weighing you down, or _slowing_ you down. This condition has inherited the useful name of *technical debt*. I want to talk about some of the different types of debt you may encounter and how I think about each of them.


# Debt is good

The first thing to remember is that *technical debt is good*! This is because technical debt is usually a sign of a successful business - one whose growth and success means that solutions to early problems are now showing their age. Some debt is good, but too much debt can be a killer. The trick is to manage your development process so that debt doesn't get out of hand. 

Now the truth is, some software businesses are so successful, and grow so fast, that they generate enormous amounts of tech debt. The demand to satisfy the market simply outstrips the capacity of the engineering team to go back and fix old code. You are very lucky if you own equity in a company like this! However, working as a *developer* in an organization like this can be very stressful and unrewarding. An increasing percentage of every developer's day is spent fighting the tech debt inside the product, even as the business may continue growing very successfully.

# Scale Debt

One typical type of debt comes from solutions that are failing to scale to meet current load demands. Scale problems are inevitable if load is growing, and the techniques for solving them are generally well known until you get to huge scale. The key tool for solving scale problems is to give your team sufficient time to create the new solution. Depending on the system it may take 2-6 months to build something that can handle 10x the load of the old system. Depending on your growth curve you may want to plan to handle 100x the load, and this might mean taking 12 months to build the new system, buying a pre-built solution or service, or hiring a specialist that has built for that scale before.

# Test debt

A very typical situation for growing startups is to find that their system has bad and missing tests. Bad tests are flaky and hard to maintain. But even worse are _missing_ tests. This manifests as the inability to make invasive code changes with confidence that you aren't breaking your system. There exist areas of your system that developers are afraid to change because they "work", today. The problem is that you probably need to add new functionality to these areas, or refactor that code to be more maintanable. 

The first solution to test debt is straightforward: write more tests. And give your engineering team the schedule slack to write those tests. 

A more subtle challenge is how, oftentimes, components of your system will not have been designed to be easily testable. A typical example is code that interacts with some external system, but mingles additional logic in with the code that talks to that system. This makes it difficult to write separate tests for the integration logic and the internal logic. It may make sense to refactor those systems or modules in order to make them more testable. Depending on your situation however, sometimes it makes more sense to just rewrite a component from scratch with an eye towards testabilty.

# Architecture debt

In my experience the most difficult type of technical debt to fix is _architecture debt_. This debt occurs when the architecture of your system (data models, interfaces between modules, assumptions about behavior) does not match your current requirements. The classic example is the "company/org" problem. Most SaaS startups begin life with a data model with one entity that represents people, and a containing entity that represents companies. This model works fine until you get big enough that some of your larger customers may have separate groups that all want to use your product. If you pack all the users in all those groups into a single Company entity then all of their usage of your product will be mixed together. But if you model each group as a separate Company, then you will likely find it hard to manage billing for the single corporation. The solution is the *Organization* model which represents another level of container above your Company entity.

I have seen and lived through multiple projects which introduced another container level in the company hierarchy, and each one of them was extraordinarily painful. The entities often live at the heart of your system and have accrued tremendous amounts of logic and entanglement with various parts of the system. Building and migrating to the new data model can take many months of preparation, development and testing.

Architecture debt can be insidious and very damaging to productivity. Product or code compromises often have to be made in order to "fit into" the current architecture. Some of you may remember when YouTube migrated to support native Google accounts. This change took months (years?) and I have no doubt a tremendous internal engineering effort. 

I don't have any panacea to offer as a solution for architecture debt, but I do offer some recommendations to help make it more manageable:

-Maintain agility on your core data model. Separate features like billing info, contact info, and authorization settings from your core entities earlier than is strictly required. And make sure you have really good tests around your core data model.

-Separate features and concerns into distinct systems. I am [not a fan](http://scottp.org/2017/08/06/busting-the-monolith/) of the current "back to the monolith!" movement. Sure, too many microservices too early is a recipe for a headache. But when monoliths inevitably accrue architecture debt, they can be incredibly difficult to change. Even having a small-N number of cooperating services will give you the chance to rearchitect or rebuild one of them without having to rewrite your whole product.

-Go read [Domain Driven Design](https://dddcommunity.org/) by Eric Evans. And then read it again. And then re-read it every 12 months. The ability to iterate your system's model of the business domain is one of the keys to solving architecture debt.
