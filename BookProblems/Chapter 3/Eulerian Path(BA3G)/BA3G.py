class Node:
    def __init__(self, value):
        self.inDegree = 0
        self.outDegree = 0
        self.val = value


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = {}

    def add_node(self, value):
        node = Node(value)
        self.graph[node] = []
        return node

    def add_edge(self, source: Node, destination: Node):
        self.graph[source].append(destination)
        destination.inDegree += 1
        source.outDegree += 1

    def get_outDegree(self, source: Node):
        source.outDegree = len(self.graph[source])
        return len(self.graph[source])

    def remove_edge(self, source: Node, destination: Node):
        self.graph[source].remove(destination)
        destination.inDegree -= 1
        source.inDegree -= 1

    def print_graph(self):
        for key in self.graph:
            if len(self.graph.get(key)) == 0:
                continue
            print(key.val, end=" -> ")
            for val_index in range(len(self.graph.get(key))):
                if val_index == 0:
                    print(self.graph.get(key)[val_index].val, end="")
                else:
                    print(",", self.graph.get(key)[val_index].val, end="")
            print(',,,,',key.inDegree)
            print()

    def eulerian_path(self):

        for key in self.graph:
            if key.inDegree - key.outDegree == 1:
                sink = key
            elif key.outDegree - key.inDegree == 1:
                source = key
        self.add_edge(sink, source)
        curr = []
        circuit = []
        curr.append(source)
        current_node = source
        while len(curr):
            if current_node.outDegree > 0:
                curr.append(current_node)
                next_node = self.graph[current_node][current_node.outDegree - 1]
                current_node.outDegree -= 1
                current_node = next_node
            else:
                circuit.append(current_node)
                current_node = curr[-1]
                curr.pop()

        for i in range(0, len(circuit)):
            if circuit[i] == source:
                index = i
                continue

        self.remove_edge(sink, source)
        for i in range(index, index - len(circuit) + 1, -1):
            print(circuit[i].val, end="")
            if i != index - len(circuit) + 2:
                print("->", end="")




if __name__ == '__main__':
    lines = []
    while True:
        try:
            x = input()
            lines.append(x)
        except:
            break
    y = -1
    for line in lines:
        x = line.split()
        if y < int(x[0]):
            y = int(x[0])
    # Used y to find number of vertices
    graph = Graph(y+1)
    nodes = [Node] * (y + 1)

    for i in range(0, y+1):
        node = graph.add_node(i)
        nodes[i] = node

    for line in lines:
        parts = line.split()
        destinations = parts[2].split(",")
        for dest in destinations:
            graph.add_edge(nodes[int((parts[0]))], nodes[int(dest)])

    graph.eulerian_path()
