def solution(clothes):
    cnt = 1
    wear = {}

    # 옷 종류별 개수 저장
    for cloth in clothes:
        if cloth[1] not in wear:
            wear[cloth[1]] = 1
        else:
            wear[cloth[1]] += 1

    # 옷 종류 별로 옷의 개수+옷을 안입었을 경우(1)를 계산
    for w in wear.values():
        cnt *= (w + 1)

    # 옷을 모두 안입었을 경우 하나를 빼줌
    return cnt - 1


if __name__ == '__main__':
    print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])) # 5
    print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']])) # 3
