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
    routes = dict()
    for a, b in tickets:
        if a in routes:
            routes[a].append(b)
        else:
            routes[a] = [b]

    for r in routes:
        routes[r].sort(reverse=True)

    st = ["ICN"]
    path = []

    while st:
        top = st[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(st.pop())
        else:
            st.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]


print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))   # [ICN, JFK, HND, IAD]
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))    # [ICN, ATL, ICN, SFO, ATL, SFO]
print(solution2([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))   # [ICN, JFK, HND, IAD]
print(solution2([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))    # [ICN, ATL, ICN, SFO, ATL, SFO]
