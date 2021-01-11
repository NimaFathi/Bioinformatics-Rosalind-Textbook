def kmp(pattern, text):
    ans = []
    n = len(pattern)
    m = len(text)
    lps = len(pattern) * [0]
    LPSArray(pattern, n, lps)
    i = 0
    j = 0
    while i < m:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == n:
            ans.append(i - j)
            j = lps[j - 1]
        elif i < m and pattern[j] != text[i]:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
    return ans


def LPSArray(pattern, m, lps):
    previous = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[previous]:
            previous += 1
            i += 1
            lps[i - 1] = previous
        else:
            if previous != 0:
                previous = lps[previous - 1]
            else:
                lps[i] = 0
                i += 1


if __name__ == '__main__':
    pat = input()
    txt = input()
    s = kmp(pat, txt)
    for i in s:
        print(i, end=' ')
