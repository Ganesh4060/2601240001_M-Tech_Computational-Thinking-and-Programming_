def merge_sort(arr):

    # Base case
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Input
arr = [38, 12, 27, 43, 9, 31]

print("Original array:", arr)

# Merge Sort
sorted_array = merge_sort(arr)

print("Sorted array:", sorted_array)