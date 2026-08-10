import utils
import Quiz
import QuizGame

def main():
    quiz_game_manager: QuizGame.QuizGame = QuizGame.QuizGame()
    quiz_game_manager.run()
 

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nkeyboard interrupt 발생")
    except EOFError:
        print("\nEOFError 발생 ")