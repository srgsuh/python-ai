import numpy as np
import unittest as ut
from game_of_life import game_of_life
from numpy.typing import NDArray
from itertools import islice

class TestGameOfLife(ut.TestCase):
    def __zeros(self)->NDArray[np.uint8]:
        return np.zeros((3, 3), dtype=np.uint8)
    
    def __test_sample(self, init_data: NDArray[np.uint8], max_test_size: int = 10)->list[NDArray[np.uint8]]:
        return [mx for mx in islice(game_of_life(3, 1, 0, init_data), max_test_size)]

    def test_zeroes(self)->None:
        output = self.__test_sample(self.__zeros())
        
        self.assertEqual(1, len(output))
        self.assertTrue(np.array_equal(self.__zeros(), output[0]))

    def test_one_neighbor(self)->None:
        init_data = np.array([[1,1,0],[0,0,0],[0,0,0]], dtype=np.uint8)
        output = self.__test_sample(init_data)
        
        self.assertEqual(2, len(output))
        self.assertTrue(np.array_equal(init_data, output[0]))
        self.assertTrue(np.array_equal(self.__zeros(), output[1]))
    
    def test_life_appears_with_3_neigbors(self) -> None:
        init_data = np.array([[1,1,0],[1,0,0],[0,0,0]], dtype=np.uint8)
        brick = np.array([[1,1,0],[1,1,0],[0,0,0]], dtype=np.uint8)
        output = self.__test_sample(init_data)
        self.assertEqual(2, len(output))
        self.assertTrue(np.array_equal(init_data, output[0]))
        self.assertTrue(np.array_equal(brick, output[1]))

    def test_over_population(self) -> None:
        init_data = np.ones((3,3), dtype=np.uint8)
        next =  np.array([[1,0,1],[0,0,0],[1,0,1]], dtype=np.uint8)
        output = self.__test_sample(init_data)
        self.assertEqual(3, len(output))
        self.assertTrue(np.array_equal(init_data, output[0]))
        self.assertTrue(np.array_equal(next, output[1]))
        self.assertTrue(np.array_equal(self.__zeros(), output[2]))
        


if __name__ == "__main__":
    ut.main()