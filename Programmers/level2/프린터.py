from collections import deque


def solution(pri, location):
    answer = 0
    Q = deque()
    for i in range(len(pri)):
        Q.append((pri[i], i))

    while len(Q):
        item = Q.popleft()
        if Q and max(Q)[0] > item[0]:
            Q.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


import heapq


def solution2(priorities, location):
    answer = 1
    arr = []
    for i, p in enumerate(priorities):
        heapq.heappush(arr, [-p, i])

    while arr:
        check = 0
        for i in range(len(priorities)):
            if priorities[i] == -arr[0][0]:
                if i == location:
                    check = 1
                    break
                heapq.heappop(arr)
                answer += 1
        if check:
            break
    return answer


if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
