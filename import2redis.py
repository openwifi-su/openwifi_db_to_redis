#!/usr/bin/env python
#-*- coding: utf-8 -*-
import redis
redis_key_prefix = "WP_"
r = redis.Redis(connection_pool= redis.ConnectionPool(host='localhost', port=6379, db=1))
fh = open('db.csv','r')
cnt = 0
for line in fh:
    cnt +=1
    if cnt < 2:
        continue
    arr = line.strip().split("\t")
    r.set(redis_key_prefix+arr[0],"{} {}".format(arr[1],arr[2]))
fh.close()

