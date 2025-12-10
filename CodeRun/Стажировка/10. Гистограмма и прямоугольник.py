# N, *h = map(int, input().split())

mas = []
for i in range(0, N - 1):
    formula = min(h[i], h[i+1]) * 2
    mas.append(formula)

print(max(mas))