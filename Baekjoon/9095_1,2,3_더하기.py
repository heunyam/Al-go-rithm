DP = [0 for i in range(1000001)]

DP[1] = 1
DP[2] = 2
DP[3] = 4

n = int(input())

for i in range(n):
    num = int(input())
    for j in range(4, num+1):
        DP[j] = DP[j-1] + DP[j-2] + DP[j-3]

    print(DP[num])
