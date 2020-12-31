import sys

def hamming(str1, str2):
    HammingDistance = 0
    for i in range(len(str2)):
        if str1[i] != str2[i]:
            HammingDistance += 1
    return HammingDistance

def find_kmer(text, k):
    kmer_collection = []
    for i in range(len(text) - k):
        kmer_collection.append(text[i:i+k])
    return kmer_collection


def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = Pattern.__len__()
    distance = 0
    for dna_str in Dna:
        HammingDistance = sys.maxsize
        kmer_collection = find_kmer(dna_str,k)
        for kmer in kmer_collection:
            if HammingDistance > hamming(Pattern, kmer):
                HammingDistance = hamming(Pattern, kmer)
        distance += HammingDistance
    return distance

def kmersInDNA(Dna , k):
    possible_kmers = []
    for dna_str in Dna:
        for i in range(len(dna_str) - k):
            possible_kmers.append(dna_str[i:i+k])
    return set(possible_kmers)

def MedianString(Dna, k):
    distance = sys.maxsize
    def kmersInDNA():
        possible_kmers = []
        for dna_str in Dna:
            for i in range(len(dna_str) - k):
                possible_kmers.append(dna_str[i:i + k])
        return set(possible_kmers)
    for Pattern in kmersInDNA():
        if distance > DistanceBetweenPatternAndStrings(Pattern, Dna):
            distance = DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median = Pattern
    return Median


if __name__ == '__main__':
    INPUTFILENAME = 'rosalind_ba2b.txt'
    OUTPUTFILENAME = 'rosalind.txt'
    file = open(INPUTFILENAME, "r")
    k = int(file.readline())
    DNA = []
    for line in file:
        DNA.append(line.replace("\n", ""))
    file.close()
    file = open(OUTPUTFILENAME, "w")
    file.write(MedianString(DNA, k))