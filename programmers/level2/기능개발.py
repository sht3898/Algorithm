def solution(progresses, speeds):
    answer = []
    while sum(answer) < len(progresses):
        temp = 0
        check = 0
        for i in range(len(progresses)):

            if progresses[i] >= 100:
                if i == 0:
                    temp += 1
                else:
                    for j in range(i):
                        if progresses[j] < 100:
                            check = 1
                            break
            if check:
                break

        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
        if temp != 0:
            answer.append(temp)
    return answer


if __name__ == '__main__':
    # print(solution([93, 30, 55], [1, 30, 5]	))  # [2, 1]
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))  # [1, 3, 2]
