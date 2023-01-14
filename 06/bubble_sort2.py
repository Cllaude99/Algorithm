def bubble_sort(a):
    n = len(a)
    k = 0

    while k < n - 1:
        last = n - 1
        for i in range(n-1, k, -1):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                last = i
        k = last
