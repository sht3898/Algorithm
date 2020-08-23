def solution(N, stages):
    answer = []
    number = len(stages)
    result = [0] * (N + 2)
    failure = []

    for stage in stages:
        result[stage] += 1

    result = result[1:]
    temp = number

    for idx in range(len(result) - 1):
        if temp != 0:
            failure.append(result[idx] / temp)
            print("{}/{}".format(result[idx], temp))
            temp = temp - result[idx]

    return answer


if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))    # [3,4,2,1,5]
    print(solution(4, [4, 4, 4, 4, 4]))     # [4,1,2,3]
