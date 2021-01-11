import numpy

spectrum_score = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186,
    'X': 4,
    'Z': 5

}


def spectral_alignment_graph(spectral_vector, peptide, k):
    diff = {}
    m = 0
    acceptable_rows = []
    for i in peptide:
        m += spectrum_score[i]
        acceptable_rows.append(m)
        diff[m] = spectrum_score[i]
    delta = len(spectral_vector) - m
    m += 1
    score = numpy.full((m, m + delta, k + 1), float('-inf'))
    score_array = [[["" for i in range(k + 1)] for _ in range(m + delta)] for _ in range(m)]
    score[0][0][0] = 0

    for z in range(0, k + 1):
        for y in range(m + delta):
            for x in range(m):
                if x not in acceptable_rows:
                    continue
                c = []
                if z != 0:
                    for j in range(1, y + 1):
                        c.append(score[x - diff[x]][j - 1][z - 1])
                c.append(score[x - diff[x]][y - diff[x]][z])
                arg_max = numpy.argmax(c)
                if arg_max == len(c) - 1:
                    mstr = score_array[x - diff[x]][y - diff[x]][z]
                    mstr += "/"
                    mstr += str(y - diff[x])
                    score_array[x][y][z] = mstr
                else:
                    mstr = score_array[x - diff[x]][arg_max][z - 1]
                    mstr += "/"
                    mstr += str(arg_max)
                    score_array[x][y][z] = mstr
                m_max = max(c)
                score[x][y][z] = spectral_vector[y - 1] + m_max
    return m, m + delta, score, score_array


if __name__ == '__main__':
    INPUTFILE = 'rosalind_ba11j.txt'
    file = open(INPUTFILE, 'r')
    peptide = file.readline().replace("\n", '')
    spectral_vector = list(map(int, file.readline().split()))
    k = int(file.readline())
    x_dim, y_dim, score, path_score = spectral_alignment_graph(spectral_vector, peptide, k)
    file.close()

    max_val = float('-inf')
    max_index = 0
    for i in range(0, k + 1):
        if score[x_dim - 1][y_dim - 1][i] > max_val:
            max_index = i
            max_val = score[x_dim - 1][y_dim - 1][i]

    path_indices = list(map(int, path_score[x_dim - 1][y_dim - 1][max_index].split("/")[2:]))
    path_indices.append(len(spectral_vector))

    ans = ''
    prev = 0
    for i, path_index in enumerate(path_indices):
        diff = path_index - prev
        diff = diff - spectrum_score[peptide[i]]
        ans += peptide[i]
        if diff > 0:
            ans += '(' + "+" + str(diff) + ')'
        elif diff < 0:
            ans += '(' + str(diff) + ')'
        prev = path_index

    print(ans)
