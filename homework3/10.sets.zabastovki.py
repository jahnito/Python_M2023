#!/usr/bin/env python3

N, K = [int(i) for i in input().split()]
A = set()
zab = [[int(i) for i in input().split()] for j in range(K)]
for i in range(K):
    for j in range(zab[i][0], N + 1, zab[i][1]):
        if j % 7 != 0 and j % 7 != 6:
            A.add(j)
print(len(A))
