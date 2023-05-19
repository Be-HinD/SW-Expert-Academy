import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    N = int(input())
    box = list(map(int, input().split()))
    for _ in range(N):
        high = max(box)
        low = min(box)
        if high == 0 or low == 0:
            break
        hidx = box.index(high)
        lidx = box.index(low)
        box[hidx] = high - 1
        box[lidx] = low + 1
    print('#{} {}'.format(tc+1, int(max(box)) - int(min(box))))

"""
최대값 최소값 함수 사용
"""