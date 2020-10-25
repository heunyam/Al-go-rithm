# 문자열을 뒤집는 함수 작성하기
# 입력값은 문자 배열이며, return 없이 리스트를 직접 조작해야 한다

example_list = ["h", "e", "l", "l", "o"]


def reverse_string(s):
    # s = s[:] 리트코드 서비스에서는 공간 복잡도를 O(0)으로 제한해서 변수 할당을 처리할 때 제약이 생긴다.
    s[:] = s[::-1]  # 대신에 다음과 같은 트릭을 쓸 수 있다.
    print(s)


if __name__ == "__main__":
    reverse_string(example_list)
