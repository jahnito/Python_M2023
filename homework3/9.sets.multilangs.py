#!/usr/bin/env python3

n = int(input())
langs_all = set()
min_scool_man = None

for i in range(n):
    scool_man = set()
    for j in range(int(input())):
        lang = input()
        scool_man.add(lang)
        langs_all.add(lang)
    if min_scool_man and len(scool_man) < len(min_scool_man):
        min_scool_man = scool_man
    elif not min_scool_man:
        min_scool_man = scool_man

print(len(min_scool_man))
for i in sorted(min_scool_man):
    print(i)

print(len(langs_all))
for i in sorted(langs_all):
    print(i)
