# ✨ 영어코딩 — 추가 워크시트

이 폴더는 특정 코스 주차에 묶이지 않은 **단독 워크시트** 를 모아두는 곳입니다.

하나의 개념(예: 중첩 반복문)을 집중해서 연습할 때, 또는 보충·심화 학습이 필요할 때 꺼내 쓰실 수 있습니다.

---

## 📚 워크시트 목록

| 워크시트 | 종류 | 개념 | 📝 받기 |
|---|---|---|---|
| 중첩 반복문 (Nesting) | 연습 | 반복문 안의 반복문 | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/nesting.pdf) |
| 몬스터 웨이브 (Monster Waves) | 연습 · 기초 | 중첩 반복문 · 그림으로 이해하기 · 코드 없음 | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/nested-loops-monster-waves.pdf) |
| 딕셔너리 만들기 — 기초 (Creating Dictionaries) | 연습 · 기초 | 딕셔너리 · 키 · 값 · `{ }` | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/creating-dictionaries.pdf) |
| 딕셔너리 만들기 — 중급 (Add & Update) | 연습 · 중급 | 키 추가 · 값 수정 · `dict[key] = value` | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/creating-dictionaries-intermediate.pdf) |
| 딕셔너리 만들기 — 심화 (Advanced) | 연습 · 심화 | 딕셔너리 리스트 · 중첩 · `.get()` | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/creating-dictionaries-advanced.pdf) |
| 포켓몬 도감 깊이 검색 (Nested Data — Pokédex) | 연습 · 심화 | 중첩 딕셔너리 · 딕셔너리 리스트 · 인덱스 · `.get()` | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/pokedex-deep-search.pdf) |
| 카페 메뉴 — 항목 추가와 가격 변수 (Café Menu) | 숙제 · 중급 | 중첩 딕셔너리 · `.items()` · 변수에 값 담기 · f-string | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/cafe-menu-four-more-items.pdf) |
| CSS 색상과 글씨 꾸미기 (CSS Colors & Text Styling) | 연습 · 기초 | 선택자 · 색상 · padding · border · margin | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/css-colors-text-styling.pdf) |
| CSS 플렉스박스 레이아웃 (CSS Flexbox Layout) | 연습 · 기초 | display: flex · flex-direction · justify-content · align-items · gap | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/css-layout-flexbox.pdf) |
| 헬퍼 함수 만들기 — 기초 (Helper Functions) | 연습 · 기초 | 함수 정의 · 호출 · 매개변수 · 재사용 (반복문 없이) | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/helper-functions.pdf) |
| 파이게임 총알과 리스트 (Bullets & Lists) | 연습 · 심화 | 리스트 복사 `[:]` · 쿨다운 타이머 · 충돌 판정 · 디버깅 | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/pygame-bullets-and-lists.pdf) |
| 파이게임 점수·목숨·HUD (Score, Lives & HUD) | 연습 · 심화 | 게임 루프 · 프레임 · 타이머 · blit · 디버깅 | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/pygame-score-lives-hud.pdf) |
| set과 change 구분 (set or change?) | 연습 · 중급 | 변수 · `set` vs `change` · 커지는 구조물 · 코너 세기 (블록 코딩) | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/variables-set-vs-change.pdf) |
| 미로 1주차 단어 (Maze Wk1 Words) | 단어 | while · loop · detect · wall · forward | [PDF](https://github.com/datawithkasim/english-coding-templates/raw/master/999-extras/worksheets/vocab-week1-maze.pdf) |

> 단어 워크시트는 매주 코스에서 배우는 핵심 단어를 따로 연습하는 자료입니다. 숙제와 함께 보내드릴 수 있습니다.

---

## ➕ 새 워크시트 추가하기

1. `worksheets/이름.md` 로 원본을 만듭니다.
   - 일반 워크시트는 `scripts/templates/week-template.md`
   - 단어 워크시트는 `scripts/templates/vocab-template.md` 를 복사해서 채우면 됩니다.
2. `python scripts/build-worksheets.py` 를 실행하면 PDF가 자동으로 만들어집니다.
3. 위 목록 표에 한 줄 추가합니다.

---

## 📩 자세한 안내

제출은 **카카오톡** 으로, 평소 숙제와 동일합니다. 궁금한 점은 선생님께 편하게 연락 주세요.
