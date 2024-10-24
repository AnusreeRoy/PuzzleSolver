class EightPuzzle:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        
    def goal_test(self, state):
        return state == self.goal_state
    
    def get_neighbors(self, state):
        neighbors = []
        blank_index = state.index(0)
        row, col = divmod(blank_index, 3)
        moves = {
            'up' : (row - 1, col),
            'down' :(row + 1,col),
            'left' : (row, col-1),
            'right' : (row, col +1)
        }
        for direction, (new_row, new_col) in moves.items():
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_blank_index = new_row * 3 + new_col
                new_state = state[:]
                new_state[blank_index], new_state[new_blank_index]= new_state[new_blank_index], new_state[blank_index]
                neighbors.append(new_state)
        return neighbors
    
    def manhattan_distance(self, state):
        distance = 0
        for i in range(1,9):
            current_index = state.index(i)
            goal_index = self.goal_state.index(i)
            current_row, current_col = divmod(goal_index,3)
            goal_row, goal_col = divmod(goal_index, 3)
            distance += abs(current_row - goal_row) + abs(current_col-goal_col)
        return distance
    
    def misplaced_tiles(self, state):
        return sum (1 for i in range(9)if state[i]!=self.goal_state[i] and state[i]!=0) 
    
    
    def heuristic(self, state, heuristic_type='manhattan'):
        if heuristic_type == 'manhattan':
            return self.manhattan_distance(state)
        elif heuristic_type == 'misplaced':
            return self.misplaced_tiles(state)
        else:
            raise ValueError("Invalid heuristic")