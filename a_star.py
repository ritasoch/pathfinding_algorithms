
import heapq
import math
from base_algorithm import BaseAlgorithm


class AStar(BaseAlgorithm):

    def __init__(self):
        super().__init__("A*")

    def _heuristic(self, a: tuple, b: tuple) -> float:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def _run_algorithm(self):
        grid = self.grid
        start = self.start
        goal = self.goal
        height = self.height
        width = self.width

        g_score = [[math.inf] * width for _ in range(height)]
        g_score[start[1]][start[0]] = 0

        f_score = [[math.inf] * width for _ in range(height)]
        f_score[start[1]][start[0]] = self._heuristic(start, goal)

        pq = [(f_score[start[1]][start[0]], start[0], start[1])]

        visited = set()
        parents = {}

        while pq:
            current_f, x, y = heapq.heappop(pq)
            current = (x, y)

            if current in visited:
                continue

            if current_f != f_score[y][x]:
                continue

            visited.add(current)

            if current == goal:
                break

            for nx, ny in self._get_neighbors(x, y):
                neighbor = (nx, ny)
                weight = grid[ny][nx]
                tentative_g = g_score[y][x] + weight

                if tentative_g < g_score[ny][nx]:
                    g_score[ny][nx] = tentative_g
                    f_score[ny][nx] = tentative_g + self._heuristic(neighbor, goal)
                    parents[neighbor] = current
                    heapq.heappush(pq, (f_score[ny][nx], nx, ny))

        self.parents = parents
        self.cost = g_score[goal[1]][goal[0]] if goal in visited else float('inf')
        self.visited = visited 