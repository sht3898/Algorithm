def solution_slow(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    leng = len(routes)
    checked = [0] * leng

    for i in range(leng):
        if checked[i] == 0:
            camera = routes[i][1]
            answer += 1
        for j in range(i + 1, leng):
            if routes[j][0] <= camera <= routes[j][1] and checked[j] == 0:
                checked[j] = 1
    return answer


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))   # 2
print(solution_slow([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))  # 2
