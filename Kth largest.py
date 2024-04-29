class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def kth_largest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.right
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.left

n = int(input())
elements = list(map(int, input().split()))
k = int(input())

root = None
for element in elements:
    root = insert(root, element)
result = kth_largest(root, k)
print(result)
