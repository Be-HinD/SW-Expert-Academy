"""
1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
"""

T = int(input())
for i in range(1, T + 1):
    result = 0
    num = int(input())
    for j in range(1, num +1):
        if j%2 == 0:
            result -= j
        else:
            result += j
    print('#{} {}'.format(i, result))

"""
1~N까지의 숫자의 짝수,홀수 여부를 확인하고, 그에 맞게 result값 수정 후 출력
"""