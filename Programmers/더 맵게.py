import heapq


def solution(scoville=None, k=10):
    if scoville is None:
        scoville = [1, 2, 3, 9, 10, 12]

    heapq.heapify(scoville)
    count = 0
    while scoville[0] < k:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            count += 1
        else:
            return -1

    return count

print(solution())

