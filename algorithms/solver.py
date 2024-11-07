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
        
    def astar(self):
        frontier = []
        initial_state = self.puzzle.initial_state
        heapq.heappush(frontier, (self.puzzle.heuristic(initial_state, self.heuristic), 0, initial_state))   
        explored = set()
        parent_map = {tuple(initial_state):None}
        
        while frontier:
            f_cost, g_cost, current_state = heapq.heappop(frontier)
            if self.puzzle.goal_test(current_state):
                return current_state, self.reconstruct_path(parent_map, current_state)
            
            explored.add(tuple(current_state))
            
            for neighbor in self.puzzle.get_neighbors(current_state):
                if tuple(neighbor) not in explored:
                    total_cost = g_cost + 1
                    heapq.heappush(frontier, (total_cost + self.puzzle.heuristic(neighbor,self.heuristic), total_cost, neighbor))
                    parent_map[tuple(neighbor)] = tuple(current_state)
                    
        return None, []
    
    def greedy(self):
        frontier = []
        initial_state = self.puzzle.initial_state
        heapq.heappush(frontier, (self.puzzle.heuristic(initial_state, self.heuristic), initial_state))  # (heuristic_cost, state)
        explored = set()
        parent_map = {tuple(initial_state): None}  # To keep track of parent states

        while frontier:
            _, current_state = heapq.heappop(frontier)
            if self.puzzle.goal_test(current_state):
                return current_state, self.reconstruct_path(parent_map, current_state)

            explored.add(tuple(current_state))
            
            for neighbor in self.puzzle.get_neighbors(current_state):
                if tuple(neighbor) not in explored:
                    heapq.heappush(frontier, (self.puzzle.heuristic(neighbor, self.heuristic), neighbor))
                    parent_map[tuple(neighbor)] = tuple(current_state)

        return None, []
    
    def reconstruct_path(self, parent_map, current_state):
        path = []
        while current_state:
            path.append(current_state)
            current_state = parent_map[tuple(current_state)]
        return path[::-1]