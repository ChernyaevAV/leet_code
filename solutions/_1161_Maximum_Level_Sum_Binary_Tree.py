"""Given the root of a binary tree, the level of its root is 1, the
level of its children is 2, and soon.

Return the smallest level x such that the sum of all the values
of nodes at level x is maximal.

Example 1:
Input: root = [1, 7, 0, 7, -8, null, null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989, null, 10250, 98693, -89388, null, null, null, -32127]
Output: 2

Constraints:
The number of nodes in the tree is in the range[1, 10^4].
-10^5 <= Node.val <= 10^5"""
from typing import Optional, Dict

import pytest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # метод обхода в глубину DFS со словарем
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, level: int, sum_at_level: Dict) -> None:
            if not node:
                return
            sum_at_level[level] = sum_at_level.get(level, 0) + node.val
            dfs(node.left, level + 1, sum_at_level)
            dfs(node.right, level + 1, sum_at_level)

        sum_at_level = {}
        dfs(root, 0, sum_at_level)

        return 1 + max(sum_at_level, key=sum_at_level.get)


    # метод обхода в ширину BFS
    # def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    #     max_sum, ans, level = float('-inf'), 0, 0
    #
    #     q = collections.deque()
    #     q.append(root)
    #
    #     while q:
    #         level += 1
    #         sum_at_current_level = 0
    #         for _ in range(len(q)):
    #             node = q.popleft()
    #             sum_at_current_level += node.val
    #
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #         if max_sum < sum_at_current_level:
    #             max_sum, ans = sum_at_current_level, level
    #     return ans


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
        root = [1, 7, 0, 7, -8, None, None]
        tree = to_binary_tree(root)
        ans = 2
        assert Solution().maxLevelSum(tree) == ans

    def test2(self):
        root = [989, None, 10250, 98693, -89388, None, None, None, -32127]
        tree = to_binary_tree(root)
        ans = 2
        assert Solution().maxLevelSum(tree) == ans


if __name__ == '__main__':
    pytest.main()


