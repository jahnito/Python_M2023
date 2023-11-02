#!/usr/bin/env python3

s = []

for i in range(int(input())):
    s.extend(map(lambda x: x.strip(), input().split()))

print(len(set(s)))
