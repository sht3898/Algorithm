# 내 풀이
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

# 다른 사람 풀이
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]