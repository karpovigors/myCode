a = int(input())
b = int(input())
c = int(input())

num = 3 * a + b - c
if num <= 0:
    print(0)
else:
    print((num + 2) // 3)
