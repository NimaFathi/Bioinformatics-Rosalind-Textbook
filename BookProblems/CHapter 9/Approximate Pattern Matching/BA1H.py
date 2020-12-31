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

def eulerianDistance(pattern1, pattern2):
    distance = 0
    for i in range(0, len(pattern1)):
        if i >= len(pattern2):
            distance += len(pattern1) - len(pattern2)
            break
        if pattern1[i] != pattern2[i]:
            distance += 1
    return distance

def kmerGenerator(pattern, d):
    length = len(pattern)
    k = length // (d+1)
    kmers = []
    for i in range(0, d):
        kmers.append(pattern[k*i:k*(i+1)])
    kmers.append(pattern[k*d:])
    return kmers, k





def patternMatching(pattern, text, d):
    kmers, k = kmerGenerator(pattern, d) #generate k-mers
    ans = []
    for i in range(0, len(kmers) - 1):
        indices = kmp(kmers[i], text)
        if indices: #if not null
            for index in indices:
                if index - k*i <0:
                    continue
                mismatch = 0
                for j in range(0, i): #Left-hand side
                    mismatch += eulerianDistance(kmers[j], text[index + k * (j - i):index + k * (j - i) + k])
                    if mismatch > d:
                        break
                for j in range(i+1, len(kmers)-1): #Right-hand side
                    mismatch += eulerianDistance(kmers[j], text[index + k * (j - i):index + k * (j - i) + k])
                    if mismatch > d:
                        break
                mismatch += eulerianDistance(kmers[-1], text[index + k * (len(kmers) - i - 1): index + k * (len(kmers) - i - 1) + len(kmers[-1])])
                if mismatch <= d:
                    ans.append(index - k*(i))
    indices = kmp(kmers[-1], text)

    for index in indices:
        if index < k * d:
            continue
        subtext = text[index-k*d:index]
        mismatch = eulerianDistance(pattern[0:k * d], subtext)
        if mismatch <=d:
            ans.append(index - k * d)
    return sorted(list(set(ans)))


if __name__ == '__main__':
    INPUTFILENAME = "rosalind_ba1h.txt"
    OUTPUTFILENAME = "ba1h.txt"
    file = open(INPUTFILENAME, "r")
    pattern = file.readline()[:-1]
    text = file.readline()[:-1]
    d = int(file.readline())
    file.close()
    answer = patternMatching(pattern,text,d)
    file = open(OUTPUTFILENAME, "w+")
    for i in answer:
        file.write(str(i))
        file.write(" ")
    file.close()