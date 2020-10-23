def solution(gems):
    answer = []
    gem_list = set(gems)
    length = 100000
    for i in range(len(gems)-len(gem_list)+1):
        for j in range(i+len(gem_list)-1, len(gems)):
            new_gems = gems[i:j+1]
            if len(gem_list) <= len(new_gems) < length:
                if gem_list == (set(new_gems)):
                    answer = [i, j]
                    length = len(new_gems)
    answer = [answer[0]+1, answer[1]+1]
    return answer