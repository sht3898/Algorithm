import sys; sys.stdin = open('1202_input.txt', 'r')

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]   #
bag = [int(input()) for _ in range(K)]  # 가방 무게
print(arr)
print(bag)