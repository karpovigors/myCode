import sys


def main():
    N = int(input())
    mas =[list(map(int,input().split()))for _ in range(N)]
    s, e = map(int,input().split())
    s -= 1
    e -= 1

    d = [-1] * N
    q = [s]
    d[s] = 0

    for v in q:
        for i in range(N):
            if mas[v][i] and d[i]<0:
                d[i] = d[v]+1
                q.append(i)

    print(d[e])


if __name__ == '__main__':
    main()
