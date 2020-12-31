INPUTFILENAME = "rosalind_ba3k.txt"
OUTPUTFILENAME = "ba3k.txt"


def contig_generator(debruijn_graph):
    contigs = []
    for path in maximal_non_branching_path(debruijn_graph):
        contig = path[0]
        for node in path[1:]:
            contig += node[-1]
        contigs.append(contig)
    return contigs


def maximal_non_branching_path(debruijn_graph):
    inout_degree = inout(debruijn_graph)
    paths = []
    for node in inout_degree:
        (node_in, node_out) = inout_degree[node]
        if node_in != 1 or node_out != 1:
            if node_out > 0:
                for v in debruijn_graph[node]:
                    path = [node, v]
                    v_in, v_out = inout_degree[v]
                    while v_in == 1 and v_out == 1:
                        w = debruijn_graph[v].pop(0)
                        path.append(w)
                        v_in = inout_degree[w][0]
                        v_out = inout_degree[w][1]
                        v = w
                    paths.append(path)
    return paths + isolated_cycles(debruijn_graph)


def deBruijn(patterns):
    def prefix(pattern):
        return pattern[0:-1]

    def suffix(pattern):
        return pattern[1:]

    debruijn_graph = {}
    k = len(patterns[0])
    for pattern in patterns:
        if prefix(pattern) not in debruijn_graph:
            debruijn_graph[prefix(pattern)] = []
        debruijn_graph[prefix(pattern)].append(suffix(pattern))
        debruijn_graph[prefix(pattern)].sort()
    return debruijn_graph


def inout(debruijn_graph):
    inout_dict = {}
    for node, outDegree in debruijn_graph.items():
        inout_dict[node] = [0, len(outDegree)]
    for node, outDegree in debruijn_graph.items():
        for outNode in outDegree:
            if outNode not in inout_dict.keys():
                inout_dict[outNode] = [0, 0]
            inout_dict[outNode][0] += 1
    return inout_dict


def isolated_cycles(debruijn):
    isolateds = []
    for node in debruijn:
        cycle = [node]
        curr_node = node
        while curr_node in debruijn and len(debruijn[curr_node]) == 1:
            next = debruijn[curr_node][0]
            if next == node:
                isolateds.append(cycle)
            else:
                cycle.append(next)
            curr_node = next
    return isolateds


if __name__ == '__main__':
    file = open(INPUTFILENAME, "r")
    patterns = []
    for line in file:
        patterns.append(line[:-1])
    file.close()
    file = open(OUTPUTFILENAME, "w+")
    contigs = contig_generator(debruijn_graph=deBruijn(patterns))
    for contig in contigs:
        print(contig)
        file.write(str(contig))
        file.write("\n")
    file.close()
