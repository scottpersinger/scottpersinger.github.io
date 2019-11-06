---
layout: post
title: Dependency injection in PHP is a really bad idea
date: '2012-01-12 22:17:00'
---

I’m not a huge fan of dependency injection. Anytime you move logic out of code and into some XML file you’re making your application harder to understand.

The argument for dependency injection is that it makes your application more flexible by creating a loose coupling between components. So rather than having a hard-coded line of code to instantiate a concrete instance of some logger class, instead you move the type choice out into some configuration file.

Dependency injection was popularized by the Spring framework in Java. Now I can almost, sort of, see the benefit of DI when using Java, where the compile-jar-startup cycle can be quite long. (Although I think most cases are probably better handled by a basic factory pattern.) When you’re using a static-typed language like Java, then DI can introduce some late binding where types don’t have to be resolved until runtime.

But recently I’ve gotten the peculiar pleasure of getting to work on a PHP application using the Symfony 2 framework. Symfony includes a DI system taking inspiration from Spring. They even have a really nice web page describing the system, which includes this great feature: “comes bundled with a Graphviz dumper, allowing you to visualize the graph of your objects and ease the debugging of your container”.

The only problem is that dependency injection is a terrible idea in PHP. After all, PHP is a loosely typed, dynamic language. If you want to use a different class for your logger, well then you just assign your “logger” variable to some other object. Objects are duck-typed in PHP, you can call “logMessage” on any old object you like. There’s no compile-link-debug cycle to avoid by moving type resolution into some XML file!!

You want to choose a different logger at runtime? Just set some config option (say in php.ini or your own config system or in an env variable) and choose your logger class at runtime based on the config value. You can even put the logger class name in your config, and use: “$logger = new $loggerClassName;”. Please, please, do not start littering your code with XML files, and forcing yourself to “visualize the graph of your objects to ease debugging of your container”!!

Dependency injection is a crummy solution to a problem specific to the limitations of complex, statically-typed systems. It really has no benefit in a dynamic language like PHP.