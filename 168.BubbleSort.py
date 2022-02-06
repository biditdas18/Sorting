b = [2, 65, 34, 2, 1, 7, 8]


def bubblesort(l):
    count = 0
    lam = len(l)
    while count < lam:
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                l[i], l[i - 1] = l[i - 1], l[i]
        count += 1
    return l


print(bubblesort(b))

"""
When will you use bubble sort?

You are never really going to use it. It's only used for educational purposes as a way to teach sorting
but it's very rare that you will find this in real life because it's just not very efficient.

Time Complexity:
Best: Ω(n)
Average: Θ(n^2)
Worst: O(n^2)

Space Complexity: O(1)
"""
