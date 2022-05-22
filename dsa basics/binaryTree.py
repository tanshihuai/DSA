class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


newBT = TreeNode(1)
newNode2 = TreeNode(2)
newNode5 = TreeNode(5)
newNode3 = TreeNode(3)
newNode4 = TreeNode(4)
newNode6 = TreeNode(6)

newBT.left = newNode2
newBT.right = newNode5
newNode2.left = newNode3
newNode2.right = newNode4
newNode5.right = newNode6


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


def levelOrder(root):
    ans = []
    levels = [root]
    while root and levels:
        level_values = []
        next_level = []
        for i in levels:
            level_values.append(i.data)
            if i.left:
                next_level.append(i.left)
            if i.right:
                next_level.append(i.right)
        ans.extend([level_values])
        levels = next_level
    return ans


prev = None

def flatten_tree(root):
    global prev

    if root == None:
        return
    else:
        flatten_tree(root.right)
        flatten_tree(root.left)
        root.left = None
        root.right = prev
        prev = root


def reverseTree(root):
    if root == None:
        return
    else:
        reverseTree(root.left)
        reverseTree(root.right)
        root.left, root.right = root.right, root.left
        return root


def maxNum(root):
    if root == None:
        return -999
    else:
        max_left = maxNum(root.left)
        max_right = maxNum(root.right)
        return max(root.data, max_left, max_right)


def maxDepth(root):
    if root == None:
        return 0
    else:
        left_depth = maxDepth(root.left) + 1
        right_depth = maxDepth(root.right) + 1
        return max(left_depth, right_depth)


def insertion(root, value):
    if root == None:
        newNode = TreeNode(value)
        return newNode
    else:
        if value < root:
            root.left = insertion(root.left, value)
        else:
            root.right = insertion(root.right, value)
        return root


def deleteNode(self, root, key):
    if not root:
        return
    if root.val == key:
        if root.left and not root.right:
            return root.left
        elif root.right and not root.left:
            return root.right
        elif root.left and root.right:
            min_node = find_min(root.right)
            root.val = min_node.val
            root.right = deleteNode(root.right, min_node.value)
            return root
        else:
            return None

    else:
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

def find_min(root):
    if root.left == None:
        return root
    else:
        return find_min(root.left)
