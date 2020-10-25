def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(L, total):
        nonlocal answer
        if L == n:
            if total == target:
                answer += 1
        else:
            dfs(L+1, total+numbers[L])
            dfs(L+1, total-numbers[L])
    dfs(0, 0)
    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3)) # 5

