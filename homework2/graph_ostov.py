n = 6
w = [
    [0, 2, 4, 0, 0, 0],
    [2, 0, 9, 0, 1, 0],
    [4, 9, 0, 7, 0, 0],
    [0, 0, 7, 0, 8, 2],
    [0, 1, 0, 8, 0, 1],
    [0, 0, 0, 2, 1, 0]
]

col = [i for i in range(n)]

ostov = []

for k in range(n - 1):
    mindist = 1e10
    for i in range(n):
        for j in range(n):
            if col[i] != col[j] and 0 < w[i][j] < mindist:
                iMin = i
                jMin = j
                mindist = w[i][j]
    ostov.append((iMin, jMin))
    c = col[jMin]

    for i in range(n):
        if col[i] == c:
            col[i] = col[iMin]

for edge in ostov:
    print('(', edge[0], ',', edge[1], ')')
