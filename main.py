# main.py - 게임 실행, 메뉴, 게임 선택, 전체 흐름 (v1.0)

import game01_survival
import game02_escape
import game03_reality
import ending
from utils import ask, pause

# GAME 01을 다 만들면 True로 바꾸세요. (False이면 선택할 수 없다)
GAME01_READY = True


# ---------- 화면 출력 ----------
def show_title():
    print("\n" + "=" * 34)
    print("        PROJECT: ECLIPSE")
    print("   가상현실 속 생존과 탈출,")
    print("   그리고 숨겨진 진실에 관한 이야기")
    print("=" * 34)


def show_help():
    
    print("\n[게임 설명]")
    print("- 2045년, 당신은 정체를 모른 채 가상현실 속 게임에서 깨어납니다.")
    print("- GAME 01(생존) 또는 GAME 02(탈출) 중 하나를 골라 클리어하세요.")
    print("- 클리어하면 마지막 이야기 GAME 03이 열립니다.")
    print("- GAME 03에서 세 가지 진실을 찾아보세요. 마지막 선택에 따라 엔딩이 달라집니다.")
    print("- 번호를 입력하고 엔터를 누르면 진행됩니다.")
    pause()


# ---------- 게임 흐름 ----------
def new_player():
    """새 플레이어 상태를 만든다. (다시 시작할 때마다 새로 만든다)"""
    return {"hp": 3, "items": []}


def choose_game():
    """GAME 01 / GAME 02 중 하나를 고른다. 0을 입력하면 메인 메뉴로 돌아간다."""
    while True:
        print("\n[게임 선택]")
        if GAME01_READY:
            print("1) GAME 01 생존 - JACK THE RIPPER")
        else:
            print("1) GAME 01 생존 - JACK THE RIPPER  [준비 중]")
        print("2) GAME 02 탈출 - MIDNIGHT EXPRESS")
        print("0) 메인 메뉴로")

        choice = ask(["0", "1", "2"])
        if choice == "1" and not GAME01_READY:
            print("GAME 01은 아직 준비 중이에요. 다른 게임을 골라 주세요.")
        else:
            return choice


def play_game(game_choice):
    """선택한 게임 하나를 끝까지 진행한다. (실패하면 다시 도전할 수 있다)"""
    while True:
        player = new_player()

        if game_choice == "1":
            cleared = game01_survival.play(player)
        else:
            cleared = game02_escape.play(player)

        if cleared:
            # 클리어! GAME 03으로 진행하고 엔딩을 본다
            records, choice = game03_reality.play(player)
            ending.show(records, choice)
            return

        # 실패했을 때
        print("\n=== GAME OVER ===")
        print("1) 다시 도전")
        print("2) 메인 메뉴로")
        if ask(["1", "2"]) == "2":
            return


def main():
    while True:
        show_title()
        print("1) 게임 시작")
        print("2) 게임 설명")
        print("3) 종료")

        choice = ask(["1", "2", "3"])

        if choice == "1":
            game_choice = choose_game()
            if game_choice != "0":
                play_game(game_choice)
                pause()   # 엔딩/게임 오버 후 잠깐 멈췄다가 메인 메뉴로
        elif choice == "2":
            show_help()
        else:
            print("\n플레이해 주셔서 감사합니다.")
            input("엔터를 누르면 종료합니다.")
            break


# 이 파일을 직접 실행했을 때만 게임을 시작한다
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C 등으로 갑자기 종료해도 오류 글자 대신 인사말만 보여 준다
        print("\n\n게임을 종료합니다.")