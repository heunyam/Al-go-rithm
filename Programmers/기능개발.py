from collections import deque
import math


def solution(progresses, speeds):

    global count
    temp = deque(list(map(lambda progress, speed: math.ceil((100 - progress) / speed), progresses, speeds)))
    answer = []
    print(temp)
    while temp:
        p = temp.popleft()
        count = 1

        while temp:

            if p >= temp[0]:
                count += 1
                temp.popleft()
            else:
                answer.append(count)
                break

    answer.append(count)

    return answer


print(solution(PROGRESSES, SPEEDS))
