"""
10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.

(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
"""

T = int(input())
li = []
for i in range(1, T +1):
    sums = 0
    li = list(map(int, input().split()))
    li.sort()
    li.pop(0)
    li.pop(len(li)-1)
    for j in range(len(li)):
        sums += li[j]
    print('#{} {}'.format(i, round(sums/len(li))))

"""
list로 테스트 케이스를 받고, 정렬 후 평균값 계산 round()가 핵심
"""