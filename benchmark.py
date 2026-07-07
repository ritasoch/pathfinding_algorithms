
def run_test(scenario, algorithm, runs: int = 5):

    grid = scenario.generate()

    start = (8, 8)
    goal = (18, 18)

    if grid[start[1]][start[0]] == 0 or grid[goal[1]][goal[0]] == 0:
        print("SKIP: start or goal is a wall")
        return None

    results = []
    for _ in range(runs):
        result = algorithm.find_path(grid, start, goal)
        results.append(result)

    avg = {
        'scenario': scenario.get_name(),
        'algorithm': algorithm.name,
        'width': scenario.width,
        'height': scenario.height,
        'runs': runs,
    }

    numeric_keys = ['time_ms', 'memory_mb', 'visited_count', 'path_length', 'cost']
    for key in numeric_keys:
        values = [r[key] for r in results if r[key] != float('inf')]
        avg[key] = sum(values) / len(values) if values else float('inf')

    for r in results:
        if r['path']:
            avg['path'] = r['path']
            break
    else:
        avg['path'] = []

    return avg


def print_summary(results):

    if not results:
        print("No results")
        return

    print("\n" + "=" * 110)
    print("SUMMARY TABLE")
    print("=" * 110)

    header = (f"{'Scenario':<20} {'Algorithm':<12} {'Size':<10} "
              f"{'Time (ms)':<12} {'Memory (MB)':<12} {'Visited':<10} {'Length':<8} {'Cost':<10}")
    print(header)
    print("-" * 110)

    for row in results:
        scenario = row['scenario'][:18]
        algorithm = row['algorithm'][:10]
        size = f"{row['width']}x{row['height']}"
        time = f"{row['time_ms']:.2f}" if row['time_ms'] != float('inf') else "inf"
        memory = f"{row['memory_mb']:.4f}" if row['memory_mb'] != float('inf') else "inf"
        visited = row['visited_count']
        length = row['path_length']
        cost = f"{row['cost']:.1f}" if row['cost'] != float('inf') else "inf"

        print(f"{scenario:<20} {algorithm:<12} {size:<10} "
              f"{time:<12} {memory:<12} {visited:<10} {length:<8} {cost:<10}")
    print("=" * 110)