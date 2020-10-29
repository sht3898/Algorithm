def solution(arr):
    def solve(x, y, n):
        if n == 1:
            return [0, 1] if arr[x][y] == 1 else [1, 0]

        left_up = solve(x, y, n // 2)
        right_up = solve(x, y + n // 2, n // 2)
        left_down = solve(x + n // 2, y, n // 2)
        right_down = solve(x + n // 2, y + n // 2, n // 2)

        if left_up == right_up == left_down == right_down == [1,
                                                              0] or left_up == right_up == left_down == right_down == [
            0, 1]:
            return left_up
        else:
            return list(map(sum, zip(left_up, right_up, left_down, right_down)))

    return solve(0, 0, len(arr))


if __name__ == '__main__':
    print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))  # 4, 9
    print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))  # [10, 15]
