import random
import sys

nucleotide_dc = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}




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


def Motif_cal(Profile, Dna):
    motifs_col = []
    k = len(Profile[0])
    for dna_str in Dna:
        bestmotif = ""
        motifscore = 0
        for i in range(len(dna_str) - k + 1):
            s = 1
            for j in range(k):
                s = s * Profile[nucleotide_dc[dna_str[i + j]]][j]
            if s >= motifscore:
                bestmotif = dna_str[i:i + k]
                motifscore = s
        motifs_col.append(bestmotif)
    return motifs_col


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


def RandomizedMotifSearch(DNA, k, t):
    motifs = []
    for i in range(t):
        kmer_col = kmers(k, DNA[i])
        motifs.append(kmer_col[random.randint(0, len(kmer_col) - 1)])
    BestMotifs = motifs
    counter = 0
    while True:
        counter += 1
        profile = Profile(motifs)
        motifs = Motif_cal(profile, DNA)
        if score(motifs) < score(BestMotifs):
            BestMotifs = motifs
        else:
            return BestMotifs


if __name__ == '__main__':
    INPUTFILE = 'rosalind_ba2f.txt'
    OUTPUTFILE = 'roslalind.txt'
    DNA = []
    file = open(INPUTFILE, "r")
    k, t = map(int, file.readline().split())
    for line in file:
        DNA.append(line.replace("\n", ""))
    file.close()
    minscore = sys.maxsize
    for i in range(1000):
        temp = RandomizedMotifSearch(DNA, k, t)
        if score(temp) < minscore:
            minscore = score(temp)
            best_motifs = temp
    file = open(OUTPUTFILE, "w")
    for motif in best_motifs:
        file.write(motif + "\n")
