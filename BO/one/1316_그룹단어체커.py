import sys
sys.stdin = open('1316_input.txt', 'r')

N = int(input())
words = [list(input()) for _ in range(N)]
result = 0
for word in words:
    word_used = [word[0]]
    before = word[0]
    for idx in range(len(word)):
        if before == word[idx]:
            before = word[idx]
            if idx == len(word) -1:
                result += 1
        elif before != word[idx] and word[idx] in word_used:
            break
        elif before != word[idx] and word[idx] not in word_used:
            before = word[idx]
            word_used.append(word[idx])
            if idx == len(word)-1:
                result += 1
print(result)
