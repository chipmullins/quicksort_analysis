import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = random.choice(arr)
    arr_copy = arr.copy()
    arr_copy.remove(pivot)
    
    less = [x for x in arr_copy if x <= pivot]
    greater = [x for x in arr_copy if x > pivot]
    
    return randomized_quicksort(less) + [pivot] + randomized_quicksort(greater)


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Sorted:", randomized_quicksort(data))