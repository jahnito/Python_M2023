#!/usr/bin/env python3

result = {}

while True:
    try:
        name, product, num = input().split()
        if result.get(name):
            result[name][product] = result[name].get(product, 0) + int(num)
        else:
            result[name] = {product: int(num)}
    except (EOFError, ValueError):
        break

for i in sorted(result.keys()):
    print(i + ':')
    for j in sorted(result[i].keys()):
        print(j, result[i][j])