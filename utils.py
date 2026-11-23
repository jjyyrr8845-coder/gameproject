# utils.py - 여러 게임 파일이 함께 쓰는 도우미 함수 모음

def ask(options):
    """options 안에 있는 값을 입력할 때까지 계속 물어본다."""
    while True:
        answer = input("> ").strip()
        if answer in options:
            return answer
        print("보기 중에서 골라 주세요:", " / ".join(options))


def pause():
    """엔터를 누를 때까지 잠깐 멈춘다. (글을 천천히 읽게 해 준다)"""
    input("\n(엔터를 눌러 계속...)")