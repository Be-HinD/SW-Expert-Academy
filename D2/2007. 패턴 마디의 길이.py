"""
패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.
"""

T = int(input())
result = 0
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = str(input())
    for i in range(1, 11):
        st = a[0:i]
        if st == a[i:i+i]:
            result = len(st)
            break
    print('#{} {}'.format(test_case, result))

"""
비교할 string의 개수를 점진적으로 늘리면서
반복되는 부분이 있는지 확인한 뒤 해당 string의 길이를 반환
"""