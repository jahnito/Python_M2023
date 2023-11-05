#!/usr/bin/env python3

words = {}
for i in range(int(input())):
    for word in input().split():
        words[word] = words.get(word, 0) + 1

s = [(-v, k) for k, v in words.items()]
s.sort()

for i in s:
    print(i[1])
