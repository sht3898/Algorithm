# 내 풀이
def solution(nums):
    N = len(nums) // 2
    mon = set()
    for n in nums:
        mon.add(n)
    if len(mon) >= N:
        return N
    else:
        return len(mon)


def solution2(nums):
    return min(len(nums)//2, len(set(nums)))


print(solution([3,1,2,3])) # 2
print(solution([3,3,3,2,2,4]))  # 3
print(solution([3,3,3,2,2,2]))  # 2
print(solution2([3,1,2,3])) # 2
print(solution2([3,3,3,2,2,4]))  # 3
print(solution2([3,3,3,2,2,2]))  # 2
