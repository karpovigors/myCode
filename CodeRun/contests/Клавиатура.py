n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))

counts = {}
for x in p:
    counts[x] = counts.get(x, 0) + 1

for i in range(len(counts)):
    if counts[i+1] > c[i]:
        print("YES")
    else:
        print("NO")