import Quiz

def str_to_int(input: str):
    try:
        return int(input)
    except ValueError:
        return None

def add_quiz(question, choices, answer):
    if str_to_int(answer) is None:
        print("퀴즈 추가 실패: 정답이 잘못 입력되었습니다")
    else:
        return Quiz(question, choices, answer)

def add_basic_quiz():
    quiz_list = [add_quiz("지문1", "정답지1", "1"), 
                add_quiz("지문2", "정답지2", "2"), 
                add_quiz("지문3", "정답지3", "3"), 
                add_quiz("지문4", "정답지4", "4"), 
                add_quiz("지문5", "정답지5", "1"), 
                 ]
    return quiz_list
    
