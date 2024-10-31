import time
from algorithms import Solver

def compare_algorithms(puzzle):
    for algorithm in ['A*', 'Greedy']:
        start_time = time.time()
        solver = Solver(puzzle, algorithm, heuristic='manhattan')
        _, _ = solver.solve()
        end_time = time.time()
        print(f"{algorithm} took {end_time - start_time:.4f} seconds.")
