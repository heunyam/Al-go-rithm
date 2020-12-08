# https://programmers.co.kr/learn/courses/30/lessons/12945
import timeit
N = 5


def solution(n):
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b

    return a


if __name__ == '__main__':
    start = timeit.default_timer()

    print(solution(N))

    end = timeit.default_timer()

    print(start, end)
    print(end - start)


