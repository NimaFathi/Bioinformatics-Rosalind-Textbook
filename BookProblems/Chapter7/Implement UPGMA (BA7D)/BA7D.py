import sys
import time


class Tree:
    def __init__(self, N: int):
        self.V = list(range(N))
        self.E = {}

    def add_edge(self, node1, node2, length):
        if node1 not in self.V:
            self.V.append(node1)
        if node1 in self.E:

            self.E[node1].append((node2, length))
        else:
            self.E[node1] = [(node2, length)]
        if node2 not in self.V:
            self.V.append(node2)
        if node2 in self.E:
            self.E[node2].append((node1, length))
        else:
            self.E[node2] = [(node1, length)]


def distance_clusters(D: list, i, j, clusters: dict):
    distance = 0
    if i in clusters and j in clusters:
        for ii in clusters[i]:
            for jj in clusters[j]:
                distance += D[ii][jj]
        return distance / (len(clusters[i]) * len(clusters[j]))


def find_closest(clusters: dict, D: list):
    min = sys.maxsize
    start = 0
    end = 0
    for i in range(len(D)):
        for j in range(i):
            if i in clusters and j in clusters:
                distance = distance_clusters(D, i, j, clusters)
                if distance < min:
                    min = distance
                    start = i
                    end = j
    return [start, end]


def UPGMA(D, n):
    tree = Tree(n)
    clusters = {}
    age = {}

    for i in range(n):
        clusters[i] = [i]

    for node in tree.V:
        age[node] = 0

    while len(clusters) > 1:
        i, j = find_closest(clusters, D)

        node = len(tree.V)

        clusters[node] = clusters[i] + clusters[j]

        tree.add_edge(node, j, 1)
        tree.add_edge(node, i, 1)

        del clusters[i]
        del clusters[j]

        age[node] = D[i][j] / 2

        new_row = []
        for k in range(len(D)):
            new_row.append(distance_clusters(D, k, node, clusters))
            D[k].append(new_row[k])
        D.append(new_row)

    for node in tree.V:
        tree.E[node] = [(e, abs(age[node] - age[e])) for e, _ in tree.E[node]]

    return tree


if __name__ == '__main__':
    INPUT_FILE_NAME = "rosalind_ba7d.txt"
    OUTPUT_FILE_NAME = "ba7d.txt"
    start_time = time.time()
    file = open(INPUT_FILE_NAME, "r")
    n = int(file.readline())
    d_array = []
    for line in file:
        v = list(map(int, line.split()))
        d_array.append(v)
    file.close()
    tree = UPGMA(d_array, n)
    tree.V.sort()
    file = open(OUTPUT_FILE_NAME, "w")
    for start in tree.V:
        if start in tree.E:
            new_list = []
            for edge in tree.E[start]:
                if edge not in new_list:
                    new_list.append(edge)
                    end, weight = edge
                    file.write('{0}->{1}:{2:.3f}'.format(start, end, weight))
                    file.write("\n")
    print("Runtime: {}s".format(time.time() - start_time))
