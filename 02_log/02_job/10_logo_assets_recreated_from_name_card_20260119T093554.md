# 작업 로그: 로고/파비콘 이미지 재생성 (명함 로고 기준)

## 작업 일시
- 2026-01-19T093554

## 요청 사항
- `public/images/favicon.svg`, `public/images/logo-circle.svg`, `public/images/logo.svg`가 현재 명함 로고와 형태가 달라 “쓸모없다”는 문제 제기
- `01_data/Name-card.png`의 로고와 **동일한 로고**로 다시 생성 요청

## 분석
- 기존 SVG들은 “대략적인” 로우폴리 형태로 재구성되어 있어, 명함의 실제 로고(각진 면 분할/뿔 형태/광택감)와 시각적으로 불일치함
- “완전 동일”을 보장하려면 명함에서 로고 마크를 정확히 추출하여 동일한 마크를 사용하는 방식이 가장 확실함

## 수행 내용
- **명함에서 로고 마크(원형 블루 + 실버 동물 머리) 크롭 추출**
  - `03_script/06_generate_logo_assets.py` 작성(소스인 `01_data/Name-card.png`는 수정하지 않음)
  - 좌측 명함 영역에서 블루 원형 영역을 색상 임계값으로 탐지 → 바운딩 박스 기반으로 크롭 → 원형 알파 마스크 적용
  - 출력:
    - `public/images/logo-mark.png` (512x512)
    - `public/images/favicon.png` (64x64)
- **SVG 3종을 명함 로고 마크 기반으로 교체**
  - `public/images/logo.svg`: `logo-mark.png`를 참조하도록 변경
  - `public/images/logo-circle.svg`: `logo-mark.png`를 참조하도록 변경
  - `public/images/favicon.svg`: `favicon.png`를 참조하도록 변경

## 결과
- 페이지에서 사용하는 로고(`logo.svg`, `logo-circle.svg`)가 명함 로고와 동일한 마크를 사용하도록 정렬됨
- 파비콘 PNG(`favicon.png`)도 생성되어 HTML의 PNG fallback 경로가 실제로 동작 가능해짐

## 변경 파일
- 추가: `03_script/06_generate_logo_assets.py`
- 추가: `public/images/logo-mark.png`
- 추가: `public/images/favicon.png`
- 수정: `public/images/logo.svg`
- 수정: `public/images/logo-circle.svg`
- 수정: `public/images/favicon.svg`

