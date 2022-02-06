b = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


# def InsertionSort(l):
#     s = []
#     for i in l:
#         if len(s) == 0:
#             s.append(i)
#         else:
#             for j in range(len(s)):
#                 if i > j:
#                     s.insert(j, i)
#                     break
#
#
#     return s

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i - 1] > value_to_sort and i > 0:
            list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]
            i = i - 1

    return list_a


print(insertion_sort(b))

'''
When should you use insertion sort?
1. If your input is small
2. Or Items are mostly sorted

In the above scenario it's really fast, uses very little space and is easy to implement in code

Time Complexity:
Best: Ω(n)
Average: Θ(n^2)
Worst: O(n^2)

Space Complexity: O(1)

'''
