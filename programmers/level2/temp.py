def solution(priorities, location):
    answer = 0
    N = len(priorities)
    visit = [0] * N
    print_list = []
    i = 0
    while sum(visit) != N:
        for j in range(i, N):
            if not visit[i] and not visit[j] and priorities[i] < priorities[j]:
                print_list.append(j)
                visit[j] = 1
                break
        else:
            if not visit[i]:
                print_list.append(i)
                visit[i] = 1
        i = (i+1) % N

    for idx in range(len(print_list)):
        if print_list[idx] == location:
            answer = idx+1
    print(print_list, answer)
    return answer


if __name__ == '__main__':
    # solution([2, 1, 3, 2], 2)
    solution([1, 1, 9, 1, 1, 1], 0)
