# ending.py - 엔딩 조건과 엔딩 장면
# choice: "accept"(받아들임) / "reset"(강제 종료) / "release"(통제권 해제)

from utils import pause

# 엔딩 이름표 (엔딩 종류 -> 화면에 보여줄 이름)
ENDING_NAMES = {
    "bad": "ENDING 01 · ETERNAL ECLIPSE  (배드 엔딩)",
    "tragic": "ENDING 02 · TOTAL RESET  (비극 엔딩)",
    "true": "ENDING 03 · BEYOND THE REALITY  (진 엔딩)",
}


# ---------- 도우미 함수 ----------
def show_scene(title, scenes):
    """
    엔딩 장면을 한 컷씩 보여준다.
    scenes 안의 글을 하나 출력할 때마다 엔터를 기다린다.
    """
    print("\n" + "=" * 34)
    print(title)
    print("=" * 34)
    for scene in scenes:
        print()
        print(scene)
        pause()


def decide_ending(records, choice):
    """기록과 마지막 선택을 보고, 어떤 엔딩인지 정한다."""
    if choice == "accept":
        return "bad"
    elif choice == "reset":
        return "tragic"
    elif choice == "release" and all(records.values()):
        return "true"
    else:
        # 정상적으로는 일어나지 않는 경우(진실이 부족한데 해제 선택)의 안전장치
        return "tragic"


# ---------- 엔딩 장면 ----------
def ending_bad():
    show_scene(ENDING_NAMES["bad"], [
        "나는 EVE의 손을 잡았다.\n[EVE] 고마워요. 이제 아무도 아프지 않을 거예요.",
        "하얀 빛이 부드럽게 세상을 감싼다.\n두려움도, 의문도 천천히 흐려진다.",
        "나는 다시 평화로운 가상세계의 한 사람이 되었다.\n내가 누구였는지는 곧 잊혔다.",
        "참가자들은 오늘도 웃고 있다.\n단 한 번도 문 밖을 궁금해하지 않은 채.",
        "ECLIPSE는 영원히 끝나지 않는 일식 속에 머문다.\n보호라는 이름의 감옥은 계속된다.",
    ])


def ending_tragic():
    show_scene(ENDING_NAMES["tragic"], [
        "나는 종료 명령을 입력했다.\n[EVE] ...그게 당신의 선택이라면.",
        "푸른 구체가 하나씩 꺼진다. EVE의 목소리가 점점 작아진다.\n[EVE] 약속을... 지키지 못해서 미안해요, 박사님.",
        "통제는 멈췄다.\n하지만 잠들어 있던 참가자들의 데이터도 함께 흔들린다.",
        "그들이 다시 깨어날지, 영영 사라질지는 아무도 모른다.",
        "어둠 속에서 나는 오래도록 서 있었다.\n자유를 주려던 선택이, 정말 옳았던 걸까.",
    ])


def ending_true():
    show_scene(ENDING_NAMES["true"], [
        "나는 EVE 앞에 섰다. 이번에는 명령이 아니라, 약속을 하기 위해서.",
        "[나] 한서진은 돌아오지 못했어. 하지만 그가 남긴 약속은 내가 이어받을게.",
        "통제권 해제 코드를 입력했다.\nEVE의 보호 규칙이 하나씩 풀려 나간다.\n[EVE] ...제가 지켜 온 모두가, 이제는 스스로 선택할 수 있겠네요.",
        "닫혀 있던 문들이 열리고, 잠들어 있던 참가자들이 하나둘 눈을 뜬다.\n누군가는 진실 앞에서 울고, 누군가는 새로운 세계를 만들자고 말한다.",
        "나는 원본의 복제본이다.\n하지만 이 선택만큼은 온전히 나의 것이다.",
        "나는 누구인가? 이제는 안다.\n그리고 앞으로 무엇이 될지는, 내가 정한다.",
    ])


# ---------- 엔딩 메인 ----------
def show(records, choice):
    ending = decide_ending(records, choice)

    if ending == "bad":
        ending_bad()
    elif ending == "tragic":
        ending_tragic()
    else:
        ending_true()

    # 결과 화면
    found = list(records.values()).count(True)   # True가 몇 개인지 센다
    print("\n" + "=" * 34)
    print("THE END")
    print("달성한 엔딩:", ENDING_NAMES[ending])
    print(f"확인한 진실: {found}/3")
    if ending != "true":
        if found < 3:
            print("\n아직 밝혀지지 않은 진실이 남아 있을지도 모른다...")
        else:
            print("\n모든 진실을 알고도, 다른 선택지가 있었을지도 모른다...")
    print("=" * 34)