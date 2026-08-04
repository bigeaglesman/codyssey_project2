import utils

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        int_answer = utils.str_to_int(answer)
        if int_answer is None:
            raise ValueError("퀴즈 정답 형식 오류")
        if int(answer) >= 1 and int(answer) <= 4:
            self.answer = answer
        else:
            raise ValueError("퀴즈 정답 범위 오류")

    def print_question(self):
        print(self.question)
        return input("정답을 입력하세요: ")

    def check_answer(self, user_answer):
        user_int_answer = utils.str_to_int(user_answer)
        if user_int_answer is None:
            print("정답의 형식이 맞지 않습니다")
            return 0
        elif user_int_answer != self.answer:
            print("오답입니다")
            return 0
        elif user_int_answer == self.answer:
            print("정답입니다")
            return 1

