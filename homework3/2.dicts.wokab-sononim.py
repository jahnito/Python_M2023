#!/usr/bin/env python3

res = dict()
for i in range(int(input())):
    k, v = input().split()
    res[k] = v
    res[v] = k

print(res.get(input()))
