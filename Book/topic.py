import random
import msvcrt as m


topic_list = ['선택정렬', '삽입정렬', '퀵정렬', '버블정렬', '해시', '스택', '큐', '힙', '탐욕(그리디)', '그래프',  '동적계획(DP)', '이분탐색', '완적탐색(BF)', '너비우선탐색(BFS)', '깊이우선탐색(DFS)']


extend_list = []


if __name__ == '__main__':

    temp_list = topic_list[:]

    for i in range(5):
        temp = random.choice(temp_list)
        extend_list.append(temp)
        temp_list.remove(temp)

    topic_list.extend(extend_list)
    for i in range(1, len(topic_list) + 1):
        random.shuffle(topic_list)
        print(f"{i} : {topic_list[i-1]}")
        input()
