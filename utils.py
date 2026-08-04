def str_to_int(input: str):
    try:
        return int(input)
    except ValueError:
        print("에러 발생: 숫자 변환 실패")
        return None
