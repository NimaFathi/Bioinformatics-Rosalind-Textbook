import sys

sys.setrecursionlimit(3000)
'''
3 means match
1 means deletion
2 means insertion
'''


def LCS_backtrack(v, w):
    back_track = [[0 for _ in range(len(w) + 1)] for _ in range(len(v) + 1)]
    s = [[0 for _ in range(len(w) + 1)] for _ in range(len(v) + 1)]
    for i in range(len(w) + 1):
        s[0][i] = 0
    for i in range(len(v) + 1):
        s[i][0] = 0

    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            is_match = 0
            if v[i - 1] == w[j - 1]:
                is_match = 1
            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + is_match)
            if s[i][j] == s[i - 1][j]:
                back_track[i][j] = 2
            elif s[i][j] == s[i][j - 1]:
                back_track[i][j] = 1
            elif s[i][j] == s[i - 1][j] + is_match:
                back_track[i][j] = 3
    return back_track


def printLCS(backtrack, v, i, j):
    print(i,j)
    print(backtrack[i][j])
    if i == 0 or j == 0:
        return ""
    if backtrack[i][j] == 2:
        return printLCS(backtrack, v, i - 1, j)
    elif backtrack[i][j] == 1:
        return printLCS(backtrack, v, i, j - 1)
    elif backtrack[i][j] == 3:
        return printLCS(backtrack, v, i - 1, j - 1) + v[i - 1]


if __name__ == '__main__':
    v = input()
    w = input()
    backtrack = LCS_backtrack(v, w)
    x = printLCS(backtrack, v, len(v), len(w))
    print(x)
