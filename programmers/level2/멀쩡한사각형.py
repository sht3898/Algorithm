def solution(w, h):

    from math import gcd

    k = gcd(w, h)

    w2 = w/k
    h2 = h/k

    return w*h-(w2+h2-1)*k
