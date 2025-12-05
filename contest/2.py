n, m = map(int, input().split())

mas = []

for i in range(n):
    h = list(map(int, input().split()))
    mas.append(h)

for i in range(n):
    print(*mas[i])