# HUMMAN RESEARCH 홈페이지 개발 계획

## 프로젝트 목표
HUMMAN RESEARCH 회사의 공식 웹 홈페이지를 다음 기준으로 제작:
1. **1순위**: 명함 디자인(Name-card.png) - 색상, 로고, 브랜드 아이덴티티
2. **2순위**: activetheory.net 레이아웃 - 레이아웃 구조, 인터랙션, 모션 효과

## 개발 단계별 계획

### Phase 1: 환경 설정 및 디자인 분석 ✅
- [x] 프로젝트 폴더 구조 생성
- [x] Cursor rules 적용
- [x] requirements.txt 생성 및 설치
- [x] Name-card.png를 01_data 폴더로 이동
- [x] 디자인 계획 문서 작성
- [x] 명함 이미지에서 정확한 색상 코드 추출 (Python 스크립트 사용)
  - `03_script/01_extract_colors.py` 작성 및 실행 완료
  - `01_data/color_palette.json` 생성 완료

### Phase 2: 디자인 시스템 구축 ✅ (문서화 완료)
- [x] 색상 팔레트 정확히 정의 (`04_layout/01_design_guide.md`에 문서화)
  - 로얄/코발트 블루 HEX 코드: `#1E3A8A` (또는 명함에서 추출한 색상)
  - 실버/메탈릭 그레이 HEX 코드: `#C0C0C0` (또는 명함에서 추출한 색상)
  - 그라데이션 및 효과 색상 정의
- [x] CSS 변수 정의 (`public/css/variables.css` 작성 완료)
- [x] 타이포그래피 시스템 구축 (`04_layout/01_design_guide.md`에 문서화)
  - 폰트 선택 및 적용: Sans-serif ('Inter', 'Roboto', 'Open Sans' 추천)
  - 폰트 크기 스케일 정의: H1(48-64px), H2(32-40px), H3(24-28px), Body(16-18px), Small(14px)
- [x] 메탈릭 효과 CSS 구현 (`04_layout/01_design_guide.md`에 문서화)
  - 엠보스/디보스 효과: CSS 예시 포함
  - 그라데이션 및 그림자: CSS 예시 포함

### Phase 3: HTML 구조 설계 ✅
- [x] 기본 HTML5 구조 작성 (`public/index.html`)
- [x] 섹션별 구조 설계 (activetheory.net 레이아웃 참고)
  - **Header/Navigation** (activetheory.net 스타일)
    - 햄버거 메뉴 버튼 (왼쪽 상단)
    - 슬라이딩 오버레이 메뉴 구조
    - 로고 배치
  - **Hero Section** (activetheory.net 스타일 + 명함 색상)
    - 대형 비주얼 영역
    - 미니멀 텍스트 레이아웃
    - 그라디언트 조명 효과 영역
  - **About Section** (회사 소개) - 명함 디자인 우선
  - **Services Section** (서비스 소개) - activetheory.net 스타일
    - 전체 화면 이미지 중심 레이아웃
    - 최소한의 텍스트 설명
  - **Contact Section** (연락처) - 명함 디자인 우선
  - **Footer** - 명함 디자인 우선
- [x] 시맨틱 HTML 적용
  - `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>` 사용
  - ARIA 레이블 및 역할 속성 적용
  - 접근성 고려 (skip link, aria-label 등)
- [x] 메타 태그 및 SEO 기본 설정
  - 기본 메타 태그 (charset, viewport, description, keywords)
  - Open Graph 태그 (Facebook)
  - Twitter Card 태그
  - Favicon 링크
  - 폰트 preconnect

### Phase 4: CSS 스타일링 ✅
- [x] Reset/Normalize CSS 적용 (`public/css/style.css`)
- [x] 레이아웃 시스템 구축 (Grid/Flexbox)
  - Grid 레이아웃: About, Contact, Footer 섹션
  - Flexbox 레이아웃: Navigation, Hero, 컴포넌트
- [x] 반응형 디자인 구현
  - Mobile First 접근
  - Breakpoints 정의 (768px, 1024px, 1280px)
  - 반응형 타이포그래피 (clamp() 사용)
- [x] 섹션별 스타일링
  - **Header/Navigation 스타일** (activetheory.net 스타일)
    - 햄버거 메뉴 스타일 (애니메이션 포함)
    - 슬라이딩 오버레이 메뉴 스타일
    - 명함 색상 적용
  - **Hero Section 스타일** (activetheory.net + 명함)
    - 명함 블루 배경 + 그라디언트 조명 효과
    - 메탈릭 효과 (명함 기반)
    - 대형 비주얼 영역 스타일
    - 스크롤 인디케이터 애니메이션
  - **About Section 스타일** (명함 디자인 우선)
    - 카드 스타일
    - 메탈릭 효과 아이콘
  - **Services Section 스타일** (activetheory.net 스타일)
    - 전체 화면 이미지 스타일 (100vh)
    - 오버레이 효과
    - 미니멀 텍스트 스타일
  - **Contact Section 스타일** (명함 디자인 우선)
    - 연락처 정보 카드
    - 폼 스타일
  - **Footer 스타일** (명함 디자인 우선)
    - 블루 배경
    - 브랜드 정보
- [x] 컴포넌트 스타일
  - 버튼 스타일 (Primary, Secondary)
  - 카드 스타일 (호버 효과 포함)
  - 로고 스타일 (메탈릭 효과)
- [x] 접근성 고려
  - Focus 스타일
  - Reduced motion 지원
  - Skip link 스타일

### Phase 5: 로고 및 이미지 처리 ✅
- [x] 로고 이미지 준비
  - SVG 형식으로 재현 완료
    - `logo.svg`: 일반 로고 (200x200px)
    - `logo-circle.svg`: 원형 로고 (히어로 섹션용, 200x200px)
    - `favicon.svg`: 파비콘 (64x64px)
  - 반응형 로고 구현 (SVG이므로 자동 반응형)
  - 명함 디자인 기반: 원형 블루 배경, 실버 메탈릭 영양/가젤 머리, 엠보스/디보스 효과
- [x] 이미지 최적화 가이드 작성
  - 이미지 최적화 가이드 문서 작성 (`06_docs/02_image_optimization_guide.md`)
  - 서비스 이미지, SEO 이미지 가이드 포함
  - 최적화 도구 및 방법 안내
- [x] 아이콘 준비
  - 로고에 포함된 아이콘 요소 (영양/가젤 머리)
  - 메탈릭 효과 적용
- [ ] 실제 서비스 이미지 추가 (사용자 제공 필요)
- [ ] SEO 이미지 생성 (og-image.jpg, twitter-image.jpg)
- [ ] Favicon PNG 생성 (SVG fallback)

### Phase 6: JavaScript 기능 구현
- [ ] **명함 기반 인터랙션** (1순위)
  - 메탈릭 효과 인터랙션
  - 호버 효과
- [ ] **activetheory.net 스타일 인터랙션** (2순위)
  - 스무스 스크롤
  - 슬라이딩 메뉴 오버레이 애니메이션
  - 햄버거 메뉴 토글 기능
  - 마우스 따라 움직이는 효과 (선택적, CSS 기반 우선)
  - 파라랙스 스크롤 효과
  - 호버 시 미세한 움직임
- [ ] 반응형 메뉴 (모바일)
- [ ] 이미지 lazy loading

### Phase 7: 반응형 디자인 최적화
- [ ] 모바일 디바이스 테스트
- [ ] 태블릿 디바이스 테스트
- [ ] 데스크톱 디바이스 테스트
- [ ] 브라우저 호환성 테스트
- [ ] 성능 최적화

### Phase 8: 최종 검토 및 배포 준비
- [ ] 코드 리뷰 및 정리
- [ ] 접근성 검토 (WCAG 가이드라인)
- [ ] SEO 최적화
- [ ] 파일 구조 정리
- [ ] 배포 준비

## 기술 스택

### Frontend
- HTML5
- CSS3 (Variables, Grid, Flexbox, Animations, 3D Transforms)
- JavaScript (Vanilla JS)
  - 인터랙션 및 애니메이션 제어
  - 메뉴 오버레이 제어
  - 스크롤 이벤트 처리
  - 선택적: WebGL/Three.js (고급 시각 효과, 성능 고려)

### 개발 도구
- Python (이미지 처리 및 색상 추출)
- Pillow (이미지 처리)
- scikit-image (색상 분석)
- numpy (이미지 분석)

### 개발 환경
- 로컬 개발 서버 (Python http.server 또는 Live Server)

## 파일 구조 계획

```
Webpage_HR/
├── 01_data/
│   └── Name-card.png
├── 02_log/
│   ├── 01_chat/
│   └── 02_job/
├── 03_script/
│   └── (색상 추출 스크립트 등)
├── 04_layout/
│   └── (디자인 문서)
├── 05_plan/
│   └── (계획 문서)
├── 06_docs/
│   └── (기타 문서)
├── public/              # 웹사이트 파일 (생성 예정)
│   ├── index.html
│   ├── css/
│   │   ├── style.css
│   │   └── variables.css
│   ├── js/
│   │   └── main.js
│   ├── images/
│   │   └── logo.svg
│   └── assets/
├── requirements.txt
└── venv/
```

## 디자인 원칙

### 색상 (명함 디자인 우선 - 1순위)
- **Primary**: 로얄/코발트 블루 (명함에서 추출)
- **Secondary**: 실버/메탈릭 그레이
- **Neutral**: 흰색, 검은색
- **활용**: activetheory.net 스타일의 그라디언트 조명 효과에 명함 색상 적용

### 레이아웃 (activetheory.net 참고 - 2순위)
- **명함 기반**: 미니멀리즘, 대칭성 및 균형
- **activetheory.net 스타일**: 
  - 대형 이미지 중심 레이아웃
  - 네거티브 스페이스 활용
  - 전체 화면 섹션
- 명확한 계층 구조
- 충분한 여백

### 타이포그래피 (명함 + activetheory.net)
- Sans-serif 폰트 (명함과 일치)
- 회사명: 대문자 (명함 스타일)
- 평평하고 모던한 조합 (activetheory.net 스타일)
- 명확한 크기 계층

### 효과
- **명함 기반 효과** (1순위)
  - 메탈릭 엠보스/디보스 효과
  - 명함 색상 기반 그라데이션
- **activetheory.net 스타일 효과** (2순위)
  - 부드러운 전환 애니메이션
  - 마우스 따라 움직이는 효과 (선택적)
  - 파라랙스 스크롤 효과
  - 호버 시 미세한 움직임
  - 슬라이딩 메뉴 애니메이션

## 다음 작업 (우선순위)

1. **즉시 시작**: 색상 추출 스크립트 작성 및 실행
2. **HTML 기본 구조**: index.html 작성
3. **CSS 변수 정의**: 색상 팔레트 및 기본 스타일
4. **로고 처리**: SVG 로고 준비 또는 이미지 최적화

## 예상 소요 시간
- Phase 1: 완료 ✅
- Phase 2-3: 2-3일
- Phase 4-5: 3-4일
- Phase 6-7: 2-3일
- Phase 8: 1일
- **총 예상 기간**: 8-11일

## 참고 사항

### 디자인 우선순위
1. **명함 디자인 (1순위)**: 색상, 로고, 브랜드 아이덴티티, 메탈릭 효과
2. **activetheory.net 레이아웃 (2순위)**: 레이아웃 구조, 인터랙션, 모션 효과

### 구현 원칙
- 명함 디자인의 색상과 형태를 정확히 반영 (최우선)
- activetheory.net의 레이아웃 스타일을 참고하되, 명함 색상과 브랜드 아이덴티티 우선
- 브랜드 일관성 유지
- 반응형 디자인 필수
- 접근성 고려
- 성능 최적화 (WebGL 효과는 선택적 적용)
- 모바일 우선 접근
