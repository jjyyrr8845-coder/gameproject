# game01_survival.py - GAME 01 생존 게임 (JACK THE RIPPER)
# 규칙: 안전한 장소에 도착하면 True, 실패하면 False를 돌려준다.

import random
from utils import ask

# ---------- 게임 설정 (바꾸고 싶으면 여기만 고치면 돼요) ----------
STREETS = [
    "어두운 뒷골목",
    "안개 낀 시장 골목",
    "텅 빈 마차 정류장",
    "낡은 우체국 골목",
    "가스등 꺼진 다리 밑",
    "새벽 성당 앞 (안전한 장소)",
]
GOAL = len(STREETS) - 1   # 안전한 장소의 번호 (0부터 세므로 5)
TIME_LIMIT = 10           # 새벽까지 남은 시간
START_DISTANCE = 3        # 처음 추격자와의 거리
MAX_DISTANCE = 5          # 거리는 이보다 더 벌어지지 않는다
CAUGHT_DISTANCE = 1       # 붙잡힌 뒤 간신히 뿌리쳤을 때의 거리
CHASE_MIN = 1             # 이동할 때 추격자가 따라붙는 최소 거리
CHASE_MAX = 2             # 이동할 때 추격자가 따라붙는 최대 거리
RUN_SUCCESS = 7           # 도망치기 성공 확률 (10번 중 7번)
HIDE_SUCCESS = 6          # 숨기 성공 확률 (10번 중 6번)

HIDING_SPOTS = ["쌓아 둔 나무 상자 뒤", "버려진 마차 밑", "열려 있는 지하 계단"]


# ---------- 화면 출력 ----------
def describe_chaser(distance):
    """추격자와의 거리에 따라 분위기 문장을 돌려준다."""
    if distance >= 4:
        return "발소리가 아주 멀다."
    elif distance == 3:
        return "멀리서 발소리가 들린다."
    elif distance == 2:
        return "발소리가 점점 가까워진다."
    else:
        return "바로 뒤에서 숨소리가 들린다!"


def show_status(player, state):
    print("-" * 34)
    print(f"현재 위치: {STREETS[state['pos']]}")
    print(f"새벽까지: {state['time']}  |  체력: {player['hp']}")
    print(f"추격자와의 거리: {'■' * state['distance']}")
    print(describe_chaser(state["distance"]))
    print("-" * 34)
    print("1) 앞으로 이동한다  (안전하지만 추격자가 따라붙는다)")
    print("2) 숨는다          (성공하면 거리가 크게 벌어진다)")
    print("3) 전력으로 도망친다 (거리가 벌어지지만 넘어질 수 있다)")


# ---------- 행동 함수 ----------
def action_move(state):
    """앞으로 이동한다. 추격자가 0~2만큼 따라붙는다."""
    state["pos"] += 1
    gain = random.randint(CHASE_MIN, CHASE_MAX)   # 추격자가 따라잡은 거리
    state["distance"] -= gain

    print("\n안개 속 골목을 따라 앞으로 걸어갔다.")
    if gain == 0:
        print("추격자가 잠시 주춤한 모양이다.")
    elif gain == 1:
        print("발소리가 조금 가까워졌다.")
    else:
        print("추격자가 빠르게 따라붙는다!")


def action_hide(state):
    """숨는다. 성공하면 거리가 +2, 들키면 -2."""
    spot = random.choice(HIDING_SPOTS)
    print(f"\n{spot}에 몸을 숨겼다. 숨을 죽인다...")

    if random.randint(1, 10) <= HIDE_SUCCESS:
        print("추격자가 바로 앞을 지나쳐 갔다! 거리가 크게 벌어졌다.")
        state["distance"] += 2
    else:
        print("들켰다! 추격자가 성큼 다가온다.")
        state["distance"] -= 2


def action_run(player, state):
    """전력으로 도망친다. 성공하면 앞으로 가며 거리 +1, 실패하면 넘어진다."""
    print("\n숨이 턱까지 차오르도록 전력으로 달렸다!")

    if random.randint(1, 10) <= RUN_SUCCESS:
        state["pos"] += 1
        state["distance"] += 1
        print("젖은 돌바닥을 박차고 달려 추격자와 거리를 벌렸다.")
    else:
        player["hp"] -= 1
        state["distance"] -= 1
        print("젖은 돌바닥에 미끄러져 넘어졌다! (체력 -1)")


def arrive_event(player, state):
    """새로운 골목에 도착했을 때의 장면. (앞으로만 이동하므로 한 번씩만 일어난다)"""
    pos = state["pos"]
    if pos == 1:
        print("[시장 골목] 닫힌 가게 사이로 안개가 짙게 깔려 있다.")
    elif pos == 2:
        print("[마차 정류장] 말 한 마리 없이 마차만 덩그러니 서 있다.")
    elif pos == 3:
        print("[우체국 골목] 벽 틈에 끼어 있던 낡은 편지를 발견했다!")
        print("봉인에는 '1888년'과 어울리지 않는 낯선 글자가 새겨져 있다. ...NOVA?")
        player["items"].append("낡은 편지")
    elif pos == 4:
        print("[다리 밑] 안개 너머로 강물 소리가 들린다. 저 멀리 성당의 종탑이 보인다.")


def check_caught(player, state):
    """거리가 0 이하가 되면 붙잡힌다. 체력이 1 줄고, 간신히 뿌리친다."""
    if state["distance"] <= 0:
        player["hp"] -= 1
        print("\n추격자에게 붙잡혔다! 필사적으로 뿌리쳤다... (체력 -1)")
        state["distance"] = CAUGHT_DISTANCE

    # 거리가 너무 멀어지지 않게 제한
    if state["distance"] > MAX_DISTANCE:
        state["distance"] = MAX_DISTANCE


# ---------- 한 턴 / 결과 판정 ----------
def take_turn(player, state, choice):
    """플레이어의 선택 하나를 처리한다."""
    old_pos = state["pos"]

    if choice == "1":
        action_move(state)
    elif choice == "2":
        action_hide(state)
    else:
        action_run(player, state)

    state["time"] -= 1

    if state["pos"] != old_pos:
        arrive_event(player, state)
    check_caught(player, state)

    if state["time"] == 3:
        print("\n동쪽 하늘이 희미하게 밝아 온다. 새벽이 가까워진다...")


def get_result(player, state):
    """게임이 끝났는지 확인한다: 'dead' / 'win' / 'late' / None(계속)"""
    if player["hp"] <= 0:
        return "dead"
    elif state["pos"] >= GOAL:
        return "win"
    elif state["time"] <= 0:
        return "late"
    return None


# ---------- GAME 01 메인 ----------
def play(player):
    print("\n==============================")
    print("  GAME 01 | JACK THE RIPPER")
    print("==============================")
    print("1888년, 안개 낀 런던의 밤. 정신을 차려 보니 낯선 골목에 서 있다.")
    print("뒤에서 정체를 알 수 없는 누군가가 쫓아오고 있다!")
    print("날이 밝기 전에 골목 끝의 성당, 안전한 장소에 도착해야 한다.\n")

    state = {
        "pos": 0,                    # 현재 골목 번호
        "distance": START_DISTANCE,  # 추격자와의 거리
        "time": TIME_LIMIT,          # 새벽까지 남은 시간
    }

    while True:
        show_status(player, state)
        choice = ask(["1", "2", "3"])
        take_turn(player, state, choice)

        result = get_result(player, state)
        if result == "win":
            print("\n성당 문이 열렸다. 안으로 몸을 던지자 무거운 문이 닫힌다.")
            print("문 옆의 작은 명패에, 이 시대엔 없을 글자가 새겨져 있다... NOVA.")
            print("종소리와 함께 동이 터 온다.")
            return True
        elif result == "dead":
            print("\n더는 버틸 수 없었다. 안개 속에서 발소리가 멈췄다.")
            return False
        elif result == "late":
            print("\n동이 터 왔지만 안전한 곳에는 닿지 못했다. 안개가 걷히고 발소리가 가까워진다.")
            return False