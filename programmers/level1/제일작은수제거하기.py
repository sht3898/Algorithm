def solution(arr):
    answer = []
    MIN = min(arr)
    if len(arr) <= 1:
        answer.append(-1)
    else:
        for num in arr:
            if num != MIN:
                answer.append(num)
    return answer