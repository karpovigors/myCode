N, K = map(int, input().split())
N_i = list(map(int, input().split()))

j = 0
ans = 0
sum_cur = 0

for i in range(N):
    
    sum_cur += N_i[i]

    while sum_cur > K and i >= j:
        sum_cur -= N_i[j]
        j += 1

    if sum_cur == K:
        ans += 1

print(ans)