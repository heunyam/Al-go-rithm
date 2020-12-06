grid_map = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

def print_grid(gird):
    for i in range(len(grid_map)):
        for j in range(len(grid_map[0])):
            print(grid_map[i][j], end=' ')
        print()

    print("===============")


def dfs(grid, i, j):
    # 종료 조건: 범위를 넘어서거나 더이상 땅이 아닌 경우 종료
    if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] != '1':
        return

    # 방문 했던 곳은 1이 아닌 값으로 마킹
    grid[i][j] = '0'

    # 동서남북 탐색
    dfs(grid, i + 1, j)  # 남
    dfs(grid, i - 1, j)  # 북
    dfs(grid, i, j + 1)  # 동
    dfs(grid, i, j - 1)  # 서


if __name__ == '__main__':

    count = 0
    for i in range(len(grid_map)):
        for j in range(len(grid_map[0])):

            # 육지 발견하면 dfs 함수 호출
            if grid_map[i][j] == '1':
                dfs(grid_map, i, j)

                # 모든 육지 탐색 후 카운트 1 증가
                count += 1

    print(count)
