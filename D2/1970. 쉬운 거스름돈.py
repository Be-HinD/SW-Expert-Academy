"""
그리디 알고리즘 거스름돈 문제
"""

T = int(input())
won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T+1):
    money = int(input())
    charge = [0] * 8
    for i in range(8):
        charge[i] = int(money/int(won[i]))
        money = int(money%int(won[i]))
    print('#%d'%tc)
    for i in range(8):
        print(charge[i], end = ' ')
    print()
    
"""
거스름돈을 리스트화 시켜 비교 후 잔돈값 갱신
"""