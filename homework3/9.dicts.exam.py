#!/usr/bin/env python3

voc = {}
for i in range(int(input())):
    word = input()
    for k, char in enumerate(word):
        if char != char.lower():
            if voc.get(word.lower()):
                voc[word.lower()].append(k)
            else:
                voc[word.lower()] = [k]

print(voc)
