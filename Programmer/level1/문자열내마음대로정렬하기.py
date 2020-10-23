# 내 풀이
def solution(strings, n):
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()
    for j in range(len(strings)):
        strings[j] = strings[j][1:]        
    return strings

# 다른 사람
from operator import itemgetter, attrgetter, methodcaller

def solution(strings, n):
    return sorted(sorted(strings), key=itemgetter(n))