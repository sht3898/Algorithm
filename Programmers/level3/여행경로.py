from collections import deque


# 테스트케이스만 맞은 풀이
def solution(tickets):
    answer = []
    tickets = deque(sorted(tickets))
    while tickets:
        a, b = tickets.popleft()
        if len(answer) == 0 and a == 'ICN':
            answer.append(a)
            answer.append(b)
        elif len(answer) > 0 and answer[-1] == a:
            answer.append(b)
        else:
            tickets.append([a, b])
    return answer


# 정답
def solution2(tickets):
    routes = {}
    for t in tickets:
        if t[0] not in routes:
            routes[t[0]] = [t[1]]
        else:
            routes[t[0]].append(t[1])
            routes[t[0]].sort()

    stack = ['ICN']
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop(0))

    return path[::-1]


print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))   # [ICN, JFK, HND, IAD]
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))    # [ICN, ATL, ICN, SFO, ATL, SFO]
print(solution2([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))   # [ICN, JFK, HND, IAD]
print(solution2([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))    # [ICN, ATL, ICN, SFO, ATL, SFO]
