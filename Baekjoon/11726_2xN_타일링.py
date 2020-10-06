# 2xN 직사각형을 1x2, 2x1 타일로 채우는 방법의 수
# D[i] = 2xi 직사각형을 채우는 방법의 수

# import sys
# n = sys.stdin.readline()

n = int(input())

arr = [0 for i in range(1001)]

arr[1] = 1
arr[2] = 2

for i in range(3, n+1):
    arr[i] = (arr[i-1] + arr[i-2]) % 10007

print(arr[n])
