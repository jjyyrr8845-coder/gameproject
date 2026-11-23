# game02_escape.py - GAME 02 탈출 게임 (MIDNIGHT EXPRESS)
# 규칙: 탈출에 성공하면 True, 실패하면 False를 돌려준다.

from utils import ask

# ---------- 게임 설정 (바꾸고 싶으면 여기만 고치면 돼요) ----------
CARS = ["1호칸 객실", "2호칸 식당칸", "3호칸 침대칸", "4호칸 화물칸", "5호칸 비상문칸"]
LAST = len(CARS) - 1      # 마지막 칸의 번호 (0부터 세므로 4)
TIME_LIMIT = 10           # 종착역까지 남은 시간(분)
MAX_HP = 3                # 체력 최대치


# ---------- 도우미 함수 ----------

def show_status(player, state):
    """현재 위치, 남은 시간, 체력을 보여준다."""
    print("-" * 32)
    print(f"현재 위치: {CARS[state['pos']]}")
    print(f"남은 시간: {state['time']}분  |  체력: {player['hp']}")
    print("-" * 32)


def show_menu(state):
    """메뉴를 출력하고, 선택 가능한 번호 목록을 돌려준다."""
    print("1) 앞 칸으로 이동")
    print("2) 뒤 칸으로 이동")
    print("3) 주변 살펴보기")
    print("4) 가방 확인")
    options = ["1", "2", "3", "4"]
    if state["pos"] == LAST:
        print("5) 비상문을 열고 탈출한다!")
        options.append("5")
    return options


# ---------- 행동 함수 ----------
def show_bag(player):
    """가방 속 아이템을 보여준다. (시간은 소모하지 않는다)"""
    if len(player["items"]) == 0:
        print("가방이 비어 있다.")
    else:
        for item in player["items"]:
            print("-", item)


def danger_event(player, state):
    """3호칸에 처음 들어갈 때 일어나는 위험 이벤트."""
    print("\n[위험] 열차가 크게 흔들린다! 바닥에 깨진 유리 조각이 흩어져 있다.")
    print("1) 천천히 조심해서 건넌다 (시간 -2분)")
    print("2) 서둘러 뛰어 건넌다 (체력 -1)")
    choice = ask(["1", "2"])
    if choice == "1":
        state["time"] -= 2
        print("조심스레 건넜다. 시간이 조금 걸렸다.")
    else:
        player["hp"] -= 1
        print("유리에 발을 베었다! 하지만 빠르게 건넜다.")
    state["crossed"] = True


def move(player, state, step):
    """step이 1이면 앞 칸, -1이면 뒤 칸으로 이동한다."""
    new_pos = state["pos"] + step

    # 더 갈 수 없는 경우 (시간 소모 없음)
    if new_pos < 0 or new_pos > LAST:
        print("더 이상 갈 수 없다.")
        return

    # 마지막 칸으로 가는 문은 잠겨 있다
    if new_pos == LAST and "열쇠" not in player["items"]:
        print("5호칸으로 가는 문이 잠겨 있다. 열쇠가 필요하다.")
        return
    if new_pos == LAST:
        print("열쇠로 잠긴 문을 열었다!")

    state["pos"] = new_pos
    state["time"] -= 1
    print(f"{CARS[new_pos]}(으)로 이동했다.")

    # 3호칸(번호 2)에 처음 들어가면 위험 이벤트 발생
    if new_pos == 2 and not state["crossed"]:
        danger_event(player, state)


def search(player, state):
    """현재 칸을 살펴본다. 칸마다 한 번만 가능하다."""
    pos = state["pos"]

    if pos in state["searched"]:
        print("이미 살펴본 곳이다.")
        return

    state["searched"].append(pos)
    state["time"] -= 1

    if pos == 0:
        print("좌석 수를 세어 보았다. 좌석은 40개, 승객은 41명이다.")
        print("...한 명이 더 많다. 그 한 명은 누구일까?")
        print("바닥에서 이름이 'ERROR'라고 적힌 낡은 승차권을 주웠다.")
        player["items"].append("낡은 승차권")
    elif pos == 1:
        print("식탁 아래에서 반짝이는 것을 발견했다. 놋쇠 열쇠다!")
        player["items"].append("열쇠")
    elif pos == 2:
        print("침대 옆 서랍에서 구급상자를 찾았다. 체력이 1 회복된다.")
        if player["hp"] < MAX_HP:
            player["hp"] += 1
    elif pos == 3:
        print("상자는 전부 비어 있다. 벽에 걸린 시계가 멈춰 있다.")
    elif pos == 4:
        print("비상문 옆에 'EXIT'라고 적힌 레버가 있다.")
        print("창문에 비친 내 얼굴이 잠깐 깜빡인 것 같다...")


# ---------- GAME 02 메인 ----------
def play(player):
    print("\n==============================")
    print("  GAME 02 | MIDNIGHT EXPRESS")
    print("==============================")
    print("눈을 떠 보니 달리는 야간 열차 안이다.")
    print(f"종착역에 도착하기까지 {TIME_LIMIT}분. 그 전에 열차 밖으로 탈출해야 한다!\n")

    # 이 게임에서만 쓰는 상태값
    state = {
        "pos": 0,             # 현재 객차 번호
        "time": TIME_LIMIT,   # 남은 시간
        "searched": [],       # 이미 살펴본 칸 번호들
        "crossed": False,     # 3호칸 위험 이벤트를 지나갔는가
    }

    while True:
        # 게임 오버 검사
        if player["hp"] <= 0:
            print("\n쓰러졌다... 눈앞이 어두워진다.")
            return False
        if state["time"] <= 0:
            print("\n열차가 종착역에 도착했다... 문이 닫힌다.")
            return False

        show_status(player, state)
        options = show_menu(state)
        choice = ask(options)

        if choice == "1":
            move(player, state, 1)
        elif choice == "2":
            move(player, state, -1)
        elif choice == "3":
            search(player, state)
        elif choice == "4":
            show_bag(player)
        elif choice == "5":
            print("\n레버를 당기자 비상문이 열렸다. 거센 바람 속으로 몸을 던졌다!")
            return True