N, M, K = map(int, input().split())
mas = [[0 for _ in range(M)] for _ in range(N)]

for i in range(K):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    mas[p][q] = "*"

    if p - 1 >= 0 and q - 1 >= 0 and mas[p-1][q-1] != "*":
        mas[p-1][q-1] += 1
    if p - 1 >= 0 and mas[p-1][q] != "*":
        mas[p-1][q] += 1
    if p - 1 >= 0 and q + 1 < M and mas[p-1][q+1] != "*":
        mas[p-1][q+1] += 1
    
    if q - 1 >= 0 and mas[p][q-1] != "*":
        mas[p][q-1] += 1
    if q + 1 < M and mas[p][q+1] != "*":
        mas[p][q+1] += 1
    
    if p + 1 < N and q - 1 >= 0 and mas[p+1][q-1] != "*":
        mas[p+1][q-1] += 1
    if p + 1 < N and mas[p+1][q] != "*":
        mas[p+1][q] += 1
    if p + 1 < N and q + 1 < M and mas[p+1][q+1] != "*":
        mas[p+1][q+1] += 1


for j in range(len(mas)):
    mas_res = print(*mas[j])
