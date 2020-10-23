def backtrack(k, n):
    if k == n:
        return 1

    ret = 0
    ret += backtrack(k + 1, n)
    ret += backtrack(k + 1, n)

    return ret


print(backtrack(0, 3))
