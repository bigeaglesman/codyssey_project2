import Quiz
import json

FILE_PATH = "./state.json"

def str_to_int(input: str):
    try:
        return int(input)
    except ValueError:
        return None

def add_quiz(
        question: str, choices: list[str], answer: str):
    if str_to_int(answer) is None:
        print("퀴즈 추가 실패: 정답이 잘못 입력되었습니다")
        return None
    else:
        try:
           quiz: Quiz.Quiz = Quiz.Quiz(question, choices, answer)
           return quiz
        except ValueError as e:
            print(f"퀴즈 추가 중 오류 발생: {e}")
            return None

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
    print(f"선택: {menu_feature}")
    if menu_feature == 1:
        solve_quiz(basic_quiz_list)
    elif menu_feature == 2:
        add_quiz_to_json()
    elif menu_feature == 3:
        check_quiz_list()

def solve_quiz(basic_quiz_list: list[Quiz.Quiz]):
    quiz_list: list[Quiz.Quiz]= get_json_quiz_data_as_instance()
    if quiz_list == None:
        print("기본 문제를 출제합니다")
        quiz_list = basic_quiz_list
    answer_cnt : int = 0
    len_quiz: int = len(quiz_list)
    for i, quiz in enumerate(quiz_list):
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
    grade: int = int(answer_cnt/quiz_cnt *100)
    return grade

def get_json_quiz_data_as_instance():
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            all_data = json.load(f)
            data_quiz_list = all_data["quizzes"]
            quiz_list = [Quiz.Quiz(**item) for item in data_quiz_list]
            return quiz_list
    except FileNotFoundError:
        print("퀴즈 파일이 없습니다")
        return None
    except KeyError:
        print("데이터에 'quizzes'키가 존재하지 않습니다")
        return None
    except ValueError as e:
        print(f"퀴즈 데이터가 손상되었습니다: {e}")
    except PermissionError:
        print("파일 권한 오류")
    except Exception as e:
        print(f"알 수 없는 에러 발생: {e}")

def add_quiz_to_json():
    print("📌 새로운 퀴즈를 추가합니다\n")
    question: str = input("문제를 입력하세요: ")
    choices = []
    for i in range(4):
        choices.append(input(f"선택지 {i+1}: "))
    answer_str: str = input("정답 번호 (1-4): ")
    new_quiz: Quiz.Quiz = add_quiz(question, choices, answer_str)
    get_json_quiz_raw_data(new_quiz)

def get_json_quiz_raw_data(new_quiz: Quiz.Quiz):
    try:
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as f:
                all_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("파일이 존재하지 않아 새로 생성합니다")
            all_data = {"quizzes":[]}
        if 'quizzes' not in all_data:
            all_data['quizzes'] = []
        if not isinstance(all_data['quizzes'], list):
            raise ValueError("'quizzes'키의 데이터가 리스트 형식이 아님")
        all_data['quizzes'].append(new_quiz.to_dict())
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, indent=4, ensure_ascii=False)
        print("✅ 퀴즈가 추가되었습니다!")
    except KeyError:
        print("데이터에 'quizzes'키가 존재하지 않습니다")
    except ValueError as e:
        print(f"퀴즈 데이터가 손상되었습니다: {e}")
    except PermissionError:
        print("파일 권한 오류")
    except Exception as e:
        print(f"알 수 없는 에러 발생: {e}")

def check_quiz_list():
    quiz_list = get_json_quiz_data_as_instance()
    if quiz_list != None:
        if len(quiz_list) != 0:
            for i, quiz in enumerate(quiz_list):
                print(f"[{i+1}] {quiz.question}")
        else:
            print("퀴즈 데이터가 비어있습니다")
