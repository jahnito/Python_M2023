#!/usr/bin/env python3

result = {}

for i in range(int(input())):
    for j in input().split():
        result[j] = result.get(j, 0) + 1

m = max(result.values())

for i in result:
    if result[i] != m:
        del result[i]

r = list(result.items())
r.sort(key=lambda x: x[0])

print(r[0][0])
