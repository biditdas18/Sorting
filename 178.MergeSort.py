b = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def merge_sort(arr):
    if len(arr) > 1:
        arr_left = arr[0:len(arr) // 2]
        arr_right = arr[len(arr) // 2:]

        merge_sort(arr_left)
        merge_sort(arr_right)

        i = 0
        j = 0
        k = 0
        while i < len(arr_left) and j < len(arr_right):
            if arr_left[i] < arr_right[j]:
                arr[k] = arr_left[i]
                i += 1
            else:
                arr[k] = arr_right[j]
                j += 1
            k += 1

        while i < len(arr_left):
            arr[k] = arr_left[i]
            i += 1
            k += 1

        while j < len(arr_right):
            arr[k] = arr_right[j]
            j += 1
            k += 1
    return arr


print(merge_sort(b))


"""
When will we use merge Sort?
If you are worried about the worst case scenario go for merge sort as it offers same time complexity for
best, average and worst
If you want to sort in memory on your machine and you are worried about space complexity, merge sort is
gonna be really expensive as it uses space complexity of O(n).
If you have external sorting then merge sort is good as we won't care about space complexity

Time Complexity:
Best: Ω(n log(n))
Average: Θ(n log(n))
Worst: O(n log(n))

Space Complexity: O(n)
"""