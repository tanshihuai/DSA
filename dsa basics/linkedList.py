class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


headNode = Node(5)
newNode1 = Node(6)
newNode2 = Node(7)
newNode3 = Node(8)
newNode4 = Node(9)
newNode5 = Node(10)

headNode.next = newNode1
newNode1.next = newNode2
newNode2.next = newNode3
newNode3.next = newNode4
newNode4.next = newNode5


def find(head, to_find):
    if head == None:
        return False
    else:
        if head.value == to_find:
            return True
        else:
            return find(head.next, to_find)




print(find(headNode, 710))


'''

def find(None, to_find): -> False
def find(head.value == to_find, to_find): -> True
def find(head.value != to_find, to_find): -> def find(head.next, to_find)



'''