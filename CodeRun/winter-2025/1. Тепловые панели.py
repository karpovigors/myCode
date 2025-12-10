R, B = map(int, input().split())


for h in range(1, int(B**0.5) + 1):
    if B % h != 0:
        continue

    w = B // h
    W = w + 2
    H = h + 2

    if 2 * W + 2 * H - 4 == R:
        print(max(W, H), min(W, H))


