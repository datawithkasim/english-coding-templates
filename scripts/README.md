# 🛠️ scripts/

워크시트·핸드아웃을 PDF로 빌드하는 도구가 들어 있습니다.

## build-worksheets.py

모든 `*/worksheets/*.md` 파일을 인쇄용 PDF로 변환합니다.

```
worksheets/<이름>.md
  → worksheets/_html/<이름>.html   (브랜드 스타일 적용, A4)
  → worksheets/<이름>.pdf          (Edge headless --print-to-pdf)
```

### 실행

```bash
pip install -r requirements.txt        # 최초 1회 (markdown 패키지)
python scripts/build-worksheets.py     # 전체 워크시트 빌드
```

- **Microsoft Edge** 가 설치되어 있어야 합니다 (PDF 렌더링 엔진). `msedge` 를 PATH 에서 먼저 찾고, 없으면 기본 설치 경로(Program Files)를 확인합니다. 둘 다 없으면 안내 메시지와 함께 멈춥니다.
- 한 번에 모든 코스(000·001·002·999)의 워크시트를 빌드합니다.

## templates/

새 워크시트의 출발점입니다. 복사해서 채운 뒤 해당 코스의 `worksheets/` 에 넣고 빌드하면 됩니다.

- `week-template.md` — 주차별 일반 워크시트 (Predict · Spot the Bug · Build · Record · Submit)
- `vocab-template.md` — 단어 연습 워크시트 (단어 · 쉬운 영어 뜻 · 짧은 예문 · 직접 문장 쓰기)

## 월드 생성 스크립트 (선생님 전용)

각 코스의 `worlds/` 안에 있는 `_gen_*.py` · `_builder_*.py` · `_*_lib.py` 는 마인크래프트 월드를 만드는 **선생님 전용** 스크립트입니다. `.gitignore` 로 git 에서 제외되어 학부모·학생에게 노출되지 않습니다. 최종 산출물인 `.mcworld` 파일만 배포됩니다.
