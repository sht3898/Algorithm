def solution(prices):
    N = len(prices)
    answer = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

