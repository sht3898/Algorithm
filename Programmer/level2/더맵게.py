import heapq


def solution(scoville, K):
    answer = 0
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + second * 2)
            answer += 1
        except:
            return -1
    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))    # 2
