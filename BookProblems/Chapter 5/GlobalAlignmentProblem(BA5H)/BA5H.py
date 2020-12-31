import sys

sys.setrecursionlimit(5500)
'''
3 means match
1 means deletion
2 means insertion
'''


def globalBacktack(V, W):
    global BLOSUMA62
    global BLOSUMA62_dict
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

    V = input()
    W = input()
    a,b,c = globalBacktack(V,W)
    print(a)
    print(b)
    print(c)