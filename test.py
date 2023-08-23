def solver(U, L, C):
    arr1 = [0] * len(C)
    arr2 = [0] * len(C)
    
    i = 0
    count = 0
    while i < len(C):
        if C[i] == 2:
            arr1[i] = 1
            arr2[i] = 1
            U -= 1
            L -= 1
        elif C[i] == 1:
            count += 1
        i += 1
    
    if U < 0 or L < 0 or count != U + L:
        return "IMPOSSIBLE"

    idx = 0
    while U + L > 0:
        while U > 0 and idx < len(C):
            if C[idx] == 1 and arr1[idx] == 0:
                arr1[idx] = 1
                U -= 1
            idx += 1
        idx = 0
        while L > 0 and idx < len(C):
            if C[idx] == 1 and arr2[idx] == 0:
                arr2[idx] = 1
                L -= 1
            idx += 1
    
    res = ""
    for i in arr1:
        res += str(i)
    res += ","
    for i in arr2:
        res += str(i)

    return res

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def solver(root):
    if root is None:
        return 0
    
    return root.value + solver(root.left) + solver(root.right)

tree = TreeNode(5)
tree.left = TreeNode(3)
tree.right = TreeNode(8)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(4)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)

total_sum = sum_of_elements(tree)
print("Sum :", total_sum)