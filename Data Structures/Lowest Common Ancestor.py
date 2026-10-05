class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    if left:
        return left

    return right


root = Node(3)
root.left = Node(5)
root.right = Node(1)

root.left.left = Node(6)
root.left.right = Node(2)

p = root.left
q = root.right

answer = lowest_common_ancestor(root, p, q)

print(answer.data)
