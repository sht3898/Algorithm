def solution(prior, location):
    answer = 0
    idx = 0
    prior_list = []
    result = []
    for i in range(len(prior)):
        prior_list.append([i, prior[i]])

    while len(prior_list):
        p = prior_list[idx][1]
        for q in prior_list:
            if idx == q[0]:
                continue
            if p < q[1]:
                prior_list.append(prior_list.pop(idx))
                break
        else:
            result.append(prior_list.pop(idx))

    for r in range(len(result)):
        if location == result[r][0]:
            answer = r+1
    return answer


if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
