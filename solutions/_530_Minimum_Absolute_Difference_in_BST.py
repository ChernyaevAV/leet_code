# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodeValues = []
        def dfs(node):
            if node is None: return
            dfs(node.left)
            nodeValues.append(node.val)
            dfs(node.right)

        dfs(root)

        # nodeValues.sort() # т.к. у нас бинарное дерево, то можно не сортировать
        minDifference = 10**5
        for i in range(1, len(nodeValues)):
            minDifference = min(minDifference, nodeValues[i] - nodeValues[i-1])
        return minDifference


if __name__ == '__main__':
    # root = [4,2,6,1,3]
    node5 = TreeNode(3, None, None)
    node4 = TreeNode(1, None, None)
    node3 = TreeNode(2, node4, node5)
    node2 = TreeNode(6, None, None)
    node1 = TreeNode(4, node3, node2)

    ans = Solution()
    assert ans.getMinimumDifference(node1) == 1

    root = [1, 0, 48, None, None, 12, 49]
    node1 = TreeNode(0, None, None)
    node2 = TreeNode(12, None, None)
    node3 = TreeNode(49, None, None)
    node4 = TreeNode(48, node2, node3)
    node5 = TreeNode(1, node1, node4)


    ans = Solution()
    assert ans.getMinimumDifference(node5) == 1