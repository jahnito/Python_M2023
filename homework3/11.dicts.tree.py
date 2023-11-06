#!/usr/bin/env python3

tree = {}

def count(tree, name):
    c = 0
    while tree.get(name):
        c += 1
        name = tree.get(name)
    return c

for i in range(int(input()) - 1):
    child, parent = input().split()
    tree[child] = parent
    if not tree.get(parent):
        tree[parent] = None

for i in sorted(tree.keys()):
    print(i, count(tree, i))
