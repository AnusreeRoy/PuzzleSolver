import heapq

class Solver:
    def __init__(self, puzzle, algorithm, heuristic=None):
        self.puzzle = puzzle
        self.algorithm =  algorithm
        self.heuristic = heuristic
        
    def solve(self):
        if self.algorithm == 'A*':
            return self.astar()
        elif self.algorithm == 'Greedy':
            return self.greedy()