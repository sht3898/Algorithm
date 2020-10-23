import math


def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    front = 0
    for idx in range(len(progresses)):
        if progresses[front] < progresses[idx]:
            answer.append(idx-front)
            front = idx
    answer.append(len(progresses)-front)
    return answer


def solution2(progresses, speeds):
    answer = []
    days = 1
    count = 0
    for i in range(len(progresses)):

        if i == 0 and progresses[i]+speeds[i]*days >= 100:
            count += 1
            answer.append(count)
        elif i > 0 and progresses[i]+speeds[i]*days >= 100:
            count += 1
            answer[-1] += 1
        while progresses[i]+speeds[i]*days < 100:
            days += 1
            if progresses[i]+speeds[i]*days >= 100:
                count = 1
                answer.append(count)
                break

    return answer


if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]	))  # [2, 1]
    print(solution2([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))  # [1, 3, 2]
