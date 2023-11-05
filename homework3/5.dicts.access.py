#!/usr/bin/env python3

files = {}

def rights(s):
    x = 0
    if 'R' in s[1:]:
        x += 4
    if 'W' in s[1:]:
        x += 2
    if 'X' in s[1:]:
        x += 1
    return x

def check_rights(file, r):
    if r == 'read' and (file // 4) == 1:
        return True
    if r == 'write' and (file % 4 // 2) == 1:
        return True
    if r == 'execute' and (file % 4 % 2) == 1:
        return True
    else:
        return False

for i in range(int(input())):
    file = input().split()
    files[file[0]] = rights(file)

for i in range(int(input())):
    r, f = input().split()
    if check_rights(files[f], r):
        print('OK')
    else:
        print('Access denied')
