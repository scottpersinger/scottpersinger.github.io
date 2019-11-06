---
layout: post
title: Python Profiling made easy
date: '2013-10-09 22:07:00'
---

This is more a reminder to myself of how to use the basic Python library’s tools for profiling.

Say you’ve got a nice function which is running slow:

object1.do_slow_stuff()
You can generate the profile data easily enough:

```
import cProfile
cProfile.runctx(“object1.do_slow_stuff()”, globals(), locals(), “profdata”)
```

If you don’t use the `runctx` version you can run into trouble in iPython finding variables defined at the repl prompt.

Now to analyze you’re results:

```
import pstats
p = pstats.Stats(“profdata”)
To print a list of functions taking the most time, try this:

p.sort_stats(‘cumulative’).print_stats(10)
  ncalls  tottime  percall  cumtime  percall filename:lineno(function)

        1    0.000    0.000   16.435   16.435 /celery/app/task.py:322(__call__)

        1    0.000    0.000   16.435   16.435 /mirror/tenant_actions.py:324(poll_db_task)

        5    0.002    0.000   16.427    3.285 /mirror/sync_machine.py:812(poll_database)
```

That says, “sort the stats by cumulative time spent inside each function and print the top 10”. Now what you’re looking for is when you have a big drop in total time. Like this:

```
    4    0.083    0.021   15.117    3.779 /lib/sf_adapter.py:1079(_process_data_change)    

    4    0.000    0.000    8.292    2.073 /lib/sf_adapter.py:89(update)
```

So there were 4 calls to _process_data_change which took 3.7 secs. This function (probably) called “update”, which constituted 2 secs, but that still leaves 1.7 secs doing something else. To figure out what that “something else” is, we can ask pstats for the functions that our “processdata_change” function called:

```
p.strip_dirs().print_callees(“_process_data_change”)

ncalls  tottime  cumtime

800    0.005    0.898  base.py:116(generateObject)

800    0.011    0.187  copy.py:145(deepcopy)

800    0.001    0.001  data_change.py:82(setSfId)
```

This shows us the time spent in each function called by the original one, and helps us spot which subroutines are the most expensive.
