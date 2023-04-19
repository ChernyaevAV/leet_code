# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.pathLength = 0

        def dfs(node, goLeft, steps):
            if node:
                self.pathLength = max(self.pathLength, steps)
                if goLeft:
                    dfs(node.left, False, steps + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)
        dfs(root, False, 0)
        dfs(root, True, 0)
        return self.pathLength


if __name__ == '__main__':
    root = [1, None, 1, 1, 1, None, None, 1, 1, None, None, 1]
    node0 = TreeNode(1, None, None)
    node1 = TreeNode(1, None, node0)
    node2 = TreeNode(1, None, node1)
    node3 = TreeNode(1, None, None)
    node4 = TreeNode(1, node2, node3)
    node5 = TreeNode(1, None, None)
    node6 = TreeNode(1, node5, node4)
    node7 = TreeNode(1, None, node6)

    tree = Solution()
    print(tree.longestZigZag(node7)) # 3

