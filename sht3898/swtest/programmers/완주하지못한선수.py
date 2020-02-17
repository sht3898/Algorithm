# collections.Counter를 사용하면 participant의 요소별 개수를 딕셔너리 형태로 표시
import collections


def solution(participant, completion):
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]