from puzzles import EightPuzzle
from algorithms import Solver
from utils.performance import compare_algorithms

def user_interface():
    print("Welcome to the Puzzle Solver!")
    initial_state_input = input("Enter the 8-puzzle initial state (e.g., 1 2 3 4 5 6 7 0 8): ")
    if " " in initial_state_input:
        initial_state = list(map(int, initial_state_input.split()))
    else:
        initial_state = list(map(int, initial_state_input))
        
        
    # Ensure exactly 9 numbers are provided
    if len(initial_state) != 9:
        print("Error: Please enter exactly 9 numbers for the 8-puzzle.")
        return    

    print("Select an algorithm:")
    print("1. A* Search")
    print("2. Greedy Best-First Search")
    algorithm_choice = int(input("Enter choice: "))
    
    if algorithm_choice == 1:
        algorithm = 'A*'
    elif algorithm_choice == 2:
        algorithm = 'Greedy'

    print("Select a heuristic:")
    print("1. Manhattan Distance")
    print("2. Misplaced Tiles")
    heuristic_choice = int(input("Enter choice: "))
    
    heuristic = 'manhattan' if heuristic_choice == 1 else 'misplaced'

    puzzle = EightPuzzle(initial_state)
    solver = Solver(puzzle, algorithm, heuristic)
    
    goal_state, path = solver.solve()
    print(f"Goal state reached: {goal_state}")
    print(f"Solution path: {path}")

    # Performance comparison
    compare_algorithms(puzzle)
