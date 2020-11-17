def solution(phone_book):
    answer = True

    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = True
    # { number : 1 }

    for phone_number in phone_book:
        # ["12", "123", "1235", ...] 중에서 "12"
        temp = ""

        for number in phone_number:
            # "12" 중에서 "1", "2"
            temp += number

            if temp in hash_map and temp != phone_number:
                # temp가 hash_map에 있는 수 라면 그 수는 number의 접두사가 되기 때문에 false
                return False

    return answer


print(solution(["124", "12", "1235", "567", "88"]))
