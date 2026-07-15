
from collections import deque
from base_algorithm import BaseAlgorithm


class BFS(BaseAlgorithm):

    def __init__(self):
        super().__init__("BFS")

    def _run_algorithm(self):
        grid = self.grid
        start = self.start
        goal = self.goal

        queue = deque([start])
        parents = {}
        visited = set([start])

        while queue:
            x, y = queue.popleft()
            current = (x, y)

            if current == goal:
                break

            for nx, ny in self._get_neighbors(x, y):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parents[(nx, ny)] = current
                    queue.append((nx, ny))

        self.parents = parents
        self.visited = visited

    def _calculate_cost(self) -> float:
        if not self.path:
            return float('inf')

        cost = 0
        for x, y in self.path:
            if (x, y) != self.path[0]:
                cost += self.grid[y][x]

        return cost