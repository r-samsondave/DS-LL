class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            return None

        if self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp


        turtle = self.head
        hair = None

        while turtle.next is not None:
            hair = turtle
            turtle = turtle.next

        self.tail = hair
        hair.next = None
        self.length -= 1

        return turtle

    def pop_first(self):
        if self.head is None:
            return None

        if self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1

        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next


        return temp

    def insert(self, index, value):
        new_node = Node(value)

        if index < 0 or index >= self.length:
            return

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        temp = self.head
        pre = None


        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        else:
            for _ in range(index):
                pre = temp
                temp = temp.next

            pre.next = new_node
            new_node.next = temp
            self.length += 1

        return






# Nodes

# LinkedList
ll = LinkedList()

# Chain

neww = ll.get(1)




current = ll.head

while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")

