# 작업 로그: 로고 알파 마스크 단순화 (흰색만 투명 처리)

## 작업 일시
- 2026-01-19T100719

## 문제
- 이전 코드가 실버 가젤을 흰색으로 변환하는 문제 발생
- 복잡한 마스킹 로직으로 인해 실버 색상이 손실됨

## 수정 내용
- `03_script/06_generate_logo_assets.py`의 `_apply_circle_alpha` 함수를 단순화
- **새로운 전략**: 흰색/거의 흰색 픽셀(R, G, B > 240)만 투명 처리
- 나머지 모든 픽셀(파란 원, 실버 가젤, 텍스트 등)은 그대로 유지
- 실버 색상이 손실되지 않도록 보존

## 결과
- `logo-mark.png` 및 `favicon.png` 재생성 완료
- 실버 가젤의 원본 색상이 정확히 보존됨
- 흰색 배경만 투명 처리되어 깔끔한 로고 마크 생성

## 변경 파일
- 수정: `03_script/06_generate_logo_assets.py`
- 재생성: `public/images/logo-mark.png`
- 재생성: `public/images/favicon.png`
