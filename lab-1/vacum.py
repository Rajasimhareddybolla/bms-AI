if True:
    import numpy as np

    class VacuumCleanerAgent:
        def __init__(self, grid, garbage_positions, start_pos):
            self.grid = grid
            self.garbage_positions = set(garbage_positions)
            self.pos = start_pos
            self.cleaned = []

        def get_next_target(self):
            current_val = self.grid[self.pos]
            min_diff = float('inf')
            target = None

            for gp in self.garbage_positions:
                if gp not in self.cleaned:
                    diff = abs(current_val - self.grid[gp])
                    if diff < min_diff:
                        min_diff = diff
                        target = gp
            return target

        def move_to(self, target):
            print(f"Moving from {self.pos} to {target}")
            self.pos = target

        def clean(self):
            print(f"Cleaning cell {self.pos} with garbage {self.grid[self.pos]}")
            self.grid[self.pos] = 0
            self.cleaned.append(self.pos)

        def run(self):
            while True:
                target = self.get_next_target()
                if not target:
                    print("All garbage cleaned!")
                    break
                self.move_to(target)
                self.clean()

    # Example setup
    n, m = 5, 5
    grid = np.random.randint(1, 10, size=(n, m))
    garbage_positions = [(0, 1), (2, 3), (4, 4), (1, 2)]
    start_pos = (0, 0)

    agent = VacuumCleanerAgent(grid, garbage_positions, start_pos)
    print("Initial Grid:\n", grid)
    agent.run()
    print("Final Grid:\n", grid)
