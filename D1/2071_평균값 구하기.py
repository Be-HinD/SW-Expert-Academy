"""
입력값의 평균값을 구하는 문제
"""
T = int(input())
for test_case in range(1, T + 1):
    li = list(map(int, input().split()))
    result = round(sum(li) / len(li))
    print('#{} {}'.format(test_case, result))

"""
list형식으로 입력값을 읽은 후
list의 합에 리스트의 길이만큼 나눗셈
여기서 결과값이 float형식으로 나올 수 있기에
round() 내장함수를 사용하여 소수점 첫째 자리에서 반올림
"""