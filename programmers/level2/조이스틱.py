alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def find(s):
    for i in range(len(alpha)):
        if alpha[i] == s:
            result = min(i, abs(len(alpha)-i))
    return result

def solution(name):
    answer = 0
    for i in range(len(name)):
        answer += find(name[i])
        # print(find(name[i]))
    answer += len(name)-1
    # print(answer)
    return answer


if __name__ == '__main__':
    print(solution("JEROEN"))   # 56
    print(solution("JAZ"))  # 23
