"""
해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
”YYYY/MM/DD”형식으로 출력하고,
날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)
"""
T = int(input())
dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T + 1):
    day = str(input())
    YY = day[:4]
    MM = day[4:6]
    DD = day[6:]
    if 0 < int(MM) < 13 and 0 < int(DD) <= dic.get(int(MM)):
        print(f'#{test_case} {YY}/{MM}/{DD}')
    else:
        print(f'#{test_case} -1')
        
"""
딕셔너리 형태의 해당하는 달이 가질 수있는 최대일수를
키값 형태로 저장해놓은 후 입력값을 str로 받아서
년/월/일 슬라이싱 진행
그 후 월/일 부분만 딕셔너리를 통한 유효성 검사 후 결과출력
"""