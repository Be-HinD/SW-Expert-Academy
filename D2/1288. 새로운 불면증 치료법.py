def cnt_(x):
    cnt = 0
    value = ''
    result = set()
    while 1:
        cnt += 1
        value = str(x * cnt)
        for word in value:
            result.add(word)
        if len(result) == 10:
            return value
        
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    R = cnt_(N)
    print('#{} {}'.format(tc,R))

"""
SET자료형의 중복 특성 활용
"""