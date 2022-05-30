
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
