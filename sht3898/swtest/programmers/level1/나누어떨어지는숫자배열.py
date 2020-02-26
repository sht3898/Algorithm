def solution(arr):
    answer = []
    before = ''
    for i in range(len(arr)):
        if arr[i] != before:
            answer.append(arr[i])
            before = arr[i]
    return answer
