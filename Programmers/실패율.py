N = 5
STAGES = [2, 1, 2, 6, 2, 4, 3, 3]


def solution(N, stages):
    temp = {}
    su = []
    result = []

    for i in range(1, N+1):
        clear = 0
        unclear = 0

        for stage in stages:
            if i == stage:
                unclear += 1
                clear += 1
            elif i < stage:
                clear += 1

        if unclear == 0:
            su.append(0)
            temp[i] = 0
        else:
            su.append(unclear / clear)
            temp[i] = unclear / clear

    su.sort(reverse=True)

    for num in su:
        for key, value in list(temp.items()):
            if num == value:
                result.append(key)
                del temp[key]

    return result


print(solution(N, STAGES))
