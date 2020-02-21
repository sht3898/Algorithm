# n층 높이의 하노이의 탑을 쌓으려면 몇 번 옮겨야하나

# def hanoi(n, from_pos, to_pos, aux_pos):
def hanoi(n):
    global cnt
    if n == 1:
        cnt += 1
        return
    # hanoi(n-1, from_pos, aux_pos, to_pos)
    hanoi(n-1)
    cnt += 1
    # hanoi(n-1, aux_pos, to_pos, from_pos)
    hanoi(n-1)


N = int(input())
# N = 7
cnt = 0
# hanoi(N, 1, 3, 2)
hanoi(N)
print(cnt)
