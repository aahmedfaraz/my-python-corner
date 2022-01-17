class Node:
    # Function to initialize the Node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        node = self.head
        while(node):
            print("Node => ", node.data)
            node = node.next


# ==============================================================================
# Code Execution Starts Here
# ==============================================================================

llist = LinkedList()

llist.head = Node('ahmed')
second_node = Node('faraz')
third_node = Node('adil')

llist.head.next = second_node
second_node.next = third_node

llist.print_list()
