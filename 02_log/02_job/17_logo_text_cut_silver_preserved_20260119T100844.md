# 작업 로그: 로고 하단 텍스트 크롭 제거 및 실버 색상 보존

## 작업 일시
- 2026-01-19T100844

## 수정 내용
- `03_script/06_generate_logo_assets.py`의 `main()` 함수에 **CUT 함수** 추가
- `_apply_circle_alpha()` 함수의 흰색 임계값 조정으로 실버 색상 보존

### 변경 사항

1. **Pass 3 추가 (텍스트 영역 크롭 제거)**:
   - 파란 원의 하단 경계(`y1_blue`)를 감지
   - `crop2.crop((0, 0, crop2.size[0], y1_blue + int(crop2.size[1] * 0.05)))`로 하단 텍스트("HUMAN RESEARCH") 영역을 크롭으로 제거
   - 파란 원 하단에 5% 패딩만 유지하여 텍스트 완전 제거

2. **실버 색상 보존을 위한 흰색 임계값 조정**:
   - 기존: `(r > 240) & (g > 240) & (b > 240)` - 실버가 흰색으로 변하는 문제 발생
   - 수정: `(r > 245) & (g > 245) & (b > 245)` - 순수 흰색만 투명 처리하여 실버(180-220 범위) 보존

## 결과
- `logo-mark.png` 및 `favicon.png` 재생성 완료
- 하단 텍스트("HUMAN RESEARCH")가 크롭으로 완전히 제거됨
- 실버 가젤 색상이 원본 그대로 보존됨 (흰색으로 변하지 않음)
- 파란 원과 실버 가젤만 정확히 보존된 깔끔한 로고 마크 생성

## 변경 파일
- 수정: `03_script/06_generate_logo_assets.py`
- 재생성: `public/images/logo-mark.png`
- 재생성: `public/images/favicon.png`
