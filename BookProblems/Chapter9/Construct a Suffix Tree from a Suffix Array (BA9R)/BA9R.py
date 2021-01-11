class Node(object):
    def __init__(self, data=None, depth=None, parent=None):
        self.parent = parent
        self.data = data
        self.depth = depth
        self.children = []

    def add_child(self, obj):
        self.add_child(obj)


class Tree(object):
    nodes = []

    def __init__(self):
        self.root = self.createRoot()

    def createRoot(self):
        return Node(data="", depth=0)

    def appendNode(self, parent: Node, child: Node):
        parent.children.append(child)
        self.nodes.append(child)

    def deleteNode(self, wanted: Node):
        self.nodes.remove(wanted)


def construct_suffixTree_from_suffixArray(text, suffixArray, LCP):
    tree = Tree()
    ans = []
    flag = True
    for i in range(len(text)):
        if LCP[i] == 0:
            node = Node(data=text[suffixArray[i]:], depth=len(text[suffixArray[i]:]), parent=tree.root)
            tree.appendNode(parent=tree.root, child=node)
            current_node = node
        else:
            while True:
                p = current_node.parent
                if p.depth < LCP[i]:
                    flag = True
                    prev = current_node
                    current_node = p
                    break
                elif p.depth == LCP[i]:
                    flag = False
                    prev = current_node
                    current_node = p
                    break
                else:
                    prev = current_node
                    current_node = p

            if flag:
                newnode = Node(data=prev.data[0:LCP[i] - current_node.depth],
                               depth=len(prev.data[0:LCP[i] - current_node.depth]) + current_node.depth,
                               parent=current_node
                               )
                tree.deleteNode(prev)
                tree.appendNode(parent=current_node, child=newnode)
                changed_node = Node(data=prev.data[LCP[i] - current_node.depth:],
                                    depth=len(prev.data[LCP[i] - current_node.depth:]) + newnode.depth,
                                    parent=newnode
                                    )
                tree.appendNode(parent=newnode, child=changed_node)
                added_node = Node(data=text[suffixArray[i] + LCP[i]:],
                                  depth=len(text[suffixArray[i] + LCP[i]:]) + newnode.depth,
                                  parent=newnode
                                  )
                tree.appendNode(parent=newnode, child=added_node)
                current_node = added_node
            else:
                added_node = Node(data=text[suffixArray[i] + LCP[i]:],
                                  depth=len(text[suffixArray[i] + LCP[i]:]) + current_node.depth,
                                  parent=current_node
                                  )
                tree.appendNode(parent=current_node, child=added_node)
                current_node = added_node
    return tree


if __name__ == '__main__':
    INPUT_FILE_NAME = 'rosalind_ba9r.txt'
    OUTPUT_FILE_NAME = 'ba9r.txt'
    file = open(INPUT_FILE_NAME, 'r')
    text = str(file.readline().replace("\n", ""))
    suffixArray = list(map(int, file.readline().split(", ")))
    LCP = list(map(int, file.readline().split(", ")))
    file.close()
    print(len(text))
    ans = construct_suffixTree_from_suffixArray(text, suffixArray, LCP)
    file = open(OUTPUT_FILE_NAME, 'w')
    for i in ans.nodes:
        file.write(i.data + "\n")
