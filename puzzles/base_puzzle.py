class Puzzle:
    def __init__(self, initial_state):
        self.state = initial_state
        
    def goal_test(self, state):
        raise NotImplementedError
    
    def get_neighbors(self, state):
        raise NotImplementedError
    
    def heuristic(self, state):
        raise NotImplementedError
    