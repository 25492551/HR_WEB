## 작업 개요
- HUMMAN RESEARCH 홈페이지의 Phase 6(자바스크립트 인터랙션) 및 Phase 6-1(콘텐츠 연결) 항목을 실제 코드에 반영했다.
- CTA는 **텍스트만 유지**하고, **클릭 동작은 의도적으로 비활성화**했다(요청사항).

## 적용 내용
- **명함 기반 인터랙션**
  - 카드에 마우스 위치 기반 메탈릭 광원(shine) 효과 추가
  - 카드 틸트(미세 3D 기울기) 및 호버 시 콘텐츠(hover copy) 노출
- **activetheory.net 스타일 인터랙션**
  - 앵커 기반 스무스 스크롤(접근성/Reduced motion 고려)
  - 햄버거 메뉴 토글 + 오버레이 메뉴 열림/닫힘(ESC/리사이즈 대응)
  - 간단 파라랙스(데이터 속성 기반)
  - 포인터 추적 CSS 변수(`--pointer-x`, `--pointer-y`) 갱신
- **반응형 메뉴(모바일)**
  - 오버레이 메뉴에서 링크 클릭 시 닫힘
  - 데스크톱 폭(1024px 이상) 전환 시 안전하게 닫힘
- **이미지 Lazy Loading**
  - 이미지 기본 `decoding="async"`, `loading="lazy"` 적용(상단 로고는 eager)

## 콘텐츠/구조 정리
- End 섹션을 플랜 기준으로 조정: **로고 제거**, **하단 고정 메시지** 형태로 반영
- 누락되던 로고 파일 추가 및 경로 정리

## 변경 파일
- `public/index.html`
- `public/css/style.css`
- `public/js/main.js` (신규)
- `public/images/logo.svg` (신규)
- `05_plan/02_homepage_development_plan.md` (체크리스트 완료 표시)

## 비고
- CTA는 현재 단계에서 동작을 연결하지 않음(클릭 시 `preventDefault()` 처리).
