import sys
sys.stdin = open('1.txt', 'r')


def solution(s):
    new_words = ''
    for word in s:
        for i in range(0, len(word)):
            if i % 2 == 0 and word[i].isalpha():
                new_words += word[i].upper()
            else:
                new_words += word[i].lower()
        new_words += ' '
    return new_words[:-1]


words = input().split(' ')
print(solution(words))
