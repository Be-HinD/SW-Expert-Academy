#월과 마지막 날 사전
day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
T = int(input())

for tc in range(1, T+1):
    result = 0
    input_ = list(map(int, input().split())) # [5, 5, 8, 15]
    if input_[0] != input_[2]:
        result += day.get(input_[0]) - input_[1] + 1
        result += input_[3]
        for i in range(input_[0] + 1, input_[2]):
            result += day.get(i)
    else:
        result = input_[1] -1 + input_[3]
    print('#{} {}'.format(tc, result))

"""
딕셔너리 선언 및 if 조건문
"""