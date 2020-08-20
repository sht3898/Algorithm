def solution(d, budget):
    answer = 0
    number = 0
    d.sort()
    for i in d:
        if number + i <= budget:
            number += i
            answer += 1
        else:
            break
    return answer


if __name__ == '__main__':
    print(solution([1,3,2,5,4], 9))
