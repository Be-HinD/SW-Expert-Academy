"""
P : 1리터당 요금(A회사)
R : 기본요금 리미트 리터
Q : R리터 이하 기본요금(B회사)
S : R리터 초과 리터당 요금(B회사)
W : 사용한 리터 수
"""
T = int(input())

for tc in range(1, T+1):
    #입력값 P, Q, R, S, W
    
    li = list(map(int, input().split()))
    result = 0
    used = li[4] #사용한 리터
    A_charge = li[0] * used #A회사 이용 시 요금
    if used <= li[2]:
        B_charge = li[1]
    else:
        B_charge = li[1] #기본요금
        B_charge += (used - li[2]) * li[3] #추가요금
    print('#{} {}'.format(tc, min(A_charge, B_charge)))

"""
A회사 vs B회사
"""