
from scenario import EmptyScenario, MazeScenario, ObstaclesScenario, WeightedScenario
from dijkstra import Dijkstra
from a_star import AStar
from bfs import BFS
from benchmark import run_test, print_summary


def render_grid(grid, path, start, goal):

    path_set = set(path)

    print("\nMAP VISUALIZATION")
    print("Legend: S-Start, G-Goal, *-Path, #-Wall, .-Empty\n")

    for y in range(len(grid)):
        row = ""
        for x in range(len(grid[0])):
            if (x, y) == start:
                row += "S "
            elif (x, y) == goal:
                row += "G "
            elif (x, y) in path_set:
                row += "* "
            elif grid[y][x] == 0:
                row += "# " 
            else:
                row += ". "
        print(row)


def main():

    scenarios = [
        EmptyScenario(),
        MazeScenario(),
        ObstaclesScenario(),
        WeightedScenario()
    ]

    algorithms = [
        Dijkstra(),
        AStar(),
        BFS()
    ]

    all_results = []

    for scenario in scenarios:
        for algorithm in algorithms:
            result = run_test(scenario, algorithm, runs=5)
            if result:
                all_results.append(result)

    if all_results:
        print_summary(all_results)

        for result in all_results:
            if result['scenario'] == "Weighted":
                if result['algorithm'] == "BFS":
                    print(f"\n  {result['algorithm']} - {result['scenario']} DETAILED STATISTICS")
                    print(f"  Algorithm:        {result['algorithm']}")
                    print(f"  Scenario:         {result['scenario']}")
                    print(f"  Map size:         {result['width']}x{result['height']}")
                    print(f"  Path length:      {result['path_length']} cells")
                    print(f"  Path cost:        {result['cost']:.1f}")
                    print(f"  Visited cells:    {result['visited_count']}")
                    print(f"  Execution time:   {result['time_ms']:.2f} ms")
                    print(f"  Peak memory:      {result['memory_mb']:.4f} MB")

                    fixed_scenario = WeightedScenario()
                    fixed_scenario.generate()

                    render_grid(
                        grid=fixed_scenario.grid,
                        path=result.get('path', []),
                        start=(8, 8),
                        goal=(18, 18)
                    )
                    break
main()
