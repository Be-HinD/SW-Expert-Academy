T = int(input())

for tc in range(1, T+1):
    result = []
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A) < len(B):
        for t in range(len(B) - len(A) + 1):
            cul = 0
            for a in range(len(A)):
                cul += A[a] * B[a+t]
            result.append(cul)
    else:
        for t in range(len(A) - len(B) + 1):
            cul = 0
            for a in range(len(B)):
                cul += A[a+t] * B[a]
            result.append(cul)
    print('#{} {}'.format(tc, max(result)))

"""
주어진 문제의 규칙성은 비교를 했을 때 몇개의 값이 나오는가이며, 이것을 for문 범위에 사용하여 결과 출력
"""