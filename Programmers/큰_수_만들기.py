def solution(number, k):
    stack = []
    numlist = list(number)

    length = len(numlist)

    for i in range(length):
        stack.append(numlist[i])
        while k > 0 and len(stack) >= 2 and stack[-2] < stack[-1]:
            stack.pop(-2)
            k -= 1

    # number = 10000, k = 2 같은 케이스 처리
    if k > 0:
        for i in range(k):
            stack.pop(-1)

    answer = str(''.join(stack))
    return answer
