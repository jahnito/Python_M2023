#!/usr/bin/env python3

n = { i for i in range(int(input())) }
status = None

while True:
    line_pre = input()
    if line_pre == 'HELP':
        break
    else:
        line = { int(i) for i in line_pre.split() }
        status = input()
        if status == 'YES':
            n = n.intersection(line)
        else:
            n = n.difference(line)

print(*n)
