def solution(n, m):
    N = [i for i in range(1,n+1) if n%i==0]
    M = [i for i in range(1,m+1) if m%i==0]

    Max = max([i for i in N if i in M])
    Min = Max*(n/Max)*(m/Max)
    answer = [Max, Min]
    return answer


def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer


if __name__ == "__main__":
    print(solution(2, 5))
    print(gcdlcm(2, 5))
