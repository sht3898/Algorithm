import sys
sys.stdin = open('./1254_input.txt', 'r')

S = input()
N = len(S)
# 거꾸로 했을때 같은 문자열일때의 인덱스 값 반환
for i in range(N):
    if S[i:] == S[i:][::-1]:
        print(N+i)
        break
