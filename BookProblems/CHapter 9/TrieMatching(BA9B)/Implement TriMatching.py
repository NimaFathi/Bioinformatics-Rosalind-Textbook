
class Node:
    def __init__(self):
        self.children = [None] * 4
        self.isPattern = False


class Trie:

    def __init__(self):
        self.root = self.createNode()
        self.dictionary = {'A':0, 'T':1, 'C':2 , 'G':3}
    def createNode(self):
        return Node()

    def insert(self, pattern):
        currentNode = self.root
        for ch in pattern:
            index = self.dictionary.get(ch)
            if not currentNode.children[index]:
                currentNode.children[index] = self.createNode()
            currentNode = currentNode.children[index]
        currentNode.isPattern = True

    def search(self, pattern):
        currentNode = self.root
        for ch in pattern:
            index = self.dictionary.get(ch)
            if not currentNode.children[index]:
                return False
            currentNode = currentNode.children[index]
            if currentNode.isPattern:
                return True

        if currentNode.isPattern:
            return True
        return False




if __name__ == '__main__':
    text = input()
    patterns = []
    while True:
        try:
            x = input()
            patterns.append(x)
        except:
            break
    trie_Tree = Trie()
    for pattern in patterns:
        trie_Tree.insert(pattern)
    for i in range(len(text)):
        suffix = text[i:]
        if trie_Tree.search(suffix):
            print(i, end=" ")