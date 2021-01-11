import sys

from Chapter5.BLOSUMA62 import BLOSUMA62_dict, BLOSUMA62

sys.setrecursionlimit(5500)
'''
3 means match
1 means deletion
2 means insertion
'''


def globalBacktack(V, W):
    indel = -5
    back_track = [[0 for _ in range(len(W) + 1)] for _ in range(len(V) + 1)]
    s = [[0 for _ in range(len(W) + 1)] for _ in range(len(V) + 1)]
    for i in range(len(V) + 1):
        s[i][0] = -5 * (i)
    for j in range(len(W) + 1):
        s[0][j] = -5 * (j)
    for i in range(1, len(W) + 1):
        back_track[0][i] = 2
    for j in range(1, len(V) + 1):
        back_track[j][0] = 1

    for i in range(1, len(V) + 1):
        for j in range(1, len(W) + 1):
            match_score = BLOSUMA62[BLOSUMA62_dict[V[i - 1]]][BLOSUMA62_dict[W[j - 1]]]
            s[i][j] = max(s[i - 1][j] + indel, s[i][j - 1] + indel, s[i - 1][j - 1] + match_score)
            if s[i][j] == (s[i - 1][j] + indel):
                back_track[i][j] = 1
            elif s[i][j] == (s[i][j - 1] + indel):
                back_track[i][j] = 2
            elif s[i][j] == (s[i - 1][j - 1] + match_score):
                back_track[i][j] = 3
    i = len(V)
    j = len(W)
    seq1 = ""
    seq2 = ""
    while (i > 0) and (j > 0):
        if back_track[i][j] == 1:
            i -= 1
            seq1 += V[i]
            seq2 += "-"
        elif back_track[i][j] == 2:
            j -= 1
            seq2 += W[j]
            seq1 += "-"
        elif back_track[i][j] == 3:
            j -= 1
            i -= 1
            seq1 += V[i]
            seq2 += W[j]
    while i > 0 or j > 0:
        if i > 0:
            i -= 1
            seq1 += V[i]
            seq2 += "-"
        elif j > 0:
            j -= 1
            seq1 += "-"
            seq2 += W[j]
    sequ1 = ''.join([seq1[j] for j in range(-1, -(len(seq1) + 1), -1)])
    sequ2 = ''.join([seq2[j] for j in range(-1, -(len(seq2) + 1), -1)])
    return s[len(V)][len(W)], sequ1, sequ2


if __name__ == '__main__':
    V = input()
    W = input()
    max_score, v_alignment, w_alignment = globalBacktack(V, W)
    print(max_score)
    print(v_alignment)
    print(w_alignment)
