import random
import sys

nucleotide_dc = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}


def Profile_randomly_generated_kmer(profile, i, dna, k):
    p = 1
    random_number = []
    random_cumulitive = []
    rsum = 0
    for j in range(len(dna) - k + 1):
        for index in range(k):
            p *= profile[nucleotide_dc[dna[index + j]]][index]
        random_number.append(p)
        p = 1
    s = sum(random_number)
    for index in range(len(random_number)):
        rsum += random_number[index]
        random_cumulitive.append(rsum / s)
    randomNum = random.random()
    for index in range(len(random_cumulitive)):
        if randomNum <= random_cumulitive[0]:
            return 0
        if randomNum >= random_cumulitive[len(random_cumulitive) - 2]:
            return len(random_cumulitive) - 1
        elif randomNum > random_cumulitive[index] and randomNum <= random_cumulitive[index + 1]:
            return index + 1


def score(Motifs):
    count = Count(Motifs)
    temp = []
    s = 0
    for i in range(len(Motifs[0])):
        for j in range(4):
            temp.append(count[j][i])
        s += len(Motifs) - max(temp)
        temp = []
    return s


def Count(Motifs):
    lmc = len(Motifs)
    lm = len(Motifs[0])
    count = [[1 for _ in range(lm)] for _ in range(4)]
    for i in range(lm):
        for j in range(lmc):
            count[nucleotide_dc[Motifs[j][i]]][i] += 1
    return count


def Profile(Motifs):
    lmc = len(Motifs)
    lm = len(Motifs[0])
    count = Count(Motifs)
    return [[count[i][j] / (lmc + 4) for j in range(lm)] for i in range(4)]


def kmers(k, dna_str):
    kmers_collection = []
    for i in range(len(dna_str) - k):
        kmers_collection.append(dna_str[i:i + k])
    return list(set(kmers_collection))


def GibsSampler(DNA, k, t, N):
    def dropOne(motifs, i):
        return [motifs[x] for x in range(len(motifs)) if x != i]

    motifs = []
    for i in range(t):
        kmer_col = kmers(k, DNA[i])
        motifs.append(kmer_col[random.randint(0, len(kmer_col) - 1)])

    best_motifs = motifs
    best_score = sys.maxsize
    for j in range(N):
        i = random.randint(0, t - 1)
        profile = Profile(dropOne(motifs, i))
        x = Profile_randomly_generated_kmer(profile, i, DNA[i], k)
        motifs[i] = DNA[i][x:x + k]
        mscore = score(motifs)
        if mscore < best_score:
            best_score = mscore
            best_motifs = motifs
    return best_motifs


if __name__ == '__main__':
    INPUT_FILE_NAME = 'rosalind_ba2g.txt'
    OUTPUT_FILE_NAME = 'rosalind.txt'
    file = open(INPUT_FILE_NAME, "r")
    k, t, N = map(int, file.readline().split())
    DNA = []
    for line in file:
        DNA.append(line.replace("\n", ""))
    min_score = sys.maxsize
    for i in range(20):
        x = GibsSampler(DNA, k, t, N)
        if score(x) < min_score:
            best = x
            min_score = score(x)
    for motif in best:
        print(motif)
