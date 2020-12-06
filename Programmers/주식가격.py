from collections import deque


PRICES = [1, 2, 3, 2, 3]


def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        current_price = prices.popleft()
        count = 0

        for price in prices:
            if current_price > price:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer


print(solution(PRICES))
