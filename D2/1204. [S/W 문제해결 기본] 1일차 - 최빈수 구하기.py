from collections import Counter
T = int(input())

for tc in range(1, T+1):
    testnum = int(input())
    grade = list(map(int, input().split()))
    result = Counter(grade).most_common()

    print('#{} {}'.format(tc,result[0][0]))

"""
collections 라이브러리 활용해서 최빈수 구하기
"""