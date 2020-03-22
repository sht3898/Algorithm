def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5] * 2000
    second = [2,1,2,3,2,4,2,5] * 1250
    third = [3,3,1,1,2,2,4,4,5,5] * 1000
    ranks = [0] * 3
    for i in range(len(answers)):
        if answers[i] == first[i]:
            ranks[0] += 1
        if answers[i] == second[i]:
            ranks[1] += 1
        if answers[i] == third[i]:
            ranks[2] += 1
    print(ranks)
    if max(ranks) == ranks[0]:
        answer.append(1)
    if max(ranks) == ranks[1]:
        answer.append(2)
    if max(ranks) == ranks[2]:
        answer.append(3)
    return answer
