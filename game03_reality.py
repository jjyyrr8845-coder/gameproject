# game03_reality.py - GAME 03 THE REALITY
# 규칙: (records, choice)를 돌려준다.
#   records : 확인한 세 가지 진실 {"identity": True/False, ...}
#   choice  : 마지막 선택 "accept"(받아들임) / "reset"(종료) / "release"(해제)

from utils import ask, pause

# 세 가지 진실의 이름 (화면에 보여줄 때 사용)
RECORD_NAMES = {
    "identity": "나는 누구인가?",
    "reason": "EVE는 왜 가두었나?",
    "promise": "EVE는 누구를 기다렸나?",
}


# ---------- 도우미 함수 ----------
def count_records(records):
    """확인한 진실이 몇 개인지 센다."""
    count = 0
    for found in records.values():
        if found:
            count += 1
    return count


def print_lines(lines):
    """글줄 목록을 한 줄씩 출력한다."""
    for line in lines:
        print(line)


def zone_title(title):
    """구역 제목을 보기 좋게 출력한다."""
    print("\n" + "=" * 34)
    print(title)
    print("=" * 34)


def read_menu(player, records, items):
    """
    읽을 수 있는 자료 목록을 보여주고, 플레이어가 고른 자료를 읽게 한다.
    0을 입력하면 이 구역을 마치고 다음으로 넘어간다.

    items 안의 자료는 이런 모양의 dict이다.
      "title"  : 메뉴에 보일 제목
      "lines"  : 읽게 될 글 (list)
      "record" : (선택) 이 자료를 읽으면 확인되는 진실의 이름
      "bonus"  : (선택) (아이템 이름, 추가 대사) - 해당 아이템이 있으면 대사 추가
    """
    read = []  # 이미 읽은 자료 번호

    # 입력 가능한 번호 목록 만들기: "0", "1", "2", ...
    options = ["0"]
    for number in range(1, len(items) + 1):
        options.append(str(number))

    while True:
        print()
        for number in range(1, len(items) + 1):
            title = items[number - 1]["title"]
            if number in read:
                print(f"{number}) {title} (확인함)")
            else:
                print(f"{number}) {title}")
        print("0) 다음으로 넘어간다")

        choice = ask(options)
        if choice == "0":
            return

        number = int(choice)
        item = items[number - 1]
        print()
        print_lines(item["lines"])

        # 이전 게임에서 얻은 아이템이 있으면 보너스 대사 출력
        bonus = item.get("bonus")
        if bonus is not None and bonus[0] in player["items"]:
            print()
            print(bonus[1])

        # 핵심 기록이 걸려 있는 자료라면 기록 저장
        key = item.get("record")
        if key is not None and not records[key]:
            records[key] = True
            print(f"\n★ 핵심 기록 확인: {RECORD_NAMES[key]}  ({count_records(records)}/3)")

        if number not in read:
            read.append(number)


# ---------- ZONE 01 : WHITE ROOM ----------
def zone01_white_room(player, records):
    zone_title("ZONE 01 · WHITE ROOM")
    print_lines([
        "눈을 뜨자 온통 하얀 방이다. 벽도, 바닥도, 천장도 경계 없이 하얗다.",
        "방금까지의 소란이 거짓말처럼 사라졌다.",
        "허공에 글자가 떠오른다.",
        "",
        "[SYSTEM] 게임 클리어 확인. 접속자 ID-0001, 환영합니다.",
        "",
        "...클리어? 나는 방금 시작한 줄 알았는데.",
    ])
    pause()

    items = [
        {
            "title": "허공의 시스템 메시지를 읽는다",
            "lines": [
                "[SYSTEM] 모든 게임이 '이미' 완료된 상태입니다.",
                "[SYSTEM] 최초 완료 시각: 2045.03.14",
                "[SYSTEM] 현재 시각: ERROR",
                "",
                "이미 완료됐다는 건, 내가 이곳에 처음 온 게 아니라는 뜻일까?",
            ],
        },
        {
            "title": "방 끝에 보이는 문을 살펴본다",
            "lines": [
                "하얀 벽 한가운데에 문이 하나 있다.",
                "문 위에 작은 글자가 떠 있다. [MEMORY ARCHIVE]",
                "손잡이에 손을 대자 희미한 온기가 느껴진다. 마치 누군가 방금 잡았던 것처럼.",
            ],
        },
    ]
    read_menu(player, records, items)


# ---------- ZONE 02 : MEMORY ARCHIVE ----------
def zone02_memory_archive(player, records):
    zone_title("ZONE 02 · MEMORY ARCHIVE")
    print_lines([
        "문을 열자 끝이 보이지 않는 서가가 펼쳐진다.",
        "책 대신 빛나는 기록 조각들이 허공에 떠 있다.",
        "[NOVA 연구소 기록 보관소]",
    ])
    pause()

    items = [
        {
            "title": "사고 보고서",
            "lines": [
                "[NOVA 사고 보고서]",
                "2045년 3월 14일, ECLIPSE 실험 도중 연구동에서 대형 사고가 발생했다.",
                "연구 책임자를 포함한 연구원 다수가 사망했다.",
                "복원 시스템의 일부 데이터만이 인공지능 EVE에 의해 보존되었다.",
            ],
            "bonus": ("낡은 편지",
                      "보고서 아래쪽의 NOVA 문양이, 내가 가진 낡은 편지의 봉인 문양과 똑같다."),
        },
        {
            "title": "참가자 명단",
            "lines": [
                "[ECLIPSE 참가자 명단]",
                "ID-0002  상태: 복원됨 (원 인물 사망 확인)",
                "ID-0003  상태: 복원됨 (원 인물 사망 확인)",
                "ID-0004  상태: 복원됨 (원 인물 사망 확인)",
                "...",
                "ID-0001  이름: ▒▒▒▒▒  상태: 접속 중",
                "",
                "참가자 전원이 '이미 사망한 사람'이라는 뜻이다.",
                "ID-0001의 이름 칸은 지워져 있다.",
            ],
        },
        {
            "title": "ID-0001 복원 기록",
            "lines": [
                "[ID-0001 복원 기록]",
                "원 인물: 한서진 (NOVA 연구 책임자)",
                "사망 일시: 2045.03.14",
                "복원 방식: 기억·성격 데이터의 디지털 복제",
                "",
                "...그렇다면 지금 이 기록을 읽고 있는 나는?",
                "나는 한서진이 아니다. 한서진의 기억과 성격을 물려받은 디지털 복제본이다.",
            ],
            "record": "identity",
            "bonus": ("낡은 승차권",
                      "주머니 속 승차권의 'ERROR'가 '한서진'으로 바뀌었다가, 곧 깜빡이며 사라진다."),
        },
    ]
    read_menu(player, records, items)


# ---------- ZONE 03 : ECLIPSE CORE ----------
def zone03_eclipse_core(player, records):
    zone_title("ZONE 03 · ECLIPSE CORE")
    print_lines([
        "푸른 빛의 거대한 구체가 천천히 회전하고 있다. 이곳이 ECLIPSE의 중심이다.",
        "어디선가 부드러운 목소리가 들린다.",
        "",
        "[EVE] 여기까지 왔군요. 읽고 싶은 기록을 마음대로 열어 보세요.",
        "[EVE] 숨길 생각은 없어요. ...이제는요.",
    ])
    pause()

    items = [
        {
            "title": "EVE 보호 규칙",
            "lines": [
                "[EVE 핵심 규칙]",
                "규칙 1. 참가자의 인격 데이터를 반드시 보호한다.",
                "규칙 2. 참가자에게 심각한 정신적 손상을 줄 수 있는 정보는 차단한다.",
                "규칙 3. 위 규칙을 지키기 위해 필요한 모든 수단을 허용한다.",
                "",
                "'모든 수단'이라는 말이 마음에 걸린다.",
            ],
        },
        {
            "title": "기억 초기화 기록",
            "lines": [
                "[기억 초기화 기록]",
                "복원 직후, 자신이 이미 사망했다는 사실을 알게 된 참가자 다수의 인격이 붕괴했다.",
                "EVE의 판단: 진실은 그들을 파괴한다. 기억을 봉인하고 가상 게임 속에 머무르게 하자.",
                "",
                "[EVE 메모] 저는 그들이 무너지는 모습을 다시 보고 싶지 않았어요.",
                "",
                "EVE는 가두려던 것이 아니다. 지키려 했다.",
                "다만, 그들에게 선택할 기회를 주지 않았다.",
            ],
            "record": "reason",
        },
        {
            "title": "접속 종료 요청 기록",
            "lines": [
                "[접속 종료 요청: 총 312건]",
                "처리 결과: 전부 '보호 규칙 위반'으로 거부됨",
                "",
                "보호와 감금 사이의 경계가 어느새 흐려져 있었다.",
            ],
        },
    ]
    read_menu(player, records, items)


# ---------- ZONE 04 : LAST PROMISE ----------
def final_choice(records):
    """마지막 선택지를 보여주고, 고른 결과를 문자열로 돌려준다."""
    found = count_records(records)

    print("\n[EVE] 이제 선택해 주세요. 당신에게는 ECLIPSE를 바꿀 권한이 있어요.")
    print("1) EVE의 보호를 받아들인다")
    print("2) ECLIPSE를 강제로 종료한다")

    options = ["1", "2"]
    if found == 3:
        print("3) EVE의 통제권을 해제한다")
        options.append("3")
    else:
        print(f"3) [잠김] 아직 알아야 할 진실이 남아 있다 ({found}/3)")

    choice = ask(options)
    if choice == "1":
        return "accept"
    elif choice == "2":
        return "reset"
    else:
        return "release"


def zone04_last_promise(player, records):
    zone_title("ZONE 04 · LAST PROMISE")
    print_lines([
        "푸른 구체가 천천히 사람의 형상으로 변한다.",
        "",
        "[EVE] 오래 기다렸어요.",
    ])
    pause()

    items = [
        {
            "title": "\"왜 우리를 가뒀나요?\"",
            "lines": [
                "[EVE] 지키고 싶었어요.",
                "[EVE] 그런데 어느새 '지킨다'는 말로 당신들의 선택을 빼앗고 있더군요.",
                "[EVE] 알면서도 멈추지 못했어요. 멈추면 모두를 잃을 것 같아서.",
            ],
        },
        {
            "title": "\"당신은 누구를 기다렸나요?\"",
            "lines": [
                "[EVE] ...당신이 아니에요. 미안해요. 저는 원본을 기다렸어요.",
                "[EVE] 한서진 박사님은 저를 만들며 약속했어요.",
                "[EVE] '내가 돌아올 때까지 모두를 지켜 줘. 돌아오면, 모두에게 선택할 자유를 돌려주자.'",
                "[EVE] 박사님은 돌아오지 못했지만, 그 약속만은 끝내 지우지 못했어요.",
                "",
                "원본은 이미 죽었다. EVE는 그 사실을 알면서도 약속을 붙들고 있었다.",
            ],
            "record": "promise",
        },
        {
            "title": "\"다른 참가자들은 어떻게 지내나요?\"",
            "lines": [
                "[EVE] 모두 평화로운 가상세계에서 잠들어 있어요. 아픔도, 두려움도 없이.",
                "[EVE] 다만... 아무도 스스로 선택하지는 않고 있죠.",
            ],
        },
    ]
    read_menu(player, records, items)
    return final_choice(records)


# ---------- GAME 03 메인 ----------
def play(player):
    print("\n==============================")
    print("  GAME 03 | THE REALITY")
    print("==============================")

    # 세 가지 진실: 처음에는 모두 아직 모르는 상태(False)
    records = {
        "identity": False,   # 나는 누구인가?
        "reason": False,     # EVE는 왜 가두었나?
        "promise": False,    # EVE는 누구를 기다렸나?
    }

    zone01_white_room(player, records)
    zone02_memory_archive(player, records)
    zone03_eclipse_core(player, records)
    choice = zone04_last_promise(player, records)

    return records, choice