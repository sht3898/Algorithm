def solution(name):
    cnt = 0  # 총 이동 횟수
    a_cnt = 0  # 'A'의 개수
    a_max = 0  # 'A'의 최대개수
    idx = 0  # 최대'A'개수 문자열의 마지막 인덱스
    a_startIdx = 0  # 최대'A'개수 문자열의 첫번째 인덱스
    wander_cnt = 0  # 좌우로 왔다갔다하는 횟수 카운트

    # 위, 아래 조이스틱 계산
    for i, n in enumerate(name):
        if n == 'A':  # 'A'개수의 최대값과 그 인덱스 계산
            a_cnt += 1
            if a_cnt > a_max:
                a_max = a_cnt
                idx = i
        else:
            cnt += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)
            a_cnt = 0

    # 최대'A'개수의 시작 인덱스
    a_startIdx = idx - a_max + 1

    # 최대'A'가 맨 앞이나 맨 끝에 있는 경우
    if a_startIdx == 0 or idx == len(name) - 1:
        cnt += len(name) - 1 - a_max  # a_max개만큼 이동 안해도 됨
    else:
        left = len(name) - idx - 1  # 최대'A'뒤에 남아있는 문자의 개수
        if a_startIdx <= left:  # 뒤에 문자가 앞에 문자개수보다 많은 경우
            wander_cnt = (a_startIdx - 1) * 2 + left
        else:
            wander_cnt = (a_startIdx - 1) + left * 2
        cnt += min(wander_cnt, len(name) - 1)  # 그냥 한쪽방향으로 모두 이동하는 것과 비교

    return cnt


def solution2(name):
    # 1. 알파벳을 맞추는 최소 횟수를 저장하는 배열 m을 만듭니다.
    m = [min(ord(c) - ord("A"), ord("Z") - ord(c) + 1) for c in name]
    answer = 0
    where = 0

    # 2. 위치 where를 0부터 시작해서, 다음을 반복합니다.
    while True:
        # 1. m[where]를 answer에 더합니다
        answer += m[where]
        # 2. m[where]를 0으로 만듭니다.
        m[where] = 0

        # 3. 만약, 현재 m이 모두 0이라면, 반복을 멈춥니다.
        if sum(m) == 0:
            break

        # 4. 3이 만족하지 않을 때, left, right를 1로 만듭니다.
        left, right = (1, 1)

        # 5. m[where-left] <= 0일 때(현재 위치부터 왼쪽에 A가 나오는데)까지, left를 1씩 증가시킵니다.
        while m[where - left] <= 0:
            left += 1
        # 6. m[where+right] <= 0일 때*현재 위치부터 오른쪽에 A가 나오는데)까지 right를 1씩 증가시킵니다.
        while m[where + right] <= 0:
            right += 1

        # 7. left, right를 비교합니다.
        # 7-1. left < right 라면, answer에 left를 더하고, where에 -left를 더합니다.
        # 7-2. 반대라면, answer에 right를 더하고 where에 right를 더합니다.
        answer += left if left < right else right
        where += -left if left < right else right

    return answer


if __name__ == '__main__':
    print(solution2("JEROEN"))   # 56
    print(solution2("JAZ"))  # 23
