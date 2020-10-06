answer = 0
D = [[0 for col in range(10)] for row in range(1001)]

n = int(input())

for i in range(10):
    D[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(j, 10):
            D[i][j] += D[i-1][k]

for i in range(20):
    for j in range(10):
        print(D[i][j], end=' ')
    print()

for i in range(10):
    answer += D[n][i]

print(answer % 10007)

