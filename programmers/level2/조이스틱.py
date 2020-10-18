def solution(name):
    answer = 0
    alpha = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    idx = 0
    while True:
        answer += alpha[idx]
        alpha[idx] = 0

        if sum(alpha) == 0:
            break

        left, right = 1, 1

        while alpha[idx - left] <= 0:
            left += 1

        while alpha[idx + right] <= 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right

    return answer


if __name__ == '__main__':
    print(solution("JEROEN"))   # 56
    print(solution("JAZ"))  # 23
