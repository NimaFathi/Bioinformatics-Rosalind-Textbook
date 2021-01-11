class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = {}

    def add_node(self, node):
        self.graph[node] = []

    def add_edge(self, source, destination):
        self.graph[source].append(destination)

    def print_graph(self):
        for key in self.graph:
            if len(self.graph.get(key)) == 0:
                continue
            print(key, end=" -> ")
            for val_index in range(len(self.graph.get(key))):
                if val_index == 0:
                    print(self.graph.get(key)[val_index], end="")
                else:
                    print(",", self.graph.get(key)[val_index], end="")
            print()


def suffix(node):
    return node[1:]


def prefix(node):
    return node[0:len(node) - 1]


def match_with(graph, node1, node2):
    if prefix(node1) == suffix(node2):
        graph.add_edge(node2, node1)


if __name__ == '__main__':
    inputs = []
    while True:
        try:
            x = input()
            inputs.append(x)
        except:
            break
    vertices = len(inputs)
    graph = Graph(vertices)

    for i in inputs:
        graph.add_node(i)

    for i in inputs:
        for j in inputs:
            match_with(graph, i, j)
    graph.print_graph()
