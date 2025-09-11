def dls(tree, node, goal, depth, path):
    print(f"Visiting node: {node}, Depth left: {depth}")
    path.append(node)

    if depth == 0:
        if node == goal:
            print(f"Found goal at node: {node}")
            return True
        else:
            path.pop()
            return False

    for child in tree.get(node, []):
        if dls(tree, child, goal, depth - 1, path):
            return True

    path.pop()
    return False

def iddfs(tree, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\Starting depth-limited search at depth {depth}")
        path = []
        if dls(tree, start, goal, depth, path):
            print(f"\ Goal '{goal}' found at depth {depth}")
            print(f" Path: {' → '.join(path)}")
            return True
        else:
            print(f" Goal not found at depth {depth}")
    print(f"\Goal '{goal}' not found within depth {max_depth}")
    return False

# Example usage
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'D': ['H'],
    'E': ['I'],
}

iddfs(tree, 'A', 'G', 3)
