# Definition for a binary tree node.
from typing import Optional

import pytest


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


def to_binary_tree(items: list[int]) -> TreeNode:
    """Создает двоичное дерево из списка значений узлов."""
    n = len(items)
    if n == 0:
        return None

    def get_tree(idx: int = 0) -> TreeNode:
        """Рекурсивная функция для формирования двоичного дерева"""
        if n <= idx or items[idx] is None:
            return None

        node = TreeNode(items[idx])
        node.left = get_tree(2 * idx + 1)
        node.right = get_tree(2 * idx + 2)
        return node

    return get_tree()

class TestCase:
    def test1(self):
        root = [4, 2, 6, 1, 3]
        tree = to_binary_tree(root)
        ans = 1
        assert Solution().getMinimumDifference(tree) == ans

    def test2(self):
        root = [1, 0, 48, None, None, 12, 49]
        tree = to_binary_tree(root)
        ans = 1
        assert Solution().getMinimumDifference(tree) == ans

if __name__ == '__main__':
    pytest.main()
