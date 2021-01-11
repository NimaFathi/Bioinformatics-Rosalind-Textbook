INPUT_FILE_NAME = "rosalind_ba3d.txt"
OUTPUT_FILE_NAME = "ba3d.txt"


def kmers_generator(k, text):
    return [text[i:i + k] for i in range(0, len(text) - (k - 1))]


def deBruijn_graph(k, text):
    deBruijnGraph = []
    kmers = kmers_generator(k - 1, text)
    deBriujn_dict = dict()
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
    file = open(INPUT_FILE_NAME, "r")
    k = int(file.readline())
    text = file.readline()
    text = text
    file.close()
    file = open(OUTPUT_FILE_NAME, "w+")
    dgraph = deBruijn_graph(k, text)
    for [a, adj_list] in dgraph:
        file.write(a)
        if not adj_list:
            continue
        file.write(" -> ")
        print(a, end=' -> ')
        for i in range(len(adj_list)):
            if i == len(adj_list) - 1:
                print(adj_list[i])
                file.write(str(adj_list[i]))
            else:
                print(adj_list[i], end=',')
                file.write(str(adj_list[i]))
                file.write(',')
        file.write("\n")
    file.close()
