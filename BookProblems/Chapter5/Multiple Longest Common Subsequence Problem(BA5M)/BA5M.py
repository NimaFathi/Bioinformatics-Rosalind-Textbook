def multipleAlignment(v, w, u):
    s = [[[0 for _ in range(len(u) + 1)] for _ in range(len(w) + 1)] for _ in range(len(v) + 1)]
    reformatted_v = ""
    reformatted_w = ""
    reformatted_u = ""
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            for k in range(1, len(u) + 1):
                if v[i - 1] == w[j - 1] == u[k - 1]:
                    score = 1
                else:
                    score = 0
                s[i][j][k] = max(s[i - 1][j][k], s[i][j - 1][k], s[i][j][k - 1], s[i - 1][j - 1][k], s[i - 1][j][k - 1],
                                 s[i][j - 1][k - 1],
                                 s[i - 1][j - 1][k - 1] + score)

    i = len(v)
    j = len(w)
    k = len(u)
    # backtrack
    while i > 0 and j > 0 and k > 0:
        if s[i][j][k] == s[i - 1][j][k]:
            i = i - 1
            reformatted_v += v[i]
            reformatted_w += "-"
            reformatted_u += "-"
        elif s[i][j][k] == s[i][j - 1][k]:
            j = j - 1
            reformatted_v += "-"
            reformatted_w += w[j]
            reformatted_u += "-"
        elif s[i][j][k] == s[i][j][k - 1]:
            k -= 1
            reformatted_v += "-"
            reformatted_w += "-"
            reformatted_u += u[k]
        elif s[i][j][k] == s[i - 1][j - 1][k - 1]:
            i -= 1
            j -= 1
            reformatted_v += v[i]
            reformatted_w += w[j]
            reformatted_u += "-"
        elif s[i][j][k] == s[i - 1][j][k - 1]:
            i -= 1
            k -= 1
            reformatted_v += v[i]
            reformatted_w += "-"
            reformatted_u += w[k]
        elif s[i][j][k] == s[i][j - 1][k - 1]:
            j -= 1
            k -= 1
            reformatted_v += ""
            reformatted_w += w[j]
            reformatted_u += u[k]
        else:
            i -= 1
            j -= 1
            k -= 1
            reformatted_v += v[i]
            reformatted_w += w[j]
            reformatted_u += u[k]
    # check if one or two of sequence still has some letters or not
    while i > 0 or j > 0 or k > 0:
        if i > 0 and j > 0:
            i -= 1
            j -= 1
            reformatted_v += v[i]
            reformatted_w += w[j]
            reformatted_u += "-"
        elif i > 0 and k > 0:
            i -= 1
            k -= 1
            reformatted_v += v[i]
            reformatted_w += '-'
            reformatted_u += u[k]
        elif j > 0 and k > 0:
            j -= 1
            k -= 1
            reformatted_v += '-'
            reformatted_w += w[j]
            reformatted_u += u[k]
        elif i > 0:
            i -= 1
            reformatted_v += v[i]
            reformatted_w += '-'
            reformatted_u += '-'
        elif j > 0:
            j -= 1
            reformatted_v += '-'
            reformatted_w += w[j]
            reformatted_u += '-'
        else:
            k -= 1
            reformatted_v += '-'
            reformatted_w += '-'
            reformatted_u += u[k]

    reformatted_v = ''.join([reformatted_v[i] for i in range(-1, -(len(reformatted_v) + 1), -1)])
    reformatted_w = ''.join([reformatted_w[i] for i in range(-1, -(len(reformatted_w) + 1), -1)])
    reformatted_u = ''.join([reformatted_u[i] for i in range(-1, -(len(reformatted_u) + 1), -1)])
    return s[len(v)][len(w)][len(u)], reformatted_v, reformatted_w, reformatted_u


if __name__ == '__main__':
    v = input()
    w = input()
    u = input()
    score, new_v, new_w, new_u = multipleAlignment(v, w, u)
    print(score)
    print(new_v)
    print(new_w)
    print(new_u)
