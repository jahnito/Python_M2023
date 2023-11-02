#!/usr/bin/env python3

s = set()
line = input().split()
for i in line:
    if i in s:
        print('YES')
    else:
        print('NO')
    s.add(i)
