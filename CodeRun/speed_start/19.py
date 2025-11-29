A, B, C, D, E = [int(input()) for _ in range(5)]

min_st, max_st = sorted([D, E])

if (min(A, B) <= min_st and max(A, B) <= max_st or
    min(A, C) <= min_st and max(A, C) <= max_st or
    min(B, C) <= min_st and max(B, C) <= max_st):
    print("YES")
else:
    print("NO")
