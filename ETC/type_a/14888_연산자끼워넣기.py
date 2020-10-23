import pprint
import sys
sys.stdin = open('14888_input.txt', 'r')


def solve(k, result, add, sub, mul, div):
    global MAX, MIN
    if k == N:
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return
    if add:
        solve(k + 1, result + nums[k], add - 1, sub, mul, div)
    if sub:
        solve(k + 1, result - nums[k], add, sub - 1, mul, div)
    if mul:
        solve(k + 1, result * nums[k], add, sub, mul - 1, div)
    if div:
        if result > 0:
            div_result = result // nums[k]
        else:
            div_result = -(-result // nums[k])  # 음수에서 나눗셈을 하면 1이 더 크게 나옴, 몫이 좌측값으로 가기 때문
        solve(k + 1, div_result, add, sub, mul, div - 1)
    return


N = int(input())
MIN = 1e9
MAX = -1e9
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))
result = nums[0]
solve(1, result, oper[0], oper[1], oper[2], oper[3])
print(MAX, MIN)
