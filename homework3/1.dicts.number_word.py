#!/usr/bin/env python3

conv = input().split()
res = dict()

for i in conv:
    n = res.get(i)
    if n:
        print(n, end=' ')
        res[i] += 1
    else:
        print('0', end=' ')
        res[i] = 1
