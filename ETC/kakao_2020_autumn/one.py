def solution(new_id):
    # 1단계
    ans = new_id
    ans = ans.lower()

    # 2단계
    temp = ''
    check_list = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    for c in ans:
        if c in check_list:
            temp += c
    ans = temp

    # 3단계
    temp = ''
    last = ''
    for a in ans:
        if a == '.' and last == '.':
            continue
        else:
            temp += a
        last = a
    ans = temp

    # 4단계
    ans = ans.strip('.')

    # 5단계
    if not len(ans):
        ans = 'a'

    # 6단계
    ans = ans[:15]
    ans = ans.rstrip('.')

    # 7단계
    if len(ans) < 3:
        ans += ans[-1] * (3-len(ans))

    return ans


if __name__ == '__main__':
    print(solution('...!@BaT#*..y.abcdefghijklm'))
