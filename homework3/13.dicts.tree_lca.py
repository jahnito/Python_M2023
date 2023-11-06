#!/usr/bin/env python3

def find(tree, name1, name2):
    ancestors1 = {name1}
    ancestors2 = {name2}
    while True:
        t = ancestors1.intersection(ancestors2)
        if len(t) == 1:
            return t
        else:
            if tree.get(name1):
                name1 = tree.get(name1)
            if tree.get(name2):
                name2 = tree.get(name2)
            ancestors1.add(name1)
            ancestors2.add(name2)

tree = {}

for i in range(int(input()) - 1):
    child, parent = input().split()
    tree[child] = parent
    if not tree.get(parent):
        tree[parent] = None

for i in range(int(input())):
    print(*find(tree, *input().split()))
