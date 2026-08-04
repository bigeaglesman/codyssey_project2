import Quiz

def str_to_int(input: str):
    try:
        return int(input)
    except ValueError:
        return None

def add_quiz(question, choices, answer):
    try:
        quiz = Quiz(question, choices, answer)
    except ValueError as e:
        print(f"퀴즈 생성 실패 {e}")
        return None
    else:
        return quiz

def add_basic_quiz():
    quiz_list = []
    quiz = add_quiz("퀴즈1", "선택지", "정답")
    if quiz != None:
        quiz_list.append(quiz)
    
