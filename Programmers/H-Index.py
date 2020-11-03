# 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고,
# 나머지 논문이 h번 이하 인용되는 값 h

# 입력 각 논문 당 인용횟수 : [8, 7, 2, 1, 0, 0]
# 출력 2


def solution(c):
    result = 0

    if min(c) >= len(c):
        result = len(c)

    c.sort(reverse=True)

    for i, ci in enumerate(c):
        if i >= ci:
            return i

    return result


print(solution([22, 42]))
