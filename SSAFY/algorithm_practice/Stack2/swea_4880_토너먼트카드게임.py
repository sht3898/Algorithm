import sys
sys.stdin = open('4880_input.txt', 'r')


def win(a, b):
    if (cards[a-1] == 1 and cards[b-1] == 2) or (cards[a-1] == 2 and cards[b-1] == 3) or (cards[a-1] == 3 and cards[b-1] == 1):
        return b
    return a


def winner(start, end):
    if start == end:
        return end
    a = winner(start, (start+end)//2)
    b = winner((start+end)//2+1, end)
    return win(a, b)


for TC in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))
    print('#{} {}'.format(TC, winner(1, N)))
