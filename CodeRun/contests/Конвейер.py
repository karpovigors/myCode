def quick_sort(mas):
    if len(mas) <= 1:
        return mas
    pivot = mas[len(mas) // 2]
    left = [x for x in mas if x < pivot]
    middle = [x for x in mas if x == pivot]
    right = [x for x in mas if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def conv(mas):
    mas_sort = quick_sort(mas)
    stack = []
    need = 0

    for x in mas:
        while stack and need < len(mas) and stack[-1] == mas_sort[need]:
            stack.pop()
            need += 1

        if x == mas_sort[need]:
            need += 1
        else:
            stack.append(x)

    while stack and need < len(mas) and stack[-1] == mas_sort[need]:
        stack.pop()
        need += 1

    if need == len(mas):
        return 1
    else:
        return 0
    

N = int(input())

K_mas = []

for i in range(N):
    K, *K_i = list(map(float, input().split()))
    K_mas.append(K_i)

for i in range(N):
    print(conv(K_mas[i]))
