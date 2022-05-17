class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


newBT = TreeNode(5)
newNode3 = TreeNode(3)
newNode6 = TreeNode(6)
newNode2 = TreeNode(2)
newNode4 = TreeNode(4)
newNode8 = TreeNode(8)
newNode1 = TreeNode(1)
newNode7 = TreeNode(7)

newBT.left = newNode3
newBT.right = newNode6
newNode3.left = newNode2
newNode3.right = newNode4
newNode2.left = newNode1
newNode6.right = newNode8
newNode8.left = newNode7


class queue():
    # for level order traversal
    def __init__(self):
        self.list = []


    def enqueue(self, value):
        self.list.append(value)


    def dequeue(self):
        return self.list.pop(0)


    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False


def preOrderTraversal(root):
    if not root:
        return
    print(root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print(root.data)
    inOrderTraversal(root.right)


def postOrderTraversal(root):
    if not root:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data)


def levelOrderTraversal(root):
    q = queue()
    q.enqueue(root)
    while not q.isEmpty():
        node = q.dequeue()
        print(node.data)
        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)


def lltolist(root):
    ans = []
    level = [root]
    while root and level:
        next_level = []
        current_level_value = []
        for i in level:
            current_level_value.append(i.data)
            if i.left:
                next_level.append(i.left)
            if i.right:
                next_level.append(i.right)
        ans.extend([current_level_value])
        level = next_level
    return ans





def validate_tree(root):
    if root.left:
        if root.left.data > root.data:
            return False
        return validate_tree(root.left)
    if root.right:
        if root.right.data < root.data:
            return False
        return validate_tree(root.right)
    return True

print(validate_tree(newBT))










