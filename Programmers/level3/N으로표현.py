def solution(N, number):
    result = [0, {N}]
    if N == number:
        return 1
    for i in range(2, 9):
        result_set = {int(str(N)*i)}
        for j in range(1, i//2+1):
            for x in result[j]:
                for y in result[i-j]:
                    result_set.add(x+y)
                    result_set.add(x-y)
                    result_set.add(y-x)
                    result_set.add(x*y)
                    if x != 0:
                        result_set.add(y//x)
                    if y != 0:
                        result_set.add(x//y)
        if number in result_set:
            return i
        result.append(result_set)
    return -1


# solution2
answer = -1


def DFS(n, pos, num, number, s):
    global answer
    if pos > 8:
        return
    if num == number:
        if pos < answer or answer == -1:
            #print(s)
            answer=pos
        return

    nn=0
    for i in range(8):
        nn=nn*10+n
        DFS(n, pos+1+i, num+nn, number, s+'+')
        DFS(n, pos+1+i, num-nn, number, s+'-')
        DFS(n, pos+1+i, num*nn, number, s+'*')
        DFS(n, pos+1+i, num/nn, number, s+'/')


def solution2(N, number):
    DFS(N, 0, 0, number, '')
    return answer


print(solution(5, 12))  # 4
print(solution(2, 11))  # 3
print(solution2(5, 12))  # 4
print(solution2(2, 11))  # 3
