#!/usr/bin/env python3

tree = {}

def status(tree, name1, name2):
    parent, child = name1, name2
    while True:
        if tree.get(parent):
            if tree.get(parent) == child:
                return 2
            else:
                parent = tree.get(parent)
        else:
            break

    parent, child = name2, name1
    while True:
        if tree.get(parent):
            if tree.get(parent) == child:
                return 1
            else:
                parent = tree.get(parent)
        else:
            break
    return 0

for i in range(int(input()) - 1):
    child, parent = input().split()
    tree[child] = parent
    if not tree.get(parent):
        tree[parent] = None

for i in range(int(input())):
    print(status(tree, *input().split()), end=' ')
