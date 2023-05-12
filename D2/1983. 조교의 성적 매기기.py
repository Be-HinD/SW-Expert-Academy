"""
입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고,

학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,

K 번째 학생의 학점을 출력하는 프로그램을 작성하라.
"""

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for i in range(1, T+1):
    li = []
    li_= []
    student = 0
    num = 0
    N, K = map(int, input().split())
    for j in range(N):
        a, b, c = map(int, input().split())
        li.append(round(a*0.35+b*0.45+c*0.2))
        li_ = sorted(li, reverse=True)
    student = li[K-1] # 점수
    div = N/10
    num = int(li_.index(student) // div)
    print('#{} {}'.format(i, grade[num]))

"""
문제 이해가 잘 안됐던 문제, 평점을 N명의 학생에게 어떻게 분배할것인지에 대해서 알고 있다면
list 정렬을 통해 정답 출력
"""