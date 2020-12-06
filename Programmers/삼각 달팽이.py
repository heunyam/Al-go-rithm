from itertools import chain
N = 6


# 아래 -> 오른쪽 -> 위
def solution(n):
    arr = [[0] * n for _ in range(n)]
    answer = []

    x = -1
    y = 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1

            arr[x][y] = num
            num += 1

    for i in arr:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer


print(solution(N))
