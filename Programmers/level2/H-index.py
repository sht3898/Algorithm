def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        # citations[i]: i번째 논문의 인용된 수, l-i: i번째에서 남은 논문의 개수
        if citations[i] >= l-i:
            return l-i
    return 0


if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]))    # 3
