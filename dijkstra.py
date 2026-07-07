
import heapq
import math
from base_algorithm import BaseAlgorithm


class Dijkstra(BaseAlgorithm):

    def __init__(self):
        super().__init__("Dijkstra")

    def _run_algorithm(self):
        grid = self.grid
        start = self.start
        goal = self.goal
        height = self.height
        width = self.width

        dist = [[math.inf] * width for _ in range(height)]
        dist[start[1]][start[0]] = 0

        pq = [(0, start[0], start[1])]

        visited = set()
        parents = {}

        while pq:
            current_dist, x, y = heapq.heappop(pq)
            current = (x, y)

            if current in visited:
                continue

            if current_dist != dist[y][x]:
                continue

            visited.add(current)

            if current == goal:
                break

            for nx, ny in self._get_neighbors(x, y):
                if (nx, ny) in visited:
                    continue

                weight = grid[ny][nx]
                new_dist = current_dist + weight

                if new_dist < dist[ny][nx]:
                    dist[ny][nx] = new_dist
                    parents[(nx, ny)] = current
                    heapq.heappush(pq, (new_dist, nx, ny))

        self.parents = parents
        self.cost = dist[goal[1]][goal[0]] if goal in visited else float('inf')
        self.visited = visited 
