#!/usr/bin/env python3

vocabulary = {}
ws = set()

for i in range(int(input())):
    en_word, latin_words = input().split(' - ')
    for lw in latin_words.split():
        lw = lw.strip(',')
        if vocabulary.get(lw):
            ws.add(lw)
            vocabulary[lw].append(en_word)
        else:
            ws.add(lw)
            vocabulary[lw] = [en_word]

print(len(ws))

for i in sorted(vocabulary.keys()):
    print(i, '-', ', '.join(vocabulary.get(i)))
