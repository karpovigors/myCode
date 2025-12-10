n, m = map(int, input().split())
a_b = [list(map(int, input().split())) for _ in range(n)]
x_mas = list(map(int, input().split()))
mas = []

for a, b in a_b:
    l, r = min(a, b), max(a, b)
    mas.append([a_b[l][0], 0])
    mas.append([a_b[r][1], 2])

for i, x in enumerate(x_mas):
    mas.append([x, 1, i])
    
mas.sort()

x_res = [0] * len(x_mas)
active = 0

for e in mas:
    if e[1] == 0:
        active += 1
    elif e[1] == 2:
        active -= 1
    else:
        idx = e[2]
        x_res[idx] = active

print(*x_res)
    
