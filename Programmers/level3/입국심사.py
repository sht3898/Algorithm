def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left < right:
        mid = (left + right) // 2
        temp = 0

        for time in times:
            temp += mid // time

        if temp >= n:
            right = mid
        else:
            left = mid + 1

    answer = left
    return answer


print(solution(6, [7, 10])) # 28
