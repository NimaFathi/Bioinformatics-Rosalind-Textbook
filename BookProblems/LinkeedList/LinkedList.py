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

    def insert_after(self, target_value, new_node):
        if not self.head:
            raise Exception("linked list is empty")
        for node in self:
            if node.value == target_value:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("node with value '%s' not found ".format(target_value))

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

    def get(self, i):
        counter = 0
        if self.head is None:
            raise Exception("Linked LIst is empty")
        for node in self:
            if counter == i:
                return node
            counter += 1
        if counter < i:
            raise Exception("Linked List doesn't have enough length")


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

if __name__ == '__main__':
    llist = LinkedList()
    node = Node(1)
    llist.insert_end(node)
    for node in llist:
        print(node.value)