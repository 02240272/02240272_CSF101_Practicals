import random
import time
from math import sqrt, floor

# Linear Search (Modified to return all indices)
def linear_search(arr, target):
    indices = [i for i, val in enumerate(arr) if val == target]
    return indices if indices else [-1]

# Binary Search (Iterative)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

# Recursive Binary Search
def binary_search_recursive(arr, target, left, right, comparisons=0):
    if left > right:
        return -1, comparisons
    comparisons += 1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)

# Find Insertion Point (Binary Search Variant)
def binary_insertion_point(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Count Comparisons (Linear Search)
def count_linear_comparisons(arr, target):
    comparisons = 0
    for val in arr:
        comparisons += 1
        if val == target:
            break
    return comparisons

# Jump Search Algorithm
def jump_search(arr, target):
    comparisons = 0
    n = len(arr)
    step = floor(sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n)-1] < target:
        comparisons += 1
        prev = step
        step += floor(sqrt(n))
        if prev >= n:
            return -1, comparisons

    for i in range(prev, min(step, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# Compare Search Algorithms
def compare_search_algorithms(arr, target):
    print("\nPerformance Comparison:")
    
    # Linear Search
    start = time.time()
    _ = linear_search(arr, target)
    linear_time = time.time() - start
    linear_comps = count_linear_comparisons(arr, target)

    # Binary Search
    arr_sorted = sorted(arr)
    start = time.time()
    _, binary_comps = binary_search(arr_sorted, target)
    binary_time = time.time() - start

    # Jump Search
    start = time.time()
    _, jump_comps = jump_search(arr_sorted, target)
    jump_time = time.time() - start

    print(f"Linear Search: Comparisons = {linear_comps}, Time = {linear_time:.6f} seconds")
    print(f"Binary Search: Comparisons = {binary_comps}, Time = {binary_time:.6f} seconds")
    print(f"Jump Search: Comparisons = {jump_comps}, Time = {jump_time:.6f} seconds")

# Main Function
def main():
    test_list = [random.randint(1, 100) for _ in range(20)]
    sorted_list = sorted(test_list)
    target = random.choice(test_list)

    print("Original List:", test_list)
    print("Sorted List  :", sorted_list)
    print(f"\nTarget: {target}\n")

    # Linear Search (All Indices)
    indices = linear_search(test_list, target)
    print(f"Linear Search: Found at indices {indices}")

    # Binary Search (Iterative)
    index, comps = binary_search(sorted_list, target)
    print(f"Binary Search (Iterative): Found at index {index} with {comps} comparisons")

    # Binary Search (Recursive)
    index, comps = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (Recursive): Found at index {index} with {comps} comparisons")

    # Binary Insertion Point
    insertion_index = binary_insertion_point(sorted_list, target)
    print(f"Insertion point for {target} is index {insertion_index} in sorted list")

    # Jump Search
    index, comps = jump_search(sorted_list, target)
    print(f"Jump Search: Found at index {index} with {comps} comparisons")

    # Compare Performance
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()

