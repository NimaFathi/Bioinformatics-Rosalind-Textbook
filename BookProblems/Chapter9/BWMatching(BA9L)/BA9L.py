import time


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            for mnode in nodes:
                node.next = Node(value=mnode)
                node = node.next

    def insert_head(self, node):
        node.next = self.head
        self.head = node

    def insert_end(self, node):
        if not self.head:
            self.head = node
            return
        for this_node in self:
            pass
        this_node.next = node

    def remove_node(self, target_value):
        if not self.head:
            raise Exception("Linked List is empty")
        if self.head.value == target_value:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.value == target_value:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception("Node with value '%s' not found".format(target_value))

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


def firstColumn_generator(forms):
    first_column = ""
    for form in forms:
        first_column += form[0]
    return first_column


def lastToFirst(LinkedArray, bwt):
    lastFirst = []
    A_node = LinkedArray[0].head
    C_node = LinkedArray[1].head
    G_node = LinkedArray[2].head
    T_node = LinkedArray[3].head
    for i in range(len(bwt)):
        ch = bwt[i]
        if ch == 'A':
            lastFirst.append(A_node.value)
            A_node = A_node.next
        elif ch == 'C':
            lastFirst.append(C_node.value)
            C_node = C_node.next
        elif ch == 'G':
            lastFirst.append(G_node.value)
            G_node = G_node.next
        elif ch == 'T':
            lastFirst.append(T_node.value)
            T_node = T_node.next
        else:
            lastFirst.append(0)
    return lastFirst


def checker(char, bwt, top, bottom):
    container = []
    for i in range(top, bottom + 1):
        if bwt[i] == char:
            container.append(i)
    if not container:
        return -1, -1
    return container[0], container[-1]


def BWMatching(lastColumn, pattern, lastToFirst):
    top = 0
    bottom = len(lastColumn) - 1
    while top <= bottom:
        if pattern:
            ch = pattern[len(pattern) - 1]
            pattern = pattern[:-1]
            returned = checker(ch, lastColumn, top, bottom)
            if (returned[0] > -1):
                topIndex = returned[0]
                bottomIndex = returned[1]
                top = lastToFirst[topIndex]
                bottom = lastToFirst[bottomIndex]
            else:
                return 0
        else:
            return bottom - top + 1


if __name__ == '__main__':
    start = time.time()
    INPUT_FILE_NAME = "rosalind_ba9l.txt"
    input_file = open(INPUT_FILE_NAME, "r")
    bwt = input_file.readline()[:-1]
    bwt_list = list(bwt)
    bwt_list.sort()
    patterns = list(map(str, input_file.readline().split()))
    input_file.close()
    firstColumn = firstColumn_generator(bwt_list)
    A_llist = LinkedList()
    C_llist = LinkedList()
    G_llist = LinkedList()
    T_llist = LinkedList()
    dsign = 0
    for i in range(len(firstColumn) - 1, 0, -1):
        ch = firstColumn[i]
        node = Node(i)
        if ch == 'A':
            A_llist.insert_head(node)
        elif ch == 'C':
            C_llist.insert_head(node)
        elif ch == 'G':
            G_llist.insert_head(node)
        else:
            T_llist.insert_head(node)

    arrayOfLinkedLists = [A_llist, C_llist, G_llist, T_llist]
    A_node = arrayOfLinkedLists[0].head
    A_node = A_node.next
    lastFirst = lastToFirst(arrayOfLinkedLists, bwt)
    file = open("ba9l.txt", "w+")
    for pattern in patterns:
        file.write(str(BWMatching(bwt, pattern, lastFirst, )))
        file.write(' ')
    file.close()
    end = time.time()
    print(end - start)
