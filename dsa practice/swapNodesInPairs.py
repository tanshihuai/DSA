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
            second.next = head
            head.next = self.swapPairs(third)
            return second


def traverse(head):
    while head:
        print(head.val)
        head = head.next




def mergeSort(arr):

    def merge(arr1, arr2):
        answer = []
        i = j = 0
        while i != len(arr1) and j != len(arr2):
            if arr1[i] > arr1[j]:
                answer.append(arr1[j])
                j += 1
            else:
                answer.append(arr2[i])
                i += 1
        answer.extend(arr1[i:])
        answer.extend(arr1[j:])
        return answer

    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        l = mergeSort(arr[:mid])
        r = mergeSort(arr[mid:])
        return merge(l, r)

input = [1,5,7,2,1,6,3,1,7,115,62,54]

print(mergeSort(input))


