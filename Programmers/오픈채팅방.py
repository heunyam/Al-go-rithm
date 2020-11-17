RECORD = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


def solution(record):

    users = {}
    proccess = {}
    answer = []

    for i, temp in enumerate(record):
        proccess[i] = temp.split(' ')

    for key in proccess:
        if proccess[key][0] == 'Enter':
            users[proccess[key][1]] = proccess[key][2]
        elif proccess[key][0] == 'Leave':
            pass
        elif proccess[key][0] == 'Change':
            users[proccess[key][1]] = proccess[key][2]

    for key in proccess:
        if proccess[key][0] == 'Enter':
            answer.append(f"{users[proccess[key][1]]}님이 들어왔습니다.")
        elif proccess[key][0] == 'Leave':
            answer.append(f"{users[proccess[key][1]]}님이 나갔습니다.")
        elif proccess[key][0] == 'Change':
            pass

    return answer


print(solution(RECORD))
