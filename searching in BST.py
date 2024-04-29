class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def constructBST(nums):
    root = None
    for num in nums:
        root = insertNode(root, num)
    return root

def insertNode(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insertNode(root.left, value)
    elif value > root.value:
        root.right = insertNode(root.right, value)
    return root

def searchBST(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    elif target < root.value:
        return searchBST(root.left, target)
    else:
        return searchBST(root.right, target)

n = int(input())
nums = list(map(int, input().split()))
target = int(input())
root = constructBST(nums)
if searchBST(root, target):
    print("Target element is found")
else:
    print("Target element is not found")
