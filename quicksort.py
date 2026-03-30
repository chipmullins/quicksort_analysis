def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Sorted:", quicksort(data))