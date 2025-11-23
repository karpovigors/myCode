x, y, z = map(int, input().split())
N = int(input())

list_xyz = [x, y, z]
list_N = [int(i) for i in str(N)]
i = 0

for k in range(len(list(list_N))):
    if list_N[k] in list_xyz:
        i += 0
    else:
        i += 1
        list_xyz.append(list_N[k])

print(i)
