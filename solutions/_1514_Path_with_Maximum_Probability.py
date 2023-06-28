from collections import defaultdict, deque
from typing import List

import pytest


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]],
                       succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        queue = deque([start])
        while queue:
            cur_node = queue.popleft()
            for next_node, path_prob in graph[cur_node]:
                if  max_prob[next_node] < max_prob[cur_node] * path_prob:
                    max_prob[next_node] = max_prob[cur_node] * path_prob
                    queue.append(next_node)
        return max_prob[end]


class TestCase:
    def test1(self):
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.2]
        start = 0
        end = 2
        ans = 0.25000
        assert ans == Solution().maxProbability(n, edges, succProb, start, end)

    def test2(self):
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.3]
        start = 0
        end = 2
        ans = 0.30000
        assert ans == Solution().maxProbability(n, edges, succProb, start, end)

    def test3(self):
        n = 3
        edges = [[0, 1]]
        succProb = [0.5]
        start = 0
        end = 2
        ans = 0.00000
        assert ans == Solution().maxProbability(n, edges, succProb, start, end)

if __name__ == '__main__':
    pytest.main()

