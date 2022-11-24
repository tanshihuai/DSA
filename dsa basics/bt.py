class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.left.left.left = Node(9)
n1.left.left.right = Node(10)
n1.right.left = Node(6)
n1.right.right = Node(7)

class queue:
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        return self.data.pop(0)

def preorder(root):
    if not root:
        return
    else:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if not root:
        return
    else:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def postorder(root):
    if not root:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def levelorder(root):
    q = queue()
    q.enqueue(root)
    while len(q.data) != 0:
        current = q.dequeue()
        print(current.data)
        if current.left:
            q.enqueue(current.left)
        if current.right:
            q.enqueue(current.right)


def searchbt(root, data):
    q = queue()
    q.enqueue(root)
    while len(q.data) != 0:
        current = q.dequeue()
        if current.data == data:
            return True
        else:
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
    return False


def addtobt(root, data):
    q = queue()
    q.enqueue(root)
    while len(q.data) != 0:
        current = q.dequeue()
        if not current.left:
            current.left = Node(data)
            return
        elif not current.right:
            current.right = Node(data)
            return
        else:
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)

def getdeepest(root):
    q = queue()
    q.enqueue(root)
    while len(q.data) != 0:
        current = q.dequeue()
        if current.left:
            q.enqueue(current.left)
        if current.right:
            q.enqueue(current.right)
    return current


def deletedeepest(root, node):
    if not root:
        return
    else:
        if root.data == node:
            root.data = None
            return
        else:
            q = queue()
            q.enqueue(root)
            while len(q.data) != 0:
                current = q.dequeue()
                if current.left:
                    if current.left.data == node:
                        print(f"{current.left.data} is deleted")
                        current.left = None
                        return
                    else:
                        q.enqueue(current.left)
                if current.right:
                    if current.right.data == node:
                        print(f"{current.right.data} is deleted")
                        current.right = None
                        return
                    else:
                        q.enqueue(current.right)

def delete(root, node):
    deepest = getdeepest(root)
    print(f"deepest is {deepest.data}")
    deletedeepest(root, deepest.data)
    q = queue()
    q.enqueue(root)
    while len(q.data) != 0:
        current = q.dequeue()
        if current.data == node:
            current.data = deepest.data
            return
        else:
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)



delete(n1, 3)
levelorder(n1)
