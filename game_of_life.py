import numpy as np
from typing import Generator
from numpy.typing import NDArray

_gen = np.random.default_rng()

def _random_gol(size: int, alive_val: np.uint8 | int, dead_val: np.uint8 | int) -> NDArray[np.uint8]:
    rm: NDArray[np.uint8] = np.empty((size, size), dtype=np.uint8)
    for r in range(size):
        for c in range(size):
            rm[r, c] = dead_val if _gen.random() < 0.5 else alive_val
    return rm

def game_of_life(size: int, alive_val: np.uint8 | int = 220, dead_val: np.uint8 | int = 0, init_data: NDArray[np.uint8] | None = None)->Generator[NDArray[np.uint8], None, None]:
    prev: NDArray[np.uint8] = _random_gol(size, alive_val, dead_val) if init_data is None else init_data

    def alive_neighbors(row: int, col: int) -> int:
        count_alive: int = -1 if prev[row, col] == alive_val else 0
        for r in range(max(row - 1, 0), min(row + 2, size)):
            for c in range(max(col - 1, 0), min(col + 2, size)):
                count_alive += 1 if prev[r, c] == alive_val else 0
        return count_alive


    def next_generation() -> NDArray[np.uint8]:
        mx: NDArray[np.uint8] = np.empty((size, size), dtype=np.uint8)
        for row in range(size):
            for col in range(size):
                count_alive: int = alive_neighbors(row, col)
                mx[row, col] = alive_val if (count_alive == 3 or 
                        (count_alive == 2 and prev[row, col] == alive_val)) else dead_val
        return mx

    while True:
        current: NDArray[np.uint8] = next_generation()
        yield prev
        if np.array_equal(prev, current):
            break
        prev = current

if __name__ == "__main__":
    for step, mx in enumerate(game_of_life(3, 1, 0, np.array([[1,1,0],[0,1,1],[0,0,0]], dtype=np.uint8))):
        print(mx)
        if step == 10:
            break