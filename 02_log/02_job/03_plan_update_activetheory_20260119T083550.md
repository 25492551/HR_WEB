# 계획 문서 업데이트 작업 로그

## 작업 일시
2026-01-19T083550

## 작업 내용
activetheory.net 레이아웃을 참고하여 모든 계획 문서 업데이트
- 명함 디자인: 1순위 (색상, 로고, 브랜드 아이덴티티)
- activetheory.net: 2순위 (레이아웃, 인터랙션, 모션 효과)

## 수행 작업

### 1. activetheory.net 레이아웃 분석
주요 특징 파악:
- 인터랙티브한 마우스 따라 움직이는 효과 (Fractured glass effect)
- 어두운 배경 + 그라디언트 조명 효과
- 햄버거 메뉴 + 슬라이딩 메뉴 오버레이
- 대형 이미지 중심 콘텐츠, 미니멀 텍스트
- 산세리프 폰트, 평평하고 모던한 조합
- 움직임 및 모션 효과 강조 (파라랙스, 호버)

### 2. 계획 문서 업데이트

#### `05_plan/01_homepage_design_plan.md` 업데이트
- 디자인 기준에 우선순위 명시 (명함 1순위, activetheory.net 2순위)
- activetheory.net 레이아웃 참고 요소 섹션 추가
- 구현 계획에 activetheory.net 스타일 반영:
  - 헤더/네비게이션: 햄버거 메뉴 + 슬라이딩 오버레이
  - 히어로 섹션: 그라디언트 조명 효과 (명함 색상 적용)
  - 서비스 섹션: 전체 화면 이미지 중심
- 기술 스택에 WebGL/Three.js 선택적 적용 추가

#### `05_plan/02_homepage_development_plan.md` 업데이트
- 프로젝트 목표에 우선순위 명시
- Phase 3 (HTML 구조): activetheory.net 스타일 레이아웃 반영
  - 햄버거 메뉴 구조
  - 슬라이딩 오버레이 메뉴
  - 대형 비주얼 히어로 섹션
- Phase 4 (CSS 스타일링): activetheory.net 스타일 적용
- Phase 6 (JavaScript): activetheory.net 스타일 인터랙션 추가
  - 슬라이딩 메뉴 애니메이션
  - 마우스 따라 움직이는 효과 (선택적)
  - 파라랙스 스크롤 효과
- 기술 스택에 WebGL/Three.js 선택적 추가
- 디자인 원칙 섹션에 우선순위 및 activetheory.net 스타일 반영

#### `04_layout/01_design_guide.md` 업데이트
- 디자인 기준 우선순위 명시
- 레이아웃 원칙에 activetheory.net 스타일 추가
- 컴포넌트 스타일에 네비게이션 및 히어로 섹션 가이드 추가

## 통합 디자인 방향

### 명함 디자인 (1순위) 적용 영역
- 색상 팔레트 (로얄/코발트 블루, 실버/메탈릭 그레이)
- 로고 및 브랜드 아이덴티티
- 메탈릭 엠보스/디보스 효과
- 타이포그래피 (산세리프, 대문자)
- About, Contact, Footer 섹션

### activetheory.net 스타일 (2순위) 적용 영역
- 레이아웃 구조 (햄버거 메뉴, 슬라이딩 오버레이)
- 히어로 섹션 (그라디언트 조명 효과 - 명함 색상 적용)
- 서비스 섹션 (전체 화면 이미지 중심)
- 인터랙션 및 모션 효과
- 네비게이션 구조

## 업데이트된 파일
- `05_plan/01_homepage_design_plan.md`
- `05_plan/02_homepage_development_plan.md`
- `04_layout/01_design_guide.md`
- `02_log/02_job/03_plan_update_activetheory_20260119T083550.md` (본 문서)

## 다음 단계
1. HTML 기본 구조 작성 (activetheory.net 스타일 레이아웃)
2. CSS 변수 정의 (명함 색상 팔레트)
3. 네비게이션 구조 구현 (햄버거 메뉴 + 슬라이딩 오버레이)
4. 히어로 섹션 구현 (명함 색상 + 그라디언트 조명 효과)
