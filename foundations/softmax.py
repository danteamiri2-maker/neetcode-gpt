import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        act = lambda x: np.exp(x - np.max(x)) / sum(np.exp(x - np.max(x)))
        return np.round(act(z), 4)
