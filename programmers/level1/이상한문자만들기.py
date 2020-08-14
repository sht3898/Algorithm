def solution(s):
    answer = ''
    word_list = list(s.split(' '))
    for word in word_list:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
    return answer[:-1]


if __name__ == '__main__':
    print(solution('try hello world'))
