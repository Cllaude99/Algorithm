def heap_sort(a):
    n = len(a)

    def down_heap(a, left, right):
        parent = left
        temp = a[left]

        while parent < (right + 1) // 2:
            cl = 2*parent + 1
            cr = cl + 1

            child = cr if cr <= right and a[cr] > a[cl] else cl

            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    for i in range((len(a) - 1) // 2, -1, -1):
        down_heap(a, i, len(a) - 1)

    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)


if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None]*num

    for i in range(num):
        x[i] = int(input(f'x[{i}]:  '))

    heap_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
