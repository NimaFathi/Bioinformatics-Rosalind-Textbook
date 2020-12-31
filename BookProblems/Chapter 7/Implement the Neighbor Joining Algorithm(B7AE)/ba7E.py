import sys
import time


class Tree(object):
    def __init__(self, N=0):
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

    def remove(self, src, des):
        adj_list = []
        for (edge, length) in self.E[src]:
            if edge == des:
                continue
            adj_list.append((edge, length))
        self.E[src] = adj_list
        adj_list1 = []
        for (edge, length) in self.E[des]:
            if edge == src:
                continue
            adj_list1.append((edge, length))
        self.E[des] = adj_list1

    def DFS(self, i, k, path=[], weights=[]):
        if i not in self.E:
            return False, []
        if len(path) == 0:
            path.append(i)
            weights.append(0)

        for node, w in self.E[i]:
            if node in path:
                continue
            extended_path = path + [node]
            extended_weight = weights + [w]
            if node == k:
                return True, list(zip(extended_path, extended_weight))
            else:
                is_found, pathed = self.DFS(node, k, extended_path, extended_weight)
                if is_found:
                    return is_found, pathed
        return False, []


def NeighborJoining(D, n, nodes):
    def TotalDistance(D, i):
        return sum(D[i])

    def NJMatrix(D):
        ln = len(D)
        NDJ = [[0 for _ in range(ln)] for _ in range(ln)]
        for i in range(ln):
            for j in range(i + 1, ln):
                # print(i, j, TotalDistance(D,i), TotalDistance(D,j))
                NDJ[i][j] = (n - 2) * D[i][j] - TotalDistance(D, i) - TotalDistance(D, j)
                NDJ[j][i] = NDJ[i][j]
        return NDJ

    def add_new_row(D, i, j):
        row = [0.5 * (D[k][i] + D[k][j] - D[i][j]) for k in range(len(D))] + [0]

        D.append(row)
        for x in range(n):
            D[x].append(row[x])
        return D

    def remove_row(D, x):
        new = []
        for i in range(len(D)):
            if i == x:
                continue
            row = []
            for j in range(len(D)):
                if j == x:
                    continue
                row.append(D[i][j])
            new.append(row)
        return new

    def find_min_NDJ(NDJ):
        min_val = sys.maxsize
        i = 0
        j = 0
        for i_itr in range(len(NDJ)):
            for j_itr in range(i_itr + 1, len(NDJ)):
                if i_itr == j_itr:
                    continue
                if NDJ[i_itr][j_itr] < min_val:
                    min_val = NDJ[i_itr][j_itr]
                    i = i_itr
                    j = j_itr
        return i, j

    if nodes is None:
        nodes = list(range(n))

    if n == 2:
        T = Tree()
        T.add_edge(nodes[0], nodes[1], D[0][1])
        return T

    NDJ_matrix = NJMatrix(D)

    i, j = find_min_NDJ(NDJ_matrix)
    delta = (TotalDistance(D, i) - TotalDistance(D, j)) / (n - 2)
    limb_i = (D[i][j] + delta) / 2
    limb_j = (D[i][j] - delta) / 2
    D = add_new_row(D, i, j)
    m = nodes[-1] + 1
    nodes.append(m)

    D = remove_row(D, max(i, j))
    D = remove_row(D, min(i, j))

    i = nodes[i]
    j = nodes[j]
    nodes.remove(i)
    nodes.remove(j)

    T = NeighborJoining(D, n - 1, nodes)

    T.add_edge(i, m, limb_i)
    T.add_edge(j, m, limb_j)
    return T


if __name__ == '__main__':
    INPUTFILENAME = "rosalind_ba7e.txt"
    OUTPUTFILENAME = "ba7e.txt"
    start = time.time()

    file = open(INPUTFILENAME, "r")
    n_in = int(file.readline())
    d_array = []
    for line in file:
        d_array.append(list(map(int, line.split())))
    T = NeighborJoining(d_array, n_in, list(range(n_in)))
    file.close()
    file = open(OUTPUTFILENAME, "w")
    T.V = sorted(T.V)
    for node in T.V:
        if node in T.E:
            for edge in T.E[node]:
                writestr = "{}->{}:{:.3f}".format(node, edge[0], edge[1])
                file.write(writestr + "\n")
    print("---------------")
    print("RunTime: {}".format(time.time() - start))
