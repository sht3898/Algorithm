# 내 풀이
# def solution(array, commands):
#     answer = []
#     for i in commands:
#         arr=sorted(array[i[0]-1:i[1]])
#         answer.append(arr[i[2]-1])
#     return answer


# 다른 사람 풀이
def solution(array, commands):
    return list(map(lambda command: sorted(array[command[0]-1:command[1]])[command[2]-1], commands))
