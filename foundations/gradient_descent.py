class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        
        D = lambda x: 2 * x

        i = 0
        res = init
        while i < iterations:
            res = res - learning_rate * D(res)
            i += 1
        
        return round(res, 5)
