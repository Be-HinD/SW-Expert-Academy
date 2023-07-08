import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    stack = []
    for i in range(9):
        for j in range(9):
            