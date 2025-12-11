N = int(input())

mas = []

for i in range(N):
    xy = list(map(int, input().split()))
    mas.append(xy)

result = len(sorted({p[0] for p in mas}))

print(result)