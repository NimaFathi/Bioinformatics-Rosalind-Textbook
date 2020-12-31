import sys
import time


class Tree(object):
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


def find_3leaves(D, j):
    for i in range(len(D)):
        for k in range(len(D)):
            if D[i][j] + D[j][k] == D[i][k]:
                return i, k, j


def limb(D, j):
    min = sys.maxsize
    for i in range(len(D)):
        if i == j:
            continue
        for k in range(len(D)):
            if k == j:
                continue
            limb = (D[i][j] + D[k][j] - D[i][k]) / 2
            if limb < min:
                min = limb
    return min


def find_V(path, x):
    cumulitive_weight = 0
    for node, weight in path:
        prev_cw = cumulitive_weight
        cumulitive_weight += weight
        if cumulitive_weight == x:
            return Tree, node, node, prev_cw, cumulitive_weight
        if cumulitive_weight > x:
            return False, prev_node, node, prev_cw, cumulitive_weight
        prev_node = node


def AdditivePhylogeny(D, n):
    def create_V(prev, curr, prev_w, w):
        v = len(T.V)
        T.remove(prev, curr)
        T.add_edge(v, prev, x - prev_w)
        T.add_edge(v, curr, w - x)
        return v

    if n == 2:
        T = Tree(n_in)
        T.add_edge(0, 1, D[0][1])
        return T

    limbLength = limb(D, n - 1)

    D_bald = D.copy()
    for j in range(n - 1):
        D_bald[n - 1][j] -= limbLength
        D_bald[j][n - 1] -= limbLength

    i, k, node = find_3leaves(D_bald, n - 1)
    x = D_bald[i][n - 1]
    D_Trim = [D_bald[i][:-1] for i in range(n - 1)]

    T = AdditivePhylogeny(D_Trim, n - 1)
    is_found, traversal = T.DFS(i, k)
    found, prev_node, curr_node, prev_w, w = find_V(traversal, x)

    if found:
        v = prev_node
        T.add_edge(node, v, limbLength)
    else:
        v = create_V(prev_node, curr_node, prev_w, w)

    T.add_edge(node, v, limbLength)

    return T


if __name__ == '__main__':
    start = time.time()
    INPUTFILENAME = "rosalind_ba7c.txt"
    OUTPUTFILENAME = "ba7c.txt"
    file = open(INPUTFILENAME, "r")
    n_in = int(file.readline())

    d_array = []
    for line in file:
        mlist = list(map(int, line.split()))
        d_array.append(mlist)
    file.close()
    file = open(OUTPUTFILENAME, "w")
    myTree = AdditivePhylogeny(d_array, n_in)
    sorted(myTree.V)
    for node in myTree.V:
        if node in myTree.E:
            for edge in myTree.E[node]:
                new_line = "{}->{}:{}".format(node, edge[0], int(edge[1]))
                file.write(new_line)
                file.write("\n")
    print("--------")
    print("Runtime: {}".format(time.time() - start))
