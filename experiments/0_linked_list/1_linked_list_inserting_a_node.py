class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if(prev_node is None):
            print("There must be previous node  to insert data after it.")
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
            return
        tail = self.head
        while(tail.next):
            tail = tail.next
        tail.next = new_node

    def print_list(self):
        node = self.head
        while(node):
            print("Node => ", node.data)
            node = node.next


llist = LinkedList()

first = Node(1)
second = Node(2)
third = Node(3)

llist.head = first
first.next = second
second.next = third

print("====================================================")
llist.print_list()  # 1st Result

print("====================================================")
llist.push(0)
llist.print_list()  # 2nd Result

print("====================================================")
llist.insert_after(llist.head.next, 100)
llist.print_list()  # 3rd Result

print("====================================================")
llist.append(200)
llist.print_list()  # 4th Result

# OUTPUT
# ====================================================
# Node =>  1
# Node =>  2
# Node =>  3
# ====================================================
# Node =>  0
# Node =>  1
# Node =>  2
# Node =>  3
# ====================================================
# Node =>  0
# Node =>  1
# Node =>  100
# Node =>  2
# Node =>  3
# ====================================================
# Node =>  0
# Node =>  1
# Node =>  100
# Node =>  2
# Node =>  3
# Node =>  200
