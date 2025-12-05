N = int(input())
h = list(map(int, input().split()))

ans = [-1] * N

mas_ch = []
mas_noch = []

for i in range(N):
    hi = h[i]

    if i % 2 == 0:
        stack = mas_ch
    else:
        stack = mas_noch
    
    while stack and h[stack[-1]] < hi:
        j = stack.pop()
        ans[j] = i - j
    
    stack.append(i)

print(*ans)

    