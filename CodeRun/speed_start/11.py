N = int(input())

synonyms = {}

for _ in range(N):
    words = input().split()
    word1, word2 = words[0], words[1]
    synonyms[word1] = word2
    synonyms[word2] = word1

word = input()

print(synonyms[word])