b = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        greater = []
        less = []
        for i in arr:
            if i>pivot:
                greater.append(i)
            else:
                less.append(i)
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort(b))

'''
Time Complexity:
Best: Ω(n log(n))
Average: Θ(n log(n))
Worst: O(n^2)

Space Complexity: O(log(n))
'''