b = [2, 65, 34, 2, 1, 7, 8]


# def selectionSort(l):
#     count = 0
#     while count < len(l):
#         smallest = l[count]
#         for i in range(count,len(l)):
#             if l[i] < smallest:
#                 smallest, l[i] = l[i], smallest
#         l[count] = smallest
#         count += 1
#     return l

# b = [2, 65, 34, 2, 1, 7, 8]
def selectionSort2(l):
    count = 0
    while count < len(l):
        smallest = l[count]
        for i in range(count + 1, len(l)):
            if l[i] < smallest:
                smallest = l[i]
                l[count], l[i] = l[i], l[count]
        count += 1
    return l


# print(selectionSort(b))
print(selectionSort2(b))

"""
When will you use bubble sort?

You are never really going to use it. It's only used for educational purposes as a way to teach sorting
but it's very rare that you will find this in real life because it's just not very efficient.

Time Complexity:
Best: Ω(n^2)
Average: Θ(n^2)
Worst: O(n^2)

Space Complexity: O(1)
"""