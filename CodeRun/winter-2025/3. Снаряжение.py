M, N = map(int, input().split())
W = list(map(int, input().split()))
flaw = sum(W) - M

mas = [0 for _ in range(N)]

while sum(mas) != flaw:
    for i in range(N):
        if sum(mas) != flaw:
            mas[i] += 1
        else:
            break

result = 0

for i in range(len(mas)):
    result += mas[i]**2

print(result)



