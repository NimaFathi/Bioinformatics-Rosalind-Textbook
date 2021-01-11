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
    return back_track, s[len(V)][len(W)]


def outputGlobalAlignment(back_track, v, i, j):
    if back_track[i][j] == 1:
        i -= 1
        return outputGlobalAlignment(back_track, v, i, j) + v[i]
    elif back_track[i][j] == 2:
        j -= 1
        return outputGlobalAlignment(back_track, v, i, j) + "-"
    elif back_track[i][j] == 3:
        i -= 1
        j -= 1
        return outputGlobalAlignment(back_track, v, i, j) + v[i]
    if i == 0 or j == 0:
        return ""


if __name__ == '__main__':
    V = input()
    W = input()
    back_track, score = globalBacktack(V, W)
    x = outputGlobalAlignment(list(back_track), V, len(V), len(W))
    print(score)
    print(x)
    back_track, _ = globalBacktack(W, V)
    y = outputGlobalAlignment(list(back_track), W, len(W), len(V))
    print(y)
    count = 0
