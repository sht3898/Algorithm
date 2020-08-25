def solution(dartResult):
    result = []
    last = ''
    for d in dartResult:
        if d.isdigit():
            if last.isdigit():
                result[-1] = result[-1] + d
            else:
                result.append(d)
        elif d == 'S':
            result[-1] = str(int(result[-1]) ** 1)
        elif d == 'D':
            result[-1] = str(int(result[-1]) ** 2)
        elif d == 'T':
            result[-1] = str(int(result[-1]) ** 3)
        elif d == '*':
            result[-1] = str(int(result[-1]) * 2)
            try:
                result[-2] = str(int(result[-2]) * 2)
            except:
                continue
        elif d == '#':
            result[-1] = str(int(result[-1])*(-1))
        last = d
    result = map(int, result)
    return sum(result)


if __name__ == '__main__':
    print(solution('1S2D*3T'))
    print(solution('1D2S#10S'))
    print(solution('1D2S0T'))
    print(solution('1S*2T*3S'))
    print(solution('1D#2S*3S'))
    print(solution('1T2D3D#'))
    print(solution('1D2S3T*'))
