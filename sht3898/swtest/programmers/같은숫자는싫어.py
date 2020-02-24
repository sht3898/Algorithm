def solution(arr):
    answer = ''
    result = []
    before = ''
    for i in range(len(arr)):
        if arr[i] != before:
            result.append(arr[i])
            before = arr[i]
    return result