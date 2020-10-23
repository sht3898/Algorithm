# 풀이1
def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        check = 1
        skills = []
        for i in s:
            if i in skill:
                skills.append(i)
        result = ''.join(skills)
        for j in range(len(result)):
            if result[j] != skill[j]:
                check = 0
                break
        if check:
            answer += 1
    return answer


# 풀이2
def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        skills = []
        for i in s:
            if i in skill:
                skills.append(i)
        result = ''.join(skills)
        for j in range(len(result)):
            if result[j] != skill[j]:
                break
        else:
            answer += 1
    return answer