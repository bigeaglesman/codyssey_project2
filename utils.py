import json

FILE_PATH = "./state.json"

def str_to_int(input: str):
    try:
        return int(input)
    except ValueError:
        return None

def get_100score(answer_cnt: int, quiz_cnt: int):
    score: int = int(answer_cnt/quiz_cnt *100)
    return score
