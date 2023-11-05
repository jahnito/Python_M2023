#!/usr/bin/env python3

lands = {}
for i in range(int(input())):
    k, *v = input().split()
    lands[k] = v

for i in range(int(input())):
    city = input()
    for land in lands:
        if city in lands.get(land):
            print(land)
