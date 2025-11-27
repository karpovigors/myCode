n, m, k = map(int, input().split())

mas = []
for _ in range(n):
    row = list(map(int, input().split()))
    mas.append(row)

mas_1 = []
for _ in range(m):
    row = list(map(int, input().split()))
    mas_1.append(row)

mas_result = [[] for _ in range(k)]

if len(mas[0]) == len(mas_1):   
    for i in range(n):
        for j in range(k):
            value = 0
            for t in range(m):
                value += mas[i][t] * mas_1[t][j]
            mas_result[j].append(value)

for row in mas_result:
    print(' '.join(map(str, row)))