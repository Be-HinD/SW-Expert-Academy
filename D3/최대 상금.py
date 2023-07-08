import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,int(input())+1):
    data, K = input().split() # 숫자판의 정보, 교환횟수
    K = int(K)
    N = len(data)
    now = set([data])
    nxt = set()
    for _ in range(K):
        s = now.pop()
        s = list(s)
        nxt