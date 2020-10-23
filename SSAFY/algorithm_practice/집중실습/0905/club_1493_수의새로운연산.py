import sys; sys.stdin = open('1493_input.txt', 'r')
# import sys; sys.stdin = open('temp.txt', 'r')
import pprint


def site(a):
    n = 1
    while a > n:
        a -= n
        n += 1
    return n-a+1, a


def num_site(y, x):
    n = x + y - 1
    result = 0
    while n > 0:
        result += n
        n -= 1
    return result + 1 - y


for TC in range(1, int(input())+1):
    p, q = map(int, input().split())
    py, px = site(p)
    qy, qx = site(q)
    y = py + qy
    x = px + qx
    print('#{} {}'.format(TC, num_site(y, x)))
