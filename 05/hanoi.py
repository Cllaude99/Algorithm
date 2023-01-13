def hanoi(no, x, y):
    if (no > 1):
        hanoi(no - 1, x, 6-x-y)

    print(f'{no}번 {x}에서 {y}로 이동')

    if (no > 1):
        hanoi(no - 1, 6-x-y, y)


hanoi(3, 1, 3)
