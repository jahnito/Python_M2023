#!/usr/bin/env python3

print(*sorted(set(input().split()).intersection(input().split()), key=lambda x: int(x)))
