T = int(input())

for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    print('#%d' % tc)
    for i in range(N):
        a, b = map(str, input().split())
        for j in range(int(b)):
            cnt += 1
            print(a, end = '')
            if cnt >= 10:
                cnt = 0
                print()
    print()

"""
카운팅 변수 cnt를 활용한 출력
"""