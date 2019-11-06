---
layout: post
title: Installing Mysql-Python 1.2.4b4 on Mac OS X Lion
date: '2013-08-19 22:12:00'
---

My new service idea for the day is an online service which installs Mysql and all the right client libraries for you automatically. Would I pay $20 for that every time I got a new computer - for sure.

Here are the steps I followed to do it manually. Note that these are instructions for install the Mysql 1.2.4 package which is required to use SSL to connect to RDS. You need to download the package first:

Install Mysql 64 Bit package from Sun
export PATH=$PATH:/usr/local/mysql/bin
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/
export VERSIONER_PYTHON_PREFER_64_BIT=yes
export VERSIONER_PYTHON_PREFER_32_BIT=no
pip install ./pip/MySQL-python-1.2.4b4
Make sure to add DYLD_LIBRARY_PATH to your permanent environment.
 
