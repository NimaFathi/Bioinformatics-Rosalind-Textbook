import sys
sys.setrecursionlimit(10500)

'''
3 means match
1 means deletion
2 means insertion
'''
def GlobalAffineAlignment(V, W):
    min = -10000
    gap_opening = -11
    gap_extension = -1
    lower = [[0 for _ in range(len(W)+1)] for _ in range(len(V)+1)]
    upper = [[0 for _ in range(len(W)+1)] for _ in range(len(V)+1)]
    middle = [[0 for _ in range(len(W)+1)] for _ in range(len(V)+1)]
    backtrack = [[0 for _ in range(len(W)+1)] for _ in range(len(V)+1)]
    for i in range(0, len(V) + 1):
        lower[i][0] = gap_opening + (gap_extension * i)
        if i == 0:
            for j in range(1,len(W)+1):
                lower[i][j] = min
    for j in range(0, len(W) + 1):
        upper[0][j] = gap_opening + (gap_extension * j)
        if j == 0 :
            for i in range(1, len(V) + 1):
                upper[i][j] = min
    for i in range(len(V)+1):
        for j in range(len(W)+1):
            if i == 0 and j == 0:
                middle[i][j] = 0
            elif i ==0 or j == 0:
                middle[i][j] = min
    seq1 = ""
    seq2 = ""
    switch = "m"
    for i in range(1, len(V) + 1):
        for j in range(1, len(W) + 1):
            score = BLOSUMA62[BLOSUMA62_dict[V[i-1]]][BLOSUMA62_dict[W[j-1]]]
            lower[i][j] = max(lower[i-1][j] + gap_extension, middle[i-1][j] + gap_opening)
            upper[i][j] = max(upper[i][j-1] + gap_extension, middle[i][j-1] + gap_opening)
            middle[i][j] = max(lower[i][j], upper[i][j], middle[i-1][j-1] + score)
            if middle[i][j] == lower[i][j]:
                backtrack[i][j] = 1
            elif middle[i][j] == upper[i][j]:
                backtrack[i][j] = 2
            elif middle[i][j] == middle[i-1][j-1] + score:
                backtrack[i][j] = 3
    i = len(V)
    j = len(W)
    while (i > 0) and (j > 0):
        if switch == 'm':
            if middle[i][j] == lower[i][j]:
                switch = "l"
                continue
            elif middle[i][j] == middle[i-1][j-1] + BLOSUMA62[BLOSUMA62_dict[V[i-1]]][BLOSUMA62_dict[W[j-1]]]:
                seq1 += V[i-1]
                seq2 += W[j-1]
                i -= 1
                j -= 1
                continue
            elif middle[i][j] == upper[i][j]:
                switch = 'u'
                continue
        elif switch == 'l':
            if lower[i][j] == lower[i-1][j] + gap_extension:
                seq1 += V[i-1]
                seq2 += "-"
                i -= 1
                continue
            elif lower[i][j] == middle[i-1][j] + gap_opening:
                seq1 += V[i-1]
                seq2 += "-"
                i -= 1
                switch = 'm'
                continue
        elif switch == 'u':
            if upper[i][j] == upper[i][j-1] + gap_extension:
                seq1 += "-"
                seq2 += W[j-1]
                j -= 1
                continue
            elif upper[i][j] == middle[i][j-1] + gap_opening:
                seq1 += "-"
                seq2 += W[j-1]
                switch = 'm'
                j -= 1
                continue
    sequ1r = ''.join([seq1[j] for j in range(-1, -(len(seq1) + 1), -1)])
    sequ2r = ''.join([seq2[j] for j in range(-1, -(len(seq2) + 1), -1)])
    print(middle[len(V)][len(W)])
    print(sequ1r)
    print(sequ2r)



if __name__ == '__main__':
    V = input()
    W = input()

    BLOSUMA62 = [[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
                [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
                [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
                [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
                [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
                [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
                [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
                [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
                [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
                [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
                [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
                [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
                [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
                [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
                [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
                [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
                [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
                [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
                [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
                [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]
                ]

    BLOSUMA62_dict = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9, 'M': 10, 'N': 11,
                      'P': 12, 'Q': 13, 'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19}
    GlobalAffineAlignment(V,W)
