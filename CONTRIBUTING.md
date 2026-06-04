# 작업 가이드 (CONTRIBUTING)

영어코딩 템플릿 저장소를 관리할 때 지키는 규칙입니다.

## 폴더 구조

코스 하나는 `NNN-코스이름/` 폴더이고, 그 안에 4개의 하위 폴더가 있습니다.

- `worlds/` — 매주 마인크래프트 월드 파일(`.mcworld`)
- `python/` — 파이썬 코드 템플릿
- `blocks/` — 블록 코드 템플릿(`.mkcd`)
- `worksheets/` — 영어 워크시트(`.md` 원본 → `.pdf` 출력본, `_html/` 는 빌드 중간 파일)

`999-extras/` 는 특정 주차에 묶이지 않은 단독 워크시트 모음입니다.

## 파일 이름 규칙

- 주차 파일은 **`weekN`** (하이픈 없음): `week1.mcworld`, `week2.md` …
- 여러 주가 공유하는 월드는 범위로: `week4-5.mcworld`, `week6-7-8.mcworld`
- (구버전 `week-1` 하이픈 표기는 `weekN` 으로 통일했습니다.)

## 새 주차 / 워크시트 추가

1. `scripts/templates/` 에서 알맞은 템플릿을 복사합니다.
   - 일반 워크시트 → `week-template.md`
   - 단어 연습 → `vocab-template.md`
2. 내용을 채워 해당 코스의 `worksheets/weekN.md` 로 저장합니다.
3. `python scripts/build-worksheets.py` 로 PDF를 만듭니다.
4. 코스 `README.md` 표(또는 `999-extras` 목록)에 받기 링크를 추가합니다.

## 언어 규칙

- **학생용**(워크시트 본문) = 영어. 과하게 규정하지 않기, "최소 N개" 같은 강제 표현 금지.
- **학부모용**(코스/폴더 README, 안내문) = 한국어. 브랜드는 "영어코딩".
- 제출은 항상 **온라인 카카오톡**. "수업에 가져오기" 같은 오프라인 표현 금지.

## 커밋

- 학부모가 읽을 수 있는 한국어 커밋 메시지. `feat:` 같은 접두사는 쓰지 않습니다.
- 마이그레이션/SQL 은 한 커밋에 하나의 변경만.

## 선생님 전용 파일

`worlds/_gen_*.py` · `_builder_*.py` · `_*_lib.py` 는 월드 생성기로, `.gitignore` 에 의해 배포에서 제외됩니다. 학생에게는 최종 `.mcworld` 만 전달됩니다.
