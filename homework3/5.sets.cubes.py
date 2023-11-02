#!/usr/bin/env python3

a, b = [int(i) for i in input().split()]

anna = [int(input()) for i in range(a)]
boris = [int(input()) for i in range(b)]

print(len(set(anna).intersection(set(boris))))
print(*sorted(set(anna).intersection(set(boris))))
print(len(set(anna) - set(boris)))
print(*sorted(set(anna).difference(set(boris))))
print(len(set(boris) - set(anna)))
print(*sorted(set(boris).difference(set(anna))))
