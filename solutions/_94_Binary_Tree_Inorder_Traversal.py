from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


def create_binary_tree(data, idx=0):
    node = None
    if idx < len(data):
        if not data[idx]:
            return
        node = TreeNode(data[idx])
        node.left = create_binary_tree(data, idx + 1)
        node.right = create_binary_tree(data, idx + 2)
    return node


if __name__ == '__main__':
    tree = [1, None, 2, 3]
    root = create_binary_tree(tree)
    ans = [1, 3, 2]
    assert ans == Solution().inorderTraversal(root)

    tree = []
    root = create_binary_tree(tree)
    ans = []
    assert ans == Solution().inorderTraversal(root)

    tree = [1]
    root = create_binary_tree(tree)
    ans = [1]
    assert ans == Solution().inorderTraversal(root)

