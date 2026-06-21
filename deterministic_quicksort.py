def partition(arr, low, high):
    """
    Partitions the array using the last element as the pivot.
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    """
    Deterministic Quicksort implementation.
    """
    if low < high:
        pivot_index = partition(arr, low, high)

        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original Array:")
    print(arr)

    quicksort(arr, 0, len(arr) - 1)

    print("\nSorted Array:")
    print(arr)


if __name__ == "__main__":
    main()
