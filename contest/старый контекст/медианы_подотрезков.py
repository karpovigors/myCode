N, B = map(int, input().split())
A = list(map(int, input().split()))

col = len(A)

if len(A) % 2 == 0:
    col = len(A) - 1

pos = A.index(B)
mas = []
for k in range(1, col + 1, 2):
    for L in range(0, col - k + 1):
        R = L + k - 1
        if L <= pos <= R:
            mas.append(A[L:R+1])

result = 0

for i in range(len(mas)):
    if len(mas[i]) % 2 != 0:
        sort_A = sorted(mas[i])
        num = int((len(sort_A) - 1) / 2)
        if sort_A[num] == B:
            result += 1

print(result)





