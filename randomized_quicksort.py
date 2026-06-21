import random


def randomized_partition(arr, low, high):
    """
    Chooses a random pivot and partitions the array.
    """
    random_index = random.randint(low, high)

    arr[random_index], arr[high] = arr[high], arr[random_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quicksort(arr, low, high):
    """
    Randomized Quicksort implementation.
    """
    if low < high:
        pivot_index = randomized_partition(arr, low, high)

        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]

    print("Original Array:")
    print(arr)

    randomized_quicksort(arr, 0, len(arr) - 1)

    print("\nSorted Array:")
    print(arr)


if __name__ == "__main__":
    main()
