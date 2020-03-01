# 풀이1
def solution(heights):
    answer = []
    for i in range(len(heights)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if heights[i]<heights[j]:
                answer.append(j+1)
                break
        else:
            answer.append(0)
    answer.reverse()
    return answer

# 풀이2
def solution(heights):
    answer = [0] * len(heights)
    for i in range(len(heights)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j+1
                break
    print(answer)
    return answer