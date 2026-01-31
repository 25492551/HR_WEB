# 작업 로그: 가젤 뿔 정점(vertex) 누락 문제 수정

## 작업 일시
- 2026-01-19T095049

## 문제
- `public/images/logo-mark.png`에서 가젤 뿔의 끝 부분(정점/vertex)이 원형 마스크 가장자리에서 잘려 보이지 않는 문제 발생

## 원인 분석
- 크롭 시 패딩 비율(`pad_ratio`)이 0.01로 너무 작아서 뿔 끝이 원형 마스크 경계에 가깝게 위치
- 원형 알파 마스크의 인셋(`inset`)이 1%로 설정되어 있어, 뿔 끝이 마스크 경계에서 클리핑됨

## 수정 내용
- `03_script/06_generate_logo_assets.py` 수정:
  - 두 번째 패스의 패딩 비율을 `0.01`에서 `0.03`으로 증가 (뿔 끝까지 포함되도록 여유 공간 확보)
  - 원형 마스크 인셋을 `0.01`에서 `0.005`로 감소 (마스크 경계를 더 넓게 사용)
- `logo-mark.png` 및 `favicon.png` 재생성

## 결과
- 가젤 뿔의 정점(vertex)이 원형 로고 내에서 완전히 보이도록 수정됨
- 로고 마크가 명함 원본과 동일한 형태를 유지하면서도 뿔 끝이 잘리지 않음

## 변경 파일
- 수정: `03_script/06_generate_logo_assets.py`
- 재생성: `public/images/logo-mark.png`
- 재생성: `public/images/favicon.png`
