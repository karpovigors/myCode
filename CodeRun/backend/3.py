N = int(input())
M = [[] for _ in range(N)]

for i in range(N):
    num = int(input())
    while num != 0:
        language = input().strip()
        M[i].append(language)
        num -= 1

common = []

for language in M[0]:
    ok = True
    for i in range(1, N):
        if language not in M[i]:
            ok = False
            break
    if ok and language not in common:
        common.append(language)

all_langs = []

for i in range(N):
    for language in M[i]:
        if language not in all_langs:
            all_langs.append(language)

print(len(common))
for language in common:
    print(language)

print(len(all_langs))
for language in all_langs:
    print(language)
