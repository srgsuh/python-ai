import numpy as np
import unittest as ut
from game_of_life import game_of_life
from numpy.typing import NDArray

class TestGameOfLife(ut.TestCase):
    def setUp(self)->None:
        self.zeros: NDArray[np.uint8] = np.zeros((3, 3), dtype=np.uint8)
    
    def test_zeroes(self)->None:
        init_data = self.zeros.copy()
        for idx, mx in enumerate(game_of_life(3, 1, 0, init_data)):
            self.assertTrue(np.array_equal(self.zeros, mx))
            if idx == 2:
                break

    def test_one_neighbor(self)->None:
        init_data = np.array([[1,1,0],[0,0,0],[0,0,0]], dtype=np.uint8)
        for idx, mx in enumerate(game_of_life(3, 1, 0, init_data)):
            if idx == 0:
                self.assertTrue(np.array_equal(init_data, mx))
            elif idx == 1:
                self.assertTrue(np.array_equal(self.zeros, mx))
            if idx == 2:
                break

if __name__ == "__main__":
    ut.main()