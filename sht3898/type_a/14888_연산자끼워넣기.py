import pprint
import sys
sys.stdin = open('14888_input.txt', 'r')


def solve(k, n):
    if k == n:
        return


N = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))  # +,-,*,/
operators = []
print(arr)
for i in range(operator[0]):
    operators.append('+')
for i in range(operator[1]):
    operators.append('-')
for i in range(operator[2]):
    operators.append('*')
for i in range(operator[3]):
    operators.append('/')
print(operators)
