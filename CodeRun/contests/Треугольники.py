n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
result = 0


for A in range(n):
    for B in range(A + 1, n):
        for C in range(B + 1, n):
            AB = (xy[A][0] - xy[B][0])**2 + (xy[A][1] - xy[B][1])**2
            AC = (xy[A][0] - xy[C][0])**2 + (xy[A][1] - xy[C][1])**2
            BC = (xy[B][0] - xy[C][0])**2 + (xy[B][1] - xy[C][1])**2
            if AB == AC or AC == BC or BC == AB or AB == AC == BC:
                result += 1


print(result)