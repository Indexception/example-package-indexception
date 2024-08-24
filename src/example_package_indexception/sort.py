

import copy
import random
from typing import Sequence


def bubble_sort(arr: Sequence[int]) -> list[int]:
    arr = list(copy.deepcopy(arr))

    for i in range(1, len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


if __name__ == '__main__':
    # arr = [random.randint(1, 10) for _ in range(10)]
    arr = [8, 4, 5, 8, 8, 5, 10, 2, 8, 1]
    print(arr)
    arr = bubble_sort(arr)
    print(arr)
