import numpy as np
from typing import Generator
from numpy.typing import NDArray

_gen = np.random.default_rng()

def _random_gol(n: int, alive_val: int, dead_val: int) -> NDArray[np.uint8]:
    return _gen.choice([alive_val, dead_val], size=(n, n))

def game_of_life(size: int, alive_val: int = 220, dead_val: int = 0, init_data: NDArray[np.uint8] | None = None)->Generator[NDArray[np.uint8], None, None]:
    prev: NDArray[np.uint8] = _random_gol(size, alive_val, dead_val) if init_data is None else init_data

    def alive_neighbors(row: int, col: int) -> int:
        r_min, r_max = max(row - 1, 0), min(row + 2, size)
        c_min, c_max = max(col - 1, 0), min(col + 2, size)
        
        return np.count_nonzero(prev[r_min:r_max, c_min:c_max] == alive_val) - np.count_nonzero(prev[row, col] == alive_val)

    def next_cell(row: int, col: int) -> int:
        count_alive: int = alive_neighbors(row, col)
        return alive_val if (count_alive == 3 or 
                        (count_alive == 2 and prev[row, col] == alive_val)) else dead_val

    def next_generation() -> NDArray[np.uint8]:
        mx: NDArray[np.uint8] = np.empty((size, size), dtype=np.uint8)
        for row in range(size):
            for col in range(size):
                mx[row, col] = next_cell(row, col)
        return mx

    while True:
        current: NDArray[np.uint8] = next_generation()
        yield prev
        if np.array_equal(prev, current):
            break
        prev = current