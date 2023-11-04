#!/usr/bin/env python3

result = {}
for i in range(int(input())):
    k, v = input().split()
    result[k] = result.get(k, 0) + int(v)

r = list(result.items())
r.sort(key=lambda x: x[0])

for i in r:
    print(*i)
