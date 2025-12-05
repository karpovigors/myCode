n, m = map(int, input().split())
v = list(map(int, input().split()))

mas = [[] for _ in range(n)]

i = 0
while i < m:
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    mas[a].append(b)
    mas[b].append(a)
    i = i + 1

paths = [[] for _ in range(n)]

paths[0].append([0])

result = []

u = 0
while u < n:
    j = 0
    while j < len(paths[u]):
        path = paths[u][j]

        # считаем сумму
        s = 0
        k = 0
        while k < len(path):
            s = s + v[path[k]]
            k = k + 1
        result.append(s)

        # пытаемся расширить путь
        t = 0
        while t < len(mas[u]):
            to = mas[u][t]

            # проверяем, был ли to в path
            used = 0
            r = 0
            while r < len(path):
                if path[r] == to:
                    used = 1
                r = r + 1

            # можно идти в to
            if used == 0:
                new_path = path + [to]
                paths[to].append(new_path)

            t = t + 1

        j = j + 1
    u = u + 1

# ответ
if len(result) == 0:
    print(v[0])
else:
    print(max(result))
