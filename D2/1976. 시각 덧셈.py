"""
시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.

(시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)
"""

T = int(input())

for ts in range(1, T +1):
    time = list(map(int, input().split()))
    hour = time[0] + time[2]
    minute = time[1] + time[3]
    if minute > 59:
        hour += 1
        minute -= 60
    if hour > 12:
        hour -= 12
    print('#{} {} {}'.format(ts, hour, minute))

"""
시간과 분을 따로 변수에 담아 유효성 체크
"""