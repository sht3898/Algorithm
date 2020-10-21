from collections import deque
import time


def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people)-1
    # pop, remove 등 list를 직접 조작하면 효율성에서 틀림
    # index를 활용하는 것이 효율성면에서 좋음
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        answer += 1
    return answer

# pop(0) 의 경우 데이터를 지우고 한칸씩 앞으로 당기기 때문에 O(1)이 아니라 O(n)이 됩니다.
# 그래서 people을 collections.deque()로 만들어 popleft()를 사용하면 시간초과가 나지 않고 해결됩니다.

def solution2(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while len(people):
        temp = people.pop()
        if len(people) and temp+people[0] <= limit:
            temp += people.popleft()
        answer += 1
    return answer


if __name__ == '__main__':
    start = time.time()
    print(solution([70, 50, 80, 50], 100))  # 3
    print(solution([70, 80, 50], 100))  # 3
    end1 = time.time()-start
    print(end1)
    start = time.time()
    print(solution2([70, 50, 80, 50], 100))  # 3
    print(solution2([70, 80, 50], 100))  # 3
    end2 = time.time()-start
    print(end2)
