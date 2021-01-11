def kmp(pattern, text):
    ans = 0
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
            ans += 1
            j = lps[j - 1]
        elif i < m and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return ans


def LPSArray(pat, M, lps):
    previous = 0
    i = 1
    while i < M:
        if pat[i] == pat[previous]:
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
    txt = input()
    pat = input()
    print(kmp(pat, txt))
