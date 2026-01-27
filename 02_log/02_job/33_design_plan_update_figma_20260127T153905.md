# Design Plan Update - Figma 디자인 반영

**작업 일시**: 2026-01-27T153905  
**작업 내용**: Figma 디자인을 참고하여 `01_homepage_design_plan.md` 업데이트

## 작업 개요

사용자가 Figma 디자인 링크를 제공하고, 디자인 계획 문서를 업데이트하도록 요청했습니다.
주요 변경사항:
1. End 섹션에서 로고 제거 (Figma 디자인 기준)
2. Figma 자산 활용 계획 추가
3. 섹션별 디자인에 Figma 자산 매핑

## 작업 내용

### 1. MAIN 구조 업데이트
- **변경 전**: `7. **End**: LOGO + 하단 고정 메시지`
- **변경 후**: `7. **End**: 하단 고정 메시지 (로고 없음)`
- Figma 디자인 기준으로 End 섹션에 로고가 포함되지 않음을 명시

### 2. 콘텐츠 소스 반영 섹션 업데이트
- Values & Footer Message 섹션에 End 섹션 로고 제외 명시
- 하단 고정 메시지 텍스트 정확히 반영:
  - "This is not about adding motivation. It is about designing systems where movement activates it."

### 3. 섹션별 디자인 업데이트
각 섹션에 Figma 자산 매핑 추가:

- **Start**: `HUMMAN RESEARCH.svg` 사용
- **Hero**: 
  - `RECODING YOUR VITALITY.svg` (메인 타이틀)
  - `THE FUTURE OF ENDOGENOUS LIPID SIGNALING.svg` (섹션 타이틀)
- **Contents 1**: 
  - `SCIENCE.svg`, `PLATFORM.svg`, `R&D.svg`, `EXPERIENCE.svg` (태그)
- **Values**: Figma 자산의 설명 텍스트 이미지 활용
- **End**: 로고 없음, 메시지만 표시

### 4. Figma 자산 활용 계획 섹션 추가
새로운 섹션 추가:
- 이미지 자산 위치: `public/images/figma/` 폴더
- 주요 자산 활용 가이드
- 자산 사용 원칙 (SVG 우선, PNG 선택적)

## 변경된 파일

- `05_plan/01_homepage_design_plan.md` - 디자인 계획 문서 업데이트

## 참고 사항

- Figma 디자인 링크: https://www.figma.com/design/bhZp6s1IGjzeTuYV7UQbTs/바이오_랜딩페이지?node-id=0-1
- 모든 Figma 자산은 `public/images/figma/` 폴더에 저장됨 (91개 파일)
- End 섹션은 로고 없이 메시지만 표시하는 미니멀한 디자인

## 다음 단계

1. HTML/CSS에서 End 섹션의 로고 제거
2. Figma 자산을 실제 HTML/CSS에 적용
3. 섹션별 이미지 자산 매핑 확인 및 적용
