# 입력
# "A man, a plan, a canal: Panama"
# 출력
# true

# 입력
# "race a car"
# 출력
# false

def is_palindrome1(s: str) -> bool:
    result = []
    for char in s:
        if char.isalnum():
            result.append(char.lower())

    while len(result) > 1:
        if result.pop(0) != result.pop():
            return False

    return True
# 리스트로 변환


import collections

def is_palindrome2(s: str) -> bool:
    Deque = collections.deque()

    for char in s:
        if char.isalnum():
            Deque.append(char.lower())

    while len(Deque) > 1:
        if Deque.popleft() != Deque.pop():
            return False

    return True
# 리스트 대신 데크로 이용

import re

def is_palindrome3(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]]', '', s)

    return s == s[::-1]  # s[::-1] == s.reverse()

# 슬라이싱을 통한 문제풀이
# 가장 효율적임

print(is_palindrome2("A man, a plan, a canal: Panama"))
