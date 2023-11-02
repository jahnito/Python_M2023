#!/usr/bin/env python3

n = { i for i in range(1, int(input()) + 1) }
k = len(n)
while True:
    line_pre = input()
    if line_pre == 'HELP':
        break
    else:
        line = { int(i) for i in line_pre.split() }
        if len(n.intersection(line)) > len(n.difference(line)):
            n = n.intersection(line)
            print('YES')
        elif len(n.intersection(line)) <= len(n.difference(line)):
            n = n.difference(line)
            print('NO')
        elif len(line) == k / 2:
            n = n.difference(line)
            print('NO')
print(*n)
