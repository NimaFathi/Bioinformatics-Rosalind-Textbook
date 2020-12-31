from numpy import argmax


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

    return sequ1, sequ2


def middlecolumn_score(v, w, indel):
    score = [[i * j * indel for j in range(-1, 1)] for i in range(len(v) + 1)]
    backtrack = [0] * (len(v) + 1)
    floor = len(w) // 2

    for i in range(1, floor + 1):
        for j in range(0, len(v) + 1):
            if j == 0:
                score[j][1] = -i * indel
            else:
                score_match = BLOSUMA62[BLOSUMA62_dict[v[j - 1]]][BLOSUMA62_dict[w[i - 1]]]
                scores = [score[j - 1][0] + score_match, score[j][0] - indel, score[j - 1][1] - indel]
                score[j][1] = max(scores)
                backtrack[j] = argmax(scores)

        if i != len(w) / 2:
            score = [[row[1]] * 2 for row in score]

    return [row[1] for row in score], backtrack


def middleEdge(v, w, sigma=5):
    source_to_middle = middlecolumn_score(v, w, sigma)[0]
    copy_w = w[::-1]
    if len(w) % 2 == 1 and len(w) > 1:
        copy_w += "/"
    middle_to_sink, backtrack = middlecolumn_score(v[::-1], copy_w, sigma)
    middle_to_sink = middle_to_sink[::-1]
    backtrack = backtrack[::-1]
    scores = list(map(sum, zip(source_to_middle, middle_to_sink)))

    maxarg = argmax(scores)
    floor = len(w) // 2
    if maxarg == len(scores) - 1:
        next_node = (maxarg, floor + 1)
    else:
        next_node = [(maxarg + 1, floor + 1), (maxarg, floor + 1), (maxarg + 1, floor), ][
            backtrack[maxarg]]
    mid_node = [0] * 2
    mid_node[0] = maxarg
    mid_node[1] = floor
    return mid_node, list(next_node)


def linearMem_global_alignment(v, w, sigma):
    def linear_space_alignment(top, bottom, left, right):
        if left == right:
            return [v[top:bottom], '-' * (bottom - top)]

        elif top == bottom:
            return ['-' * (right - left), w[left:right]]

        elif bottom - top == 1 or right - left == 1:
            return globalBacktack(v[top:bottom], w[left:right])

        else:
            mid_node, next_node = middleEdge(v[top:bottom], w[left:right], sigma)
            mid_node[0] += top
            next_node[0] += top
            mid_node[1] += left
            next_node[1] += left
            x = v[mid_node[0]] if next_node[0] - mid_node[0] == 1 else "-"
            y = w[mid_node[1]] if next_node[1] - mid_node[1] == 1 else "-"
            current_pos = [x, y]
            topLeftRect = linear_space_alignment(top, mid_node[0], left, mid_node[1])
            bottomRightRect = linear_space_alignment(next_node[0], bottom, next_node[1], right)
            return [topLeftRect[i] + current_pos[i] + bottomRightRect[i] for i in range(2)]

    reformatted_v, reformatted_w = linear_space_alignment(0, len(v), 0, len(w))

    i = len(reformatted_v) - 1
    score = 0
    while i >= 0:
        if reformatted_v[i] == '-' or reformatted_w[i] == '-':
            score += -sigma
        else:
            score += BLOSUMA62[BLOSUMA62_dict[reformatted_v[i]]][BLOSUMA62_dict[reformatted_w[i]]]
        i -= 1

    return score, reformatted_v, reformatted_w


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
    v = input()
    w = input()
    score, new_v, new_w = linearMem_global_alignment(v, w, 5)
    print(score)
    print(new_v)
    print(new_w)
