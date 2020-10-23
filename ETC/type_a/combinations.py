import itertools
N, R = 4, 2

arr = itertools.combinations([i for i in range(N)], 2)
for val in arr:
    print(val)

print()
for i in range(N - 1):
    for j in range(i+1, N):
        print((i, j))


print()
# itertools 를 안쓰고 가지치기 하는 이유 -> 가지치기 때문에
sel = []


def backtrack(k, s):    # k: 고른개수, 호출 depth
    if k == R:          # s: 반복의 시작, 이전 고른 요소의 다음
        print(sel)
        return

    for i in range(s, N):
        # i번을 고른다   -> 어딘가에 저장
        sel.append(i)
        backtrack(k+1, i+1)
        sel.pop()
        

backtrack(0, 0)
