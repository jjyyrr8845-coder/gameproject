# PROJECT: ECLIPSE

파이썬으로 만든 **텍스트 기반 SF 스토리 게임**입니다.
정체를 알 수 없는 세계에서 세 개의 게임(생존 · 탈출 · 진실 탐색)을 통과하며, 나는 누구이고 이 세계는 무엇인지 밝혀 나갑니다.

> AI융합소프트웨어과 1학년 프로젝트 · Python 기본 문법만으로 구현

---

## 🎮 바로 플레이하기 (Windows)

파이썬을 설치하지 않아도 됩니다.

1. 오른쪽 **Releases** 탭에서 최신 버전의 `ECLIPSE.exe`를 다운로드합니다.
2. 더블클릭해서 실행합니다.
3. "Windows의 PC 보호" 화면이 나오면 **추가 정보 → 실행**을 누릅니다.
   (직접 만든 프로그램에 서명이 없어서 나오는 안내이며, 처음 한 번만 뜹니다.)

> ⚠️ exe는 Windows 전용입니다. Mac / Linux는 아래 "소스로 실행하기"를 이용해 주세요.
> 실행이 처음에 조금 느릴 수 있습니다. 정상입니다.

---

## 🐍 소스로 실행하기 (Windows / Mac / Linux)

Python 3.8 이상이 필요합니다. 별도의 외부 라이브러리는 필요 없습니다.

```bash
git clone <이 저장소 주소>
cd <저장소 폴더>
python main.py        # Mac/Linux에서 python이 안 되면 python3 main.py
```

---

## 🕹️ 게임 방법

숫자를 입력하고 **엔터**를 누르면 진행됩니다. 메뉴에서 "게임 설명"을 선택하면 자세한 규칙을 볼 수 있습니다.

| 게임 | 장르 | 목표 |
|------|------|------|
| GAME 01 · JACK THE RIPPER | 생존 | 새벽이 오기 전에 추격자를 피해 성당에 도착하기 |
| GAME 02 · MIDNIGHT EXPRESS | 탈출 | 종착역에 닿기 전에 열차 밖으로 탈출하기 |
| GAME 03 · THE REALITY | 미스터리 | 자료를 읽고 세 가지 진실을 밝혀내기 |

- 앞의 두 게임에서 실패해도 다시 도전할 수 있습니다.
- 엔딩은 3가지이며, **세 가지 진실을 모두 확인해야** 진 엔딩에 도달할 수 있습니다.

---

## 📁 폴더 구성

```
├── main.py              # 시작 파일 (메인 메뉴, 게임 연결)
├── utils.py             # 입력 받기 · 엔터 대기 등 공용 도우미
├── player.py            # 플레이어 관련(확장용 자리)
├── game01_survival.py   # GAME 01 생존
├── game02_escape.py     # GAME 02 탈출
├── game03_reality.py    # GAME 03 진실 탐색
├── ending.py            # 엔딩 판정과 장면
├── build_exe.bat        # Windows용 exe 만들기 스크립트
└── docs/                # 게임 기획서
```

각 게임 파일은 `play(player)` 함수 하나로 시작되고, 성공하면 `True`, 실패하면 `False`를 돌려주는 같은 규칙을 따릅니다.

---

## 🛠️ exe 직접 만들기 (Windows)

1. Python을 설치합니다. 설치 첫 화면에서 **Add python.exe to PATH**를 꼭 체크합니다.
2. 이 저장소의 파일들이 있는 폴더에서 `build_exe.bat`을 더블클릭합니다.
3. 끝나면 `dist/ECLIPSE.exe`가 생깁니다.

직접 명령어로 만들려면 다음과 같이 입력합니다.

```bash
python -m pip install pyinstaller
python -m PyInstaller --onefile --name ECLIPSE main.py
```

---

## 📄 문서

- 게임 기획서: `docs/` 폴더 (세계관, 게임별 규칙, 엔딩, 파이썬 구현 설명 포함)

---

## ⚙️ 사용 기술

- Python 3 (표준 라이브러리만 사용: `random`)
- PyInstaller (exe 패키징)

## 📝 라이선스

학습용 프로젝트입니다. 라이선스를 정하면 이곳에 적어 주세요. (예: MIT)
