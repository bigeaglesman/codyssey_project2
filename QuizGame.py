import Quiz
import utils
import json

class QuizGame:
    def __init__(self):
        print("QuizGame객체 생성")
        print("basic quiz list 생성")
        self.basic_quiz_list: list[Quiz.Quiz] = self.add_basic_quiz()
        print("quiz list 생성")
        self.quiz_list: list[Quiz.Quiz]= self.get_json_quiz_data_as_instance()
        print("")
        self.best_score: int = self.get_best_score()
        if self.best_score == None:
            self.best_score = 0

    def run(self):
        while True:
            self.show_menu()
            feature = utils.str_to_int(input("선택: "))
            if feature is None:
                print("숫자 변환 실패")
            elif feature < 1 or feature > 5:
                print ("허용 범위 밖의 숫자입니다")
            elif feature == 5:
                print("프로그램을 종료합니다")
                break
            else: 
                self.exec_menu(feature)

    def show_menu(self):
        print("""
        ========================================
                🎯 나만의 퀴즈 게임 🎯
        ========================================
        1. 퀴즈 풀기
        2. 퀴즈 추가
        3. 퀴즈 목록
        4. 점수 확인
        5. 종료
        ========================================""")

    def add_basic_quiz(self):
        basic_quiz_list = [
                    self.add_quiz("지문1",["답1-1", "답1-2", "답1-3", "답1-4"], "1"), 
                    self.add_quiz("지문2", ["답2-1", "답2-2", "답2-3", "답2-4"], "2"), 
                    self.add_quiz("지문3", ["답3-1", "답3-2", "답3-3", "답3-4"], "3"), 
                    self.add_quiz("지문4", ["답4-1", "답4-2", "답4-3", "답4-4"], "4"), 
                    self.add_quiz("지문5", ["답5-1", "답5-2", "답5-3", "답5-4"], "1"), 
                    ]
        return basic_quiz_list

    def add_quiz(self, 
            question: str, choices: list[str], answer: str):
        if utils.str_to_int(answer) is None:
            print("퀴즈 추가 실패: 정답이 잘못 입력되었습니다")
            return None
        else:
            try:
                quiz= Quiz.Quiz(question, choices, answer)
                return quiz
            except ValueError as e:
                print(f"퀴즈 추가 중 오류 발생: {e}")

    def exec_menu(self, menu_feature: int):
        print(f"선택: {menu_feature}")
        if menu_feature == 1:
            self.solve_quiz()
        elif menu_feature == 2:
            self.add_quiz_to_json()
        elif menu_feature == 3:
            self.check_quiz_list()
        elif menu_feature == 4:
            self.print_best_score()

    def solve_quiz(self):
        if self.quiz_list == None:
            solve_quiz_list = self.basic_quiz_list
        else:
            solve_quiz_list = self.quiz_list
        answer_cnt : int = 0
        len_quiz: int = len(solve_quiz_list)
        for i, quiz in enumerate(solve_quiz_list):
            self.print_quiz(i, quiz)
            answer_cnt += self.submit_answer(quiz)
            print("\n----------------------------------------\n\n")
        print("========================================")
        score = utils.get_100score(answer_cnt, len_quiz)
        print(f"🏆 결과: {len_quiz}문제 중 {answer_cnt}문제 정답! ({score}점)" )
        if score > self.best_score:
            self.best_score = score
            self.dump_best_score_data(self.best_score)

        
    def print_quiz(self, i: int, quiz: Quiz.Quiz):
        print(f"[문제 {i+1}]")
        print(quiz.question)
        print("\n\n")
        for i, choice in enumerate(quiz.choices):
            print(f"{i+1}. {choice}")

    def submit_answer(self, quiz: Quiz.Quiz):
        user_answer: int = input("정답 입력: ")
        return quiz.check_answer(user_answer)

    def get_json_quiz_data_as_instance(self):
        try:
            with open(utils.FILE_PATH, 'r', encoding='utf-8') as f:
                all_data = json.load(f)
                data_quiz_list = all_data["quizzes"]
                quiz_list = [Quiz.Quiz(**item) for item in data_quiz_list]
                return quiz_list
        except FileNotFoundError:
            print("퀴즈 파일이 없습니다 퀴즈 데이터를 가져올 수 없습니다")
        except KeyError:
            print("데이터에 'quizzes'키가 존재하지 않습니다")
        except ValueError as e:
            print(f"퀴즈 데이터가 손상되었습니다: {e}")
        except PermissionError:
            print("파일 권한 오류")
        except Exception as e:
            print(f"알 수 없는 에러 발생: {e}")

    def add_quiz_to_json(self):
        print("📌 새로운 퀴즈를 추가합니다\n")
        question: str = input("문제를 입력하세요: ")
        choices = []
        for i in range(4):
            choices.append(input(f"선택지 {i+1}: "))
        answer_str: str = input("정답 번호 (1-4): ")
        new_quiz: Quiz.Quiz = self.add_quiz(question, choices, answer_str)
        if new_quiz != None:
            self.dump_quiz_data(new_quiz)
            self.quiz_list = self.get_json_quiz_data_as_instance()

    def dump_quiz_data(self, new_quiz: Quiz.Quiz):
        try:
            try:
                with open(utils.FILE_PATH, 'r', encoding='utf-8') as f:
                    all_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                print("파일이 존재하지 않아 새로 생성합니다")
                all_data = {"quizzes":[]}
            if 'quizzes' not in all_data:
                all_data['quizzes'] = []
            if not isinstance(all_data['quizzes'], list):
                raise ValueError("'quizzes'키의 데이터가 리스트 형식이 아님")
            all_data['quizzes'].append(new_quiz.to_dict())
            with open(utils.FILE_PATH, 'w', encoding='utf-8') as f:
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

    def check_quiz_list(self):
        if self.quiz_list == None:
            quiz_list = self.basic_quiz_list
        else:
            quiz_list = self.quiz_list
        if len(quiz_list) != 0:
            for i, quiz in enumerate(quiz_list):
                print(f"[{i+1}] {quiz.question}")
        else:
            print("퀴즈 데이터가 비어있습니다")

    def get_best_score(self):
        try:
            with open(utils.FILE_PATH, 'r', encoding='utf-8') as f:
                all_data = json.load(f)
                best_score = all_data["best_score"]
                int_best_score = int(best_score)
                if int_best_score < 0 or int_best_score > 100:
                    raise ValueError("최고 점수가 범위를 벗어났습니다")
                return int_best_score
        except FileNotFoundError:
            print("퀴즈 파일이 없습니다 최고 점수를 가져올 수 없습니다")
        except KeyError:
            print("데이터에 'best_score'키가 존재하지 않습니다")
        except ValueError as e:
            print(f"데이터가 손상되었습니다: {e}")
        except PermissionError:
            print("파일 권한 오류")
        except Exception as e:
            print(f"알 수 없는 에러 발생: {e}")

    def dump_best_score_data(self, new_best_score: int):
        try:
            try:
                with open(utils.FILE_PATH, 'r', encoding='utf-8') as f:
                    all_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                print("파일이 존재하지 않아 새로 생성합니다")
                all_data = {"best_score":0}
            all_data.update({"best_score": new_best_score})
            with open(utils.FILE_PATH, 'w', encoding='utf-8') as f:
                json.dump(all_data, f, indent=4, ensure_ascii=False)
            print("최고점수가 업데이트되었습니다")
        except PermissionError:
            print("파일 권한 오류")
        except Exception as e:
            print(f"알 수 없는 에러 발생: {e}")

    def print_best_score(self):
        print(f"🏆 최고 점수: {self.best_score}점")