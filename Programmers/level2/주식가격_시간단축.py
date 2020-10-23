def solution(prices):
    N = len(prices)
    answer = []
    for i in range(N):
        temp = 0
        switch = 0
        for j in range(i + 1, N):
            if prices[i] <= prices[j]:
                temp += 1
            else:
                temp += 1
                answer.append(temp)
                switch = 1
                break

        if not switch:
            answer.append(temp)

    return answer
