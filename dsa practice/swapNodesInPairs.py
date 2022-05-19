class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


headNode = Node(1)
newNode1 = Node(2)
newNode2 = Node(3)
newNode3 = Node(4)
newNode4 = Node(5)
newNode5 = Node(6)

headNode.next = newNode1
newNode1.next = newNode2
newNode2.next = newNode3
newNode3.next = newNode4
newNode4.next = newNode5


class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        else:
            second = head.next
            third = head.next.next
            head.val, second.val = second.val, head.val
            second.next = self.swapPairs(third)
            return head


def traverse(head):
    while head:
        print(head.val)
        head = head.next


s = Solution()
traverse(s.swapPairs(headNode))