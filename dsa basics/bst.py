class bstnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class queue:
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        return self.data.pop(0)

    def notempty(self):
        if len(self.data) != 0:
            return True
        return False


def insert(root, value):
    if root.data > value:
        if root.left:
            insert(root.left, value)
        else:
            root.left = bstnode(value)
            return
    elif root.data <= value:
        if root.right:
            insert(root.right, value)
        else:
            root.right = bstnode(value)
            return


def smallestnode(root):
    q = queue()
    q.enqueue(root)
    while q.notempty():
        current = q.dequeue()
        if current.left:
            q.enqueue(current.left)
    return current



def delete(root, value):
    if not root:
        return None
    else:
        if root.data < value:
            root.right = delete(root.right, value)
        elif root.data > value:
            root.left = delete(root.left, value)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                temp = smallestnode(root.right)                     # get smallest node of right subtree
                root.data = temp.data                               # set root value = smallest value
                root.right = delete(root.right, temp.data)          # delete smallest node recursively
                return root                                         # return root so previous stack call's root.left or root.right has something to point to




def height(root):
    if not root:
        return -1
    else:
        left = height(root.left) + 1
        right = height(root.right) + 1
        return max(left, right)



n1 = bstnode(5)
insert(n1, 4)
insert(n1, 6)
insert(n1, 3)

n1.display()

print("###################")
