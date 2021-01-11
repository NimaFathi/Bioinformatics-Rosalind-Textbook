import sys
from collections import defaultdict


def construct_cycle(path):
    reconstructed_path = []
    min = sys.maxsize
    index = -1
    for i in range(len(path)):
        if int(path[i]) < min:
            min = int(path[i])
            index = i
    reconstructed_path = path[index:] + path[:index]
    return reconstructed_path


def MaximalNonBranchingPath(Adj_list, input_deg):
    pathes = []
    for node in Adj_list.keys():
        if len(Adj_list[node]) != 1 or input_deg[node] != 1:
            if len(Adj_list[node]) > 0:
                for w in Adj_list[node]:
                    path = [node, w]
                    while len(Adj_list[w]) == 1 and input_deg[w] == 1:
                        u = Adj_list[w][-1]
                        path.append(u)
                        w = u
                    if path:
                        pathes.append(path)
    return pathes, Adj_list, input_deg


if __name__ == '__main__':
    INPUTFILE = 'rosalind_ba3m.txt'
    OUTPUTFILE = 'rosalind.txt'
    file = open(INPUTFILE, 'r')
    adjacency_list = defaultdict(list)
    input_degree = defaultdict(int)
    for line in file:
        node = line.split(' -> ')[0]
        out_nodes = line.split(' -> ')[1]
        for x in out_nodes.split(","):
            adjacency_list[node].append(x.replace("\n", ""))
    for node in adjacency_list:
        for out_node in adjacency_list[node]:
            input_degree[out_node] += 1
    file.close()
    maxx = 0
    for x in adjacency_list:
        if int(x) > maxx:
            maxx = int(x)
    for y in range(maxx):
        if not adjacency_list[str(y)]:
            adjacency_list[str(y)] = []
    pathes, adjacency_list, input_degree = MaximalNonBranchingPath(adjacency_list, input_degree)
    flag = 0
    counter = 0
    for node in adjacency_list:
        path = []
        if len(adjacency_list[node]) == 1 and input_degree[node] == 1:
            w = adjacency_list[node][-1]
            u = 's'
            path = [node]
            while len(adjacency_list[w]) == 1 and input_degree[w] == 1:
                path.append(w)
                u = adjacency_list[w][-1]
                if u == path[0]:
                    path.append(u)
                    if flag == 0:
                        flag = 1
                        counter = len(path)
                    break
                w = u
            if path[0] == path[-1]:
                counter -= 1
                if counter == 1:
                    flag = 0
                    pathes.append(path)
    file = open(OUTPUTFILE, "w")
    for path in pathes:
        sting = ''
        for node in range(len(path)):
            if len(path) <= 1:
                break
            if node == len(path) - 1:
                sting += path[node]
            else:
                sting += path[node] + ' -> '
        if sting:
            file.write(sting)
            file.write("\n")
