def solution(prices):
    answer = [0 for _ in range(len(prices))]
    count = 0

    for j in range(5):
        for i in reversed(range(1, 5)):

            x = prices[j]

            if j == i:
                break
            elif prices[i] >= x:
                answer[j] = count
                count += 1

        answer[j] += 1
        count = 0

    answer[-1] = 0

    return answer
