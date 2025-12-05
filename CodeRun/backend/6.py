N = int(input())
mas = []
for _ in range(N):
    x_y = list(map(int, input().split()))
    mas.append(x_y)

M = int(input())
mars = []
for _ in range(M):
    s_f = list(map(int, input().split()))
    mars.append(s_f)

pref_lr = [0] * N
for i in range(1, N):
    if mas[i][1] > mas[i-1][1]:
        pref_lr[i] = pref_lr[i-1] + (mas[i][1]-mas[i-1][1])
    else:
        pref_lr[i] = pref_lr[i-1]

pref_rl = [0] * N
for i in range(1, N):
    if mas[i-1][1] > mas[i][1]:
        pref_rl[i] = pref_rl[i-1] + (mas[i-1][1]-mas[i][1])
    else:
        pref_rl[i] = pref_rl[i-1]

for i in range(len(mars)):
    s = mars[i][0] - 1
    f = mars[i][1] - 1

    if s < f:
        e = pref_lr[f] - pref_lr[s]
    else:
        e = pref_rl[s] - pref_rl[f]
        
    print(e)