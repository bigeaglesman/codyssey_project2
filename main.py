import utils
import Quiz

def main():
    while True:
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
        feature = utils.str_to_int(input("선택: "))
        if feature is None:
            continue
        elif feature < 1 or feature > 5:
            print ("허용 범위 밖의 숫자입니다")
            return None
        elif feature == 5:
            print("프로그램을 종료합니다")
            break
 


    


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nkeyboard interrupt 발생")
    except EOFError:
        print("\nEOFError 발생 ")