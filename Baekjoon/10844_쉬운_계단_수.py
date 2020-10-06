D = [[0 for col in range(12)] for row in range(101)]
answer = 0

for i in range(1, 10):
    D[1][i] = 1

for i in range(1, 101):
    for j in range(0, 10):
        if 1 <= j <= 8:
            D[i][j] += D[i-1][j+1] + D[i-1][j-1]
        elif j == 0:
            D[i][j] += D[i-1][j+1]
        elif j == 9:
            D[i][j] += D[i-1][j-1]

n = int(input())
for i in range(0, 10):
    answer += D[n][i]

print(answer % 1000000000)
