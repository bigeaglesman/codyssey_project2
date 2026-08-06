import Quiz
import json

def str_to_int(input: str):
    try:
        return int(input)
    except ValueError:
        return None

def add_quiz(
        question: str, choices: list[str], answer: str):
    if str_to_int(answer) is None:
        print("퀴즈 추가 실패: 정답이 잘못 입력되었습니다")
    else:
        return Quiz.Quiz(question, choices, answer)

def add_basic_quiz():
    basic_quiz_list = [
                add_quiz("지문1",["답1-1", "답1-2", "답1-3", "답1-4"], "1"), 
                add_quiz("지문2", ["답2-1", "답2-2", "답2-3", "답2-4"], "2"), 
                add_quiz("지문3", ["답3-1", "답3-2", "답3-3", "답3-4"], "3"), 
                add_quiz("지문4", ["답4-1", "답4-2", "답4-3", "답4-4"], "4"), 
                add_quiz("지문5", ["답5-1", "답5-2", "답5-3", "답5-4"], "1"), 
                ]
    return basic_quiz_list

def exec_menu(menu_feature: int, basic_quiz_list: list[Quiz.Quiz]):
    if menu_feature == 1:
        solve_quiz(basic_quiz_list)


def solve_quiz(basic_quiz_list: list[Quiz.Quiz]):
    # TODO json파일 읽어서 퀴즈 출제
    answer_cnt : int = 0
    len_quiz: int = len(basic_quiz_list)
    for i, quiz in enumerate(basic_quiz_list):
        set_quiz(i, quiz)
        answer_cnt += submit_answer(quiz)
        print("\n----------------------------------------\n\n")
    print("========================================")
    grade = get_100grade(answer_cnt, len_quiz)
    print(f"🏆 결과: {len_quiz}문제 중 {answer_cnt}문제 정답! ({grade}점)" )


        
def set_quiz(i: int, quiz: Quiz.Quiz):
    print(f"[문제 {i+1}]")
    print(quiz.question)
    print("\n\n")
    for i, choice in enumerate(quiz.choices):
        print(f"{i+1}. {choice}")


def submit_answer(quiz: Quiz.Quiz):
    user_answer: int = input("정답 입력: ")
    return quiz.check_answer(user_answer)

def get_100grade(answer_cnt: int, quiz_cnt: int):
    grade: int = answer_cnt/quiz_cnt *100
    return grade