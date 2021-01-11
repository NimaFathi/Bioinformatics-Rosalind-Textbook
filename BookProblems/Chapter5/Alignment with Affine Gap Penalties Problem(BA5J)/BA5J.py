import sys

from Chapter5.BLOSUMA62 import BLOSUMA62_dict, BLOSUMA62

sys.setrecursionlimit(10500)

'''
3 means match
1 means deletion
2 means insertion
'''


def global_affine_alignment(V, W):
    min = -10000
    gap_opening = -11
    gap_extension = -1
    lower = [[0 for _ in range(len(W) + 1)] for _ in range(len(V) + 1)]
    upper = [[0 for _ in range(len(W) + 1)] for _ in range(len(V) + 1)]
    middle = [[0 for _ in range(len(W) + 1)] for _ in range(len(V) + 1)]
    backtrack = [[0 for _ in range(len(W) + 1)] for _ in range(len(V) + 1)]
    for i in range(0, len(V) + 1):
        lower[i][0] = gap_opening + (gap_extension * i)
        if i == 0:
            for j in range(1, len(W) + 1):
                lower[i][j] = min
    for j in range(0, len(W) + 1):
        upper[0][j] = gap_opening + (gap_extension * j)
        if j == 0:
            for i in range(1, len(V) + 1):
                upper[i][j] = min
    for i in range(len(V) + 1):
        for j in range(len(W) + 1):
            if i == 0 and j == 0:
                middle[i][j] = 0
            elif i == 0 or j == 0:
                middle[i][j] = min
    seq1 = ""
    seq2 = ""
    switch = "m"
    for i in range(1, len(V) + 1):
        for j in range(1, len(W) + 1):
            score = BLOSUMA62[BLOSUMA62_dict[V[i - 1]]][BLOSUMA62_dict[W[j - 1]]]
            lower[i][j] = max(lower[i - 1][j] + gap_extension, middle[i - 1][j] + gap_opening)
            upper[i][j] = max(upper[i][j - 1] + gap_extension, middle[i][j - 1] + gap_opening)
            middle[i][j] = max(lower[i][j], upper[i][j], middle[i - 1][j - 1] + score)
            if middle[i][j] == lower[i][j]:
                backtrack[i][j] = 1
            elif middle[i][j] == upper[i][j]:
                backtrack[i][j] = 2
            elif middle[i][j] == middle[i - 1][j - 1] + score:
                backtrack[i][j] = 3
    i = len(V)
    j = len(W)
    while (i > 0) and (j > 0):
        if switch == 'm':
            if middle[i][j] == lower[i][j]:
                switch = "l"
                continue
            elif middle[i][j] == middle[i - 1][j - 1] + BLOSUMA62[BLOSUMA62_dict[V[i - 1]]][BLOSUMA62_dict[W[j - 1]]]:
                seq1 += V[i - 1]
                seq2 += W[j - 1]
                i -= 1
                j -= 1
                continue
            elif middle[i][j] == upper[i][j]:
                switch = 'u'
                continue
        elif switch == 'l':
            if lower[i][j] == lower[i - 1][j] + gap_extension:
                seq1 += V[i - 1]
                seq2 += "-"
                i -= 1
                continue
            elif lower[i][j] == middle[i - 1][j] + gap_opening:
                seq1 += V[i - 1]
                seq2 += "-"
                i -= 1
                switch = 'm'
                continue
        elif switch == 'u':
            if upper[i][j] == upper[i][j - 1] + gap_extension:
                seq1 += "-"
                seq2 += W[j - 1]
                j -= 1
                continue
            elif upper[i][j] == middle[i][j - 1] + gap_opening:
                seq1 += "-"
                seq2 += W[j - 1]
                switch = 'm'
                j -= 1
                continue
    sequ1r = ''.join([seq1[j] for j in range(-1, -(len(seq1) + 1), -1)])
    sequ2r = ''.join([seq2[j] for j in range(-1, -(len(seq2) + 1), -1)])
    return middle[len(V)][len(W)], sequ1r, sequ2r


if __name__ == '__main__':
    V = input()
    W = input()

    max_score, v_alignment, w_alignment = global_affine_alignment(V, W)
    print("{}\n{}\n{}".format(max_score, v_alignment, w_alignment))
