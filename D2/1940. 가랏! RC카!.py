"""
0 : 현재 속도 유지.
1 : 가속
2 : 감속
"""
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ms = 0
    result = 0
    for i in range(N):
        command = list(map(int, input().split()))
        if command[0] == 0: #속도유지
            result += ms
        else:
            if command[0] == 1: #가속
                ms += command[1]
                result += ms
            else: #감속
                if ms < command[1]: #현재속도보다 감속할 속도가 더 큰 경우
                    ms = 0
                    result += ms
                else:
                    ms -= command[1]
                    result += ms
    print('#{} {}'.format(tc, result))