def dls(tree, node, goal, depth, path):
    path.append(node)  # Add current node to trace
    if depth == 0:
        return node == goal
    if depth > 0:
        for child in tree.get(node, []):
            if dls(tree, child, goal, depth - 1, path):
                return True
    path.pop()  # Backtrack if not found
    return False

def iddfs(tree, start, goal, max_depth):
    for depth in range(max_depth + 1):
        path = []
        print(f"\n🔍 Searching at depth {depth}")
        if dls(tree, start, goal, depth, path):
            print(f"✅ Found goal '{goal}' at depth {depth}")
            print(f"📌 Trace: {' → '.join(path)}")
            return True
        else:
            print(f"📌 Trace at depth {depth}: {' → '.join(path)}")
    print(f"\n❌ Goal '{goal}' not found within depth {max_depth}")
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
