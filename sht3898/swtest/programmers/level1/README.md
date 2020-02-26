# 프로그래머스

# 레벨1

* 문자열 압축

  * [링크](https://programmers.co.kr/learn/courses/30/lessons/60057)

  * 풀이

    ```python
    def solution(s):
        def compress(size):
            ret = 0
            before, count = s[:size], 1
            for i in range(size, len(s), size):
                word = s[i:i+size]
                if word == before:
                    count += 1
                else:
                    if count > 1:
                        ret += len(str(count))
                    ret += size
                    before, count = word, 1
            if count > 1:
                ret += len(str(count))
            ret += len(before)
            return ret
    
        ans = len(s)
        for size in range(1, ans+2//2):
            ans = min(ans, compress(size))
        return ans
    ```

    

  

* 완주하지 못한 선수

  * [링크](https://programmers.co.kr/learn/courses/30/lessons/42576)

  * 풀이

    ```python
    # collections.Counter를 사용하면 participant의 요소별 개수를 딕셔너리 형태로 표시
    import collections
    
    
    def solution(participant, completion):
        print(collections.Counter(participant))
        print(collections.Counter(completion))
        answer = collections.Counter(participant) - collections.Counter(completion)
        return list(answer.keys())[0]
    ```

    

* 모의고사

  * [링크](https://programmers.co.kr/learn/courses/30/lessons/42840)

  * 풀이

    ```python
    import collections
    def solution(answers):
        answer = []
        first = [1, 2, 3, 4, 5]
        second = [2, 1, 2, 3, 2, 4, 2, 5]
        third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        ranks = [0] * 3
        for i in range(len(answers)):
            if answers[i] == first[i%len(first)]:
                ranks[0] += 1
            if answers[i] == second[i%len(second)]:
                ranks[1] += 1
            if answers[i] == third[i%len(third)]:
                ranks[2] += 1
        print(ranks)
        if max(ranks) == ranks[0]:
            answer.append(1)
        if max(ranks) == ranks[1]:
            answer.append(2)
        if max(ranks) == ranks[2]:
            answer.append(3)
        return answer
    ```

    

* K번째수

  * [링크](https://programmers.co.kr/learn/courses/30/lessons/42748)

  * 내 풀이

    ```python
    def solution(array, commands):
        answer = []
        for i in commands:
            arr=sorted(array[i[0]-1:i[1]])
            answer.append(arr[i[2]-1])
        return answer
    ```

  * 다른 사람 풀이

    ```python
    def solution(array, commands):
        return list(map(lambda command: sorted(array[command[0]-1:command[1]])[command[2]-1], commands))
    
    ```

    

* 체육복

  * [링크](https://programmers.co.kr/learn/courses/30/lessons/42862)

  * 풀이

    ```python
    def solution(n:int, lost:list, reserve:list)->int:
    
        set_lost = set(lost) - set(reserve)
        set_reserve = set(reserve) - set(lost)
    
        for i in set_reserve:
            if i-1 in set_lost:
                set_lost.remove(i-1)
            elif i+1 in set_lost:
                set_lost.remove(i+1)
    
        return n - len(set_lost)
    
    ```

    

* 2016년

  * [링크](https://programmers.co.kr/learn/courses/30/lessons/12901)

  * 내 풀이

    ```python
    def solution(a, b):
        month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        month_sum = []
        k = 0
        for i in range(12):
            k += month_day[i]
            month_sum.append(k)
        wkday = month_sum[a-1] + b - 1
        answer = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'][wkday % 7]
        return answer
    ```

  * 다른 사람 풀이

    ```python
    def getDayName(a,b):
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
        return days[(sum(months[:a-1])+b-1) % 7]
    
    ```

    

* 가운데 글자 가져오기

  * [링크](https://programmers.co.kr/learn/courses/30/lessons/12903)

  * 풀이

    ```python
    def solution(s):
        if len(s) % 2 :
            answer =  s[len(s) // 2 ]
        else:
            answer =  s[len(s) // 2-1 : len(s) // 2 + 1]
        return answer
    ```

    

* 같은 숫자는 싫어

  * [링크](https://programmers.co.kr/learn/courses/30/lessons/12906)

  * 풀이

    ```python
    def solution(arr):
        answer = []
        before = ''
        for i in range(len(arr)):
            if arr[i] != before:
                answer.append(arr[i])
                before = arr[i]
        return answer
    ```

* 

