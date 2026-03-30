import time
import random
from quicksort import quicksort
from randomized_quicksort import randomized_quicksort

def test_sort(func, arr):
    start = time.time()
    func(arr)
    return time.time() - start

sizes = [100, 500, 1000]

for size in sizes:
    random_list = [random.randint(0, 10000) for _ in range(size)]
    sorted_list = sorted(random_list)
    reverse_list = sorted_list[::-1]

    print(f"\nSize: {size}")

    print("Deterministic (random):", test_sort(quicksort, random_list))
    print("Randomized (random):", test_sort(randomized_quicksort, random_list))

    print("Deterministic (sorted):", test_sort(quicksort, sorted_list))
    print("Randomized (sorted):", test_sort(randomized_quicksort, sorted_list))

    print("Deterministic (reverse):", test_sort(quicksort, reverse_list))
    print("Randomized (reverse):", test_sort(randomized_quicksort, reverse_list))