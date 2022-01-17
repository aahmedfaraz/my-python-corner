class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
            return
        tail = self.head
        while(tail.next):
            tail = tail.next
        tail.next = new_node

    def delete(self, data):
        if(self.head is None):
            print("List is empty")
        prev_node = self.head
        while(prev_node.next is not None and prev_node.next.data is not data):
            prev_node = prev_node.next
        if(prev_node.next is not None):
            prev_node.next = prev_node.next.next
        else:
            print("This ", data, " Node does not exist inside the linked list")

    def print_list(self):
        node = self.head
        while(node):
            print("Node =>", node.data)
            node = node.next


llist = LinkedList()
llist.append('a')
llist.append('b')
llist.append('c')

print("====================================================")
llist.print_list()

print("====================================================")
llist.delete('b')
llist.print_list()

print("====================================================")
llist.append('d')
llist.delete('c')
llist.print_list()

print("====================================================")
llist.delete('d')
llist.print_list()

print("====================================================")
llist.delete('z')
llist.print_list()

# OUTPUT
# ====================================================
# Node => a
# Node => b
# Node => c
# ====================================================
# Node => a
# Node => c
# ====================================================
# Node => a
# Node => d
# ====================================================
# Node => a
# ====================================================
# This  z  Node does not exist inside the linked list
# Node => a
