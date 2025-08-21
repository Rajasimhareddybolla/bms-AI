import numpy as np

class VacuumCleanerAgent:
    def __init__(self, grid, start_pos):
        self.grid = grid  # 2D numpy array of garbage quantities
        self.pos = start_pos  # (row, col)
        self.cleaned = []

    def get_next_target(self):
        current_val = self.grid[self.pos]
        min_diff = float('inf')
        target = None

        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if (i, j) not in self.cleaned and self.grid[i, j] > 0:
                    diff = abs(current_val - self.grid[i, j])
                    if diff < min_diff:
                        min_diff = diff
                        target = (i, j)
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


n, m = 4, 5  
np.random.seed(0)
grid = np.random.randint(0, 10, size=(n, m)) 
start_pos = (0, 0)

agent = VacuumCleanerAgent(grid, start_pos)
print("Initial Grid:\n", grid)
agent.run()
print("Final Grid:\n", grid)
