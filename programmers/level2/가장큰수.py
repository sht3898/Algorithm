def solution(numbers):
    result = []
    n = len(numbers)
    visit = [0] * n

    def solve(k, temp, ans):
        if k == n:
            ans = str(max(int(ans), int(temp)))
            result.append(ans)
            return
        for i in range(n):
            if not visit[i]:
                visit[i] = 1
                tmp = temp
                temp += str(numbers[i])
                solve(k+1, temp, ans)
                temp = tmp
                visit[i] = 0
    solve(0, '', 0)
    return max(result)


if __name__ == '__main__':
    print(solution([6, 10, 2])) # 6210
    print(solution([3, 30, 34, 5, 9]))  # 9534330
