def solution(board, moves):
    stack = []
    answer = 0

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1] != 0:
                stack.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0

                if len(stack) >= 2 and stack[-1] == stack[-2]:
                    answer += 2
                    del stack[-2:]
                break

    return answer

# 문제 이해만 잘 하면 간단하게 풀 수 있는 문제
