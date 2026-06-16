# 🎮 RS004 — 플랫포머 게임 만들기 (Pygame)

16주 동안 Pygame으로 **마리오 스타일 플랫포머 게임**을 처음부터 끝까지 직접 만듭니다. 빈 게임 윈도우에서 출발해 중력·점프·충돌·레벨·코인·적·게임 상태 머신까지 한 단계씩 쌓아 올리며, 처음 만든 코드는 마지막 주까지 버리지 않고 계속 키워 나갑니다.

한 슬라이드 덱을 **학습 주**(새 개념) + **응용 주**(그 개념을 깊이 활용) 두 주에 걸쳐 사용합니다.

> ℹ️ **영어코딩** Pygame 터릿(RS003) 또는 그에 준하는 경험이 있는 학생을 위한 과정입니다. 루프·키보드·도형·함수는 이미 익혔다고 가정합니다.

---

## 📅 주차별 자료

| 주차 | 주제 | 숙제 | 워크시트 | PDF | 슬라이드 |
|---|---|---|---|---|---|
| 1 | 게임 윈도우와 게임 루프 | 배경색·창 크기 바꾸고 RGB 정리 | [week-01](./worksheets/week-01.md) | [📄 PDF](./worksheets/week-01.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-01-game-window.html) |
| 2 | 그라데이션 배경 (응용) | 나만의 그라데이션 배경 | [week-02](./worksheets/week-02.md) | [📄 PDF](./worksheets/week-02.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-01-game-window.html) |
| 3 | 플레이어와 키보드 이동 | 속도·색·크기 튜닝 | [week-03](./worksheets/week-03.md) | [📄 PDF](./worksheets/week-03.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-02-player-keyboard.html) |
| 4 | 방향에 따른 플레이어 표현 (응용) | 나만의 캐릭터 디자인 | [week-04](./worksheets/week-04.md) | [📄 PDF](./worksheets/week-04.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-02-player-keyboard.html) |
| 5 | 중력과 점프 | 점프 감각 값 튜닝 | [week-05](./worksheets/week-05.md) | [📄 PDF](./worksheets/week-05.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-03-gravity-jump.html) |
| 6 | 코요테 타임 + 더블 점프 (응용) | 나만의 점프 폴리시 | [week-06](./worksheets/week-06.md) | [📄 PDF](./worksheets/week-06.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-03-gravity-jump.html) |
| 7 | 플랫폼 충돌 검사 | 플랫폼 배치 후 도달 테스트 | [week-07](./worksheets/week-07.md) | [📄 PDF](./worksheets/week-07.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-04-platforms-collision.html) |
| 8 | 사이드 충돌 + 다양한 플랫폼 (응용) | 벽·통로 포함 레벨 설계 | [week-08](./worksheets/week-08.md) | [📄 PDF](./worksheets/week-08.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-04-platforms-collision.html) |
| 9 | 레벨 디자인 (데이터·재시작·도착) | 플랫폼 7개 이상 + 시작점→도착점이 명확한 나만의 레벨 설계 | [week-09](./worksheets/week-09.md) | [📄 PDF](./worksheets/week-09.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-05-level-design.html) |
| 10 | 종이부터 코드까지 (응용) | 종이 스케치 → 레벨 구현 | [week-10](./worksheets/week-10.md) | [📄 PDF](./worksheets/week-10.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-05-level-design.html) |
| 11 | 코인과 점수 시스템 | 코인 배치 + 점프 코인 | [week-11](./worksheets/week-11.md) | [📄 PDF](./worksheets/week-11.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-06-coins-score.html) |
| 12 | 코인 종류 + 스핀 애니메이션 (응용) | 3종 코인 + 회전 효과 | [week-12](./worksheets/week-12.md) | [📄 PDF](./worksheets/week-12.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-06-coins-score.html) |
| 13 | 적 캐릭터와 게임 오버 | 적 배치 + 최종 점수 화면 | [week-13](./worksheets/week-13.md) | [📄 PDF](./worksheets/week-13.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-07-enemies-gameover.html) |
| 14 | 수직 패트롤 + 사망 효과 (응용) | 3종 적 배치 | [week-14](./worksheets/week-14.md) | [📄 PDF](./worksheets/week-14.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-07-enemies-gameover.html) |
| 15 | 멀티 레벨 구조 | 나만의 3개 레벨 데이터 | [week-15](./worksheets/week-15.md) | [📄 PDF](./worksheets/week-15.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-08-multi-level-final.html) |
| 16 | **최종: 타이틀·레벨 선택·사운드·발표** | 완성 게임 영상 + 발표 자료 | [week-16](./worksheets/week-16.md) | [📄 PDF](./worksheets/week-16.pdf) | [열기](https://datawithkasim.github.io/english-coding-slides/python/rs004-platformer/week-08-multi-level-final.html) |

> 💡 숙제는 **누적적**입니다 — 매주 새 기능을 지난주 코드 위에 쌓아 올립니다.

---

## 📩 숙제 제출

매주 **카카오톡**으로 보내드린 노션 숙제 페이지에서 데모 영상과 자세한 안내를 확인하실 수 있습니다. 완성한 워크시트와 **실행 영상 또는 코드 사진**을 카카오톡으로 선생님께 보내주세요.

---

## 🔗 앱 연동

이 과정은 영어코딩 앱의 학습 경로와 연결됩니다.

- `skill_path` id: **rs004-platformer-0000000000000001**
