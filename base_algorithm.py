
import time
import tracemalloc
from abc import ABC, abstractmethod


class BaseAlgorithm(ABC):

    def __init__(self, name: str):
        self.name = name
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def find_path(self, grid: list, start: tuple, goal: tuple) -> dict:
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.start = start
        self.goal = goal

        self.parents = {}
        self.path = []
        self.cost = float('inf')

        start_time = time.perf_counter()
        tracemalloc.start()

        try:
            self._run_algorithm()
        finally:
            end_time = time.perf_counter()
            current_mem, peak_mem = tracemalloc.get_traced_memory()
            tracemalloc.stop()

        self.time_ms = (end_time - start_time) * 1000
        self.memory_mb = peak_mem / (1024 * 1024)

        self._reconstruct_path()

        return self._make_result()

    @abstractmethod
    def _run_algorithm(self):
        pass

    def _reconstruct_path(self):
        start = self.start
        goal = self.goal
        parents = self.parents

        if goal not in parents and start != goal:
            self.path = []
            return

        current = goal
        path = []
        while current != start:
            path.append(current)
            current = parents[current]
        path.append(start)
        path.reverse()
        self.path = path

    def _make_result(self) -> dict:
        return {
            'algorithm': self.name,
            'path': self.path,
            'visited': self.visited,
            'cost': self.cost,
            'time_ms': self.time_ms,
            'memory_mb': self.memory_mb,
            'visited_count': len(self.visited),
            'path_length': len(self.path)
        }

    def _is_walkable(self, x: int, y: int) -> bool:
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        return self.grid[y][x] != 0

    def _get_neighbors(self, x: int, y: int):
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if self._is_walkable(nx, ny):
                yield nx, ny