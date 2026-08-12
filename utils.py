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

def handle_exit_confirm():
    try:
        choice = input("\n정말 종료하시겠습니까? (종료 y): ").strip().lower()
        if choice == 'y':
            print("프로그램을 종료합니다.")
            return True 
        else:
            print("프로그램을 다시 시작합니다...")
            return False
    except (KeyboardInterrupt, EOFError):
        print("\n강제 종료합니다.")
        return True
