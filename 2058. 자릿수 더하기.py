"""
하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
"""
T = str(input())
li = list(T)
result = 0
for i in li:
    result += int(i)
print(result)
"""
입력값을 str로 받은 후 리스트로 저장
그 후 for문을 통해 자리수를 합한 뒤 결과출력
"""