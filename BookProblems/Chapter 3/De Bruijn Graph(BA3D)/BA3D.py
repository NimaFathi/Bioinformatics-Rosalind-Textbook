INPUTEFILENAME = "rosalind_ba3d.txt"
OUTPUTFILENAME = "ba3d.txt"

def kmers_generator(k, text):
    return [text[i:i+k] for i in range(0, len(text) - (k-1))]



def match(kmers):
    graph = []
    def prefix(kmer):
        return kmer[0:len(kmer) - 1]

    def suffix(kmer):
        return kmer[1:]

    def presufix_match_checker(kmer1, kmer2):
        pre = prefix(kmer2)
        suf = suffix(kmer1)
        if  suf == pre:
            return True

    for kmer1 in kmers:
        for kmer2 in kmers:
            if presufix_match_checker(kmer1, kmer2):
                graph.append((kmer1,kmer2))

    return graph

def deBruijn_graph(k,text):
    deBruijnGraph = []
    kmers = kmers_generator(k-1, text)
    deBriujn_dict = dict()
    matchnodes = match(kmers)
    for i in range(0, len(kmers)):
        if kmers[i] not in deBriujn_dict.keys():
            deBriujn_dict[kmers[i]] = []
        else:
            continue
        for j in range(0, len(kmers)):
            if i == j:
                continue
            if kmers[i][1:] == kmers[j][0:len(kmers[j]) - 1]:
                deBriujn_dict[kmers[i]].append(kmers[j])

    for node in deBriujn_dict.keys():
        deBruijnGraph.append((node, sorted(list(set(deBriujn_dict[node])))))
    return sorted(deBruijnGraph)



if __name__ == '__main__':
    file = open(INPUTEFILENAME, "r")
    k = int(file.readline())
    text = file.readline()
    text = text
    file.close()
    file = open(OUTPUTFILENAME, "w+")
    dgraph = deBruijn_graph(k,text)
    for [a, mlist] in dgraph:
        file.write(a)
        if not mlist:
            continue
        file.write(" -> ")
        print(a, end=' -> ')
        for i in range(len(mlist)):
            if i == len(mlist) - 1:
                print(mlist[i])
                file.write(str(mlist[i]))
            else:
                print(mlist[i], end=',')
                file.write(str(mlist[i]))
                file.write(',')
        file.write("\n")
    file.close()
