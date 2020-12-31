import sys
def limb(D,j):
    min = sys.maxsize
    for i in range(len(D)):
        if i == j:
            continue
        for k in range(len(D)):
            if k == j:
                continue
            limb = (D[i][j] + D[k][j] - D[i][k])/2
            if limb < min:
                min = limb
    return min


if __name__ == '__main__':
    INPUTFILENAME = "rosalind_ba7b.txt"
    OUTPUTFILENAME = "ba7b.txt"
    file = open(INPUTFILENAME, "r")
    n = file.readline()
    j = int(file.readline())
    d_array = []
    for line in file:
        v = list(map(int, line.split()))
        d_array.append(v)
    file.close()
    file = open(OUTPUTFILENAME, "w+")
    file.write(str(int(limb(d_array,j))))