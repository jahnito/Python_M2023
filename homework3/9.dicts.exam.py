voc = {}

def count_accent(word) -> int:
    c = 0
    for i in word:
        if 64 <= ord(i) <= 90:
            c += 1
    return c

def check_position(word, accent):
    for pos, i in enumerate(word):
        if (64 <= ord(i) <= 90) and (pos in accent):
            return True
    return False

for i in range(int(input())):
    word = input()
    for k, char in enumerate(word):
        if char != char.lower():
            if voc.get(word.lower()):
                voc[word.lower()].append(k)
            else:
                voc[word.lower()] = [k]

c = 0

for word in input().split():
    if count_accent(word) != 1:
        c += 1
        continue
    accent = voc.get(word.lower(), [])
    if not check_position(word, accent) and len(accent) > 0:
        c += 1

print(c)
