participant = ['leo', 'jin', 'par']
completion = ['leo', 'par']


def solution(participant, completion):
    temp = 0
    hash_table = {}

    for p in participant:
        hash_table[hash(p)] = p
        temp += int(hash(p))

    for c in completion:
        temp -= int(hash(c))

    answer = hash_table[temp]
    print(hash_table)
    return answer


print(solution(participant, completion))
