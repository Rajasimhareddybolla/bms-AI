def dls(tree, node, goal, depth):
    if depth == 0:
        return node == goal
    if depth > 0:
        for child in tree.get(node, []):
            if dls(tree, child, goal, depth - 1):
                return True
    return False

def iddfs(tree, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth: {depth}")
        if dls(tree, start, goal, depth):
            print(f"Found goal '{goal}' at depth {depth}")
            return True
    print(f"Goal '{goal}' not found within depth {max_depth}")
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
