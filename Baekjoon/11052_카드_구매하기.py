answer = 0
D = [0 for col in range(1001)]

n = int(input())
input = input()
P = [0]
plist = input.split()

for i in range(0, n):
    P.append(int(plist[i]))

for i in range(1, n+1):
    for j in range(1, i+1):
        D[i] = max(D[i], D[i - j] + P[j])

print(D[n])
