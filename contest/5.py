n, k = map(int, input().split())
mas=[[] for _ in range(k)]

for y in range(k):
    i, j = map(int, input().split())
    mas[y].append(i)
    mas[y].append(j)
