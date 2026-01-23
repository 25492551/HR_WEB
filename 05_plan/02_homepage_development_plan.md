# HUMMAN RESEARCH 홈페이지 개발 계획

## 프로젝트 목표
HUMMAN RESEARCH 회사의 공식 웹 홈페이지를 다음 기준으로 제작:
1. **1순위**: 명함 디자인(Name-card.png) - 색상, 텍스처, 브랜드 아이덴티티
2. **2순위**: activetheory.net 레이아웃 - 웹페이지 맵/구조 기준

## MAIN 구조 (웹페이지 맵)
1. **Start**: LOGO
2. **Hero**: Main Headline / Subheadline / Section Title / Tech Tags
3. **Core Concept**: Exercise Is the Switch + 인용 문구
4. **Contents 1**: CARD 01~04 (SCIENCE / PLATFORM / R&D / EXPERIENCE)
   - Tag, One-liner, Hover copy, CTA
5. **Contents 2**: 상세 섹션
   - Science / Peripheral / Central 상세 정보
   - Research Updates 안내
6. **Values**: Purity & Identity / Stability by Design / Automation Mindset
7. **End**: LOGO + 하단 고정 메시지

## 콘텐츠 구조 (01_website_contents.md 기반)
1. **Hero**
   - Main Headline / Subheadline / Section Title / Tech Tags
2. **Core Concept**
   - Exercise Is the Switch + 인용 문구
3. **CARD 01: NAE Platform (SCIENCE)**
   - One-liner / Hover copy / CTA / 상세 개념
4. **CARD 02: Peripheral NAE Platform (PLATFORM)**
   - One-liner / Hover copy / CTA / 상세 개념
5. **CARD 03: Central NAE Research (R&D)**
   - One-liner / Hover copy / CTA / 상세 개념
6. **CARD 04: Training Motivation System (EXPERIENCE)**
   - One-liner / Hover copy / CTA
7. **Values + Footer Message**
   - Purity & Identity / Stability by Design / Automation Mindset
   - 하단 고정 메시지

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
- [x] 섹션별 구조 설계 (activetheory.net 레이아웃 + MAIN 구조 반영)
  - **Start: LOGO**
  - **Hero**: Main Headline / Subheadline / Section Title / Tech Tags
  - **Core Concept**: Exercise Is the Switch + 인용 문구
  - **Contents 1: CARD 01~04** (SCIENCE / PLATFORM / R&D / EXPERIENCE)
    - Tag, One-liner, Hover copy, CTA
  - **Contents 2: 상세 섹션**
    - Science / Peripheral / Central 상세 정보
    - Research Updates 안내
  - **Values**: Purity & Identity / Stability by Design / Automation Mindset
  - **End: LOGO + 하단 고정 메시지**
- [x] 01_website_contents.md 기준 섹션/카피 반영
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
  - **Start: LOGO 스타일** (명함 디자인 우선)
    - 로고 중앙 배치
    - 메탈릭 효과
  - **Hero Section 스타일** (activetheory.net + 명함)
    - 명함 블루 배경 + 그라디언트 조명 효과
    - 메탈릭 효과 (명함 기반)
    - 대형 비주얼 영역 스타일
    - Main Headline / Subheadline / Section Title / Tech Tags 스타일
    - 스크롤 인디케이터 애니메이션
  - **Core Concept Section 스타일** (명함 디자인 우선)
    - 인용 문구 강조 스타일
    - 메탈릭 효과 적용
  - **Contents 1: CARD 01~04 스타일** (명함 디자인 우선)
    - 카드형 레이아웃 (Grid/Flexbox)
    - Tag / One-liner / Hover copy / CTA 스타일
    - 호버 효과 및 메탈릭 효과
  - **Contents 2: 상세 섹션 스타일** (activetheory.net 스타일)
    - Science / Peripheral / Central 상세 정보 레이아웃
    - 전체 화면 또는 섹션별 스타일
    - 미니멀 텍스트 스타일
  - **Values Section 스타일** (명함 디자인 우선)
    - Purity & Identity / Stability by Design / Automation Mindset 카드 스타일
  - **End: LOGO + Footer 스타일** (명함 디자인 우선)
    - 로고 중앙 배치
    - 블루 배경
    - 하단 고정 메시지 스타일
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
- [x] 사용자 제작 로고/이미지 적용
  - Illustrator 원본: `public/ai.ai`
  - SVG 원본: `public/svg.svg`
  - 로고/아이콘은 위 파일을 기준으로 사용 및 파생
  - 반응형 사용 시 SVG 기준으로 스케일
- [x] 이미지 최적화 가이드 작성
  - 이미지 최적화 가이드 문서 작성 (`06_docs/02_image_optimization_guide.md`)
  - 서비스 이미지, SEO 이미지 가이드 포함
  - 최적화 도구 및 방법 안내
- [x] 아이콘 준비
  - 로고에 포함된 아이콘 요소 (영양/가젤 머리)
  - 메탈릭 효과 적용
- [ ] 실제 서비스 이미지 추가 (사용자 제공 필요)
- [ ] SEO 이미지 생성 (og-image.jpg, twitter-image.jpg)
- [x] Favicon PNG 생성 (SVG fallback) - Placeholder 생성 완료, 실제 로고 변환 필요

### Phase 5-1: 움직이는 그래픽 자산 준비 (사용자 직접 제작)
activetheory.net 스타일의 인터랙티브 효과를 위한 그래픽 자산이 필요합니다.

#### 필요한 그래픽 자산 및 형식

**1. 배경 텍스처/패턴 (Background Textures)**
- **용도**: Hero 섹션, 배경 레이어
- **형식**: 
  - **PNG** (투명도 지원, 1920x1080px 이상 권장)
  - **WebP** (최적화된 버전, 투명도 지원)
  - **SVG** (벡터 패턴, 확장 가능)
- **파일명**: `bg-texture-*.png`, `bg-pattern-*.svg`
- **위치**: `public/images/backgrounds/`
- **요구사항**:
  - 명함 색상 팔레트 사용 (#1E3A8A 블루, #C0C0C0 실버)
  - 미니멀하고 추상적인 패턴
  - 그라디언트 조명 효과와 조화

**2. 파라랙스 레이어 (Parallax Layers)**
- **용도**: 스크롤 시 다른 속도로 움직이는 레이어
- **형식**: 
  - **PNG** (투명 배경, 1920x1080px 이상)
  - **SVG** (벡터 요소, 확장 가능)
- **파일명**: `parallax-layer-01.png`, `parallax-layer-02.png`, `parallax-layer-03.png`
- **위치**: `public/images/parallax/`
- **요구사항**:
  - 최소 3개 레이어 (전경, 중경, 배경)
  - 각 레이어는 독립적으로 움직임
  - 명함 디자인과 조화되는 추상적 형태
  - 투명도 활용 가능

**3. 마우스 인터랙션 그래픽 (Mouse Interaction Graphics)**
- **용도**: 마우스 따라 움직이는 효과 (Fractured glass effect)
- **형식**: 
  - **SVG** (벡터, 실시간 변형 가능, 권장)
  - **PNG** (비트맵, 투명도, 512x512px 이상)
- **파일명**: `interaction-glass.svg`, `interaction-shard-*.svg`
- **위치**: `public/images/interactions/`
- **요구사항**:
  - 유리 파편/조각 형태의 추상적 그래픽
  - 개별 요소로 분리 가능 (여러 조각)
  - 투명도와 반사 효과 표현
  - JavaScript로 위치/회전 제어 가능한 구조

**4. WebGL/Shader 텍스처 (선택적, 고급 효과)**
- **용도**: Three.js 또는 WebGL 기반 고급 시각 효과
- **형식**: 
  - **PNG** (512x512px 또는 1024x1024px, 타일링 가능)
  - **EXR/HDR** (고해상도 조명 맵, 선택적)
- **파일명**: `webgl-noise.png`, `webgl-gradient.png`
- **위치**: `public/images/webgl/`
- **요구사항**:
  - 노이즈 텍스처 (프로시저럴 생성 가능)
  - 그라디언트 맵
  - 명함 색상 기반

**5. 애니메이션용 스프라이트 시트 (선택적)**
- **용도**: CSS/JavaScript 애니메이션
- **형식**: 
  - **PNG** (스프라이트 시트, 프레임별 정렬)
  - **SVG** (개별 프레임, CSS 애니메이션)
- **파일명**: `sprite-animation-*.png`
- **위치**: `public/images/sprites/`
- **요구사항**:
  - 프레임별로 정렬된 스프라이트
  - 각 프레임 크기 동일
  - 투명 배경

**6. 섹션별 배경 이미지**
- **용도**: Contents 1, Contents 2 섹션 배경
- **형식**: 
  - **PNG/WebP** (1920x1080px 이상, 전체 화면)
  - **SVG** (벡터 배경, 확장 가능)
- **파일명**: `section-hero-bg.png`, `section-cards-bg.png`
- **위치**: `public/images/sections/`
- **요구사항**:
  - activetheory.net 스타일의 미니멀 배경
  - 명함 색상 팔레트
  - 텍스트 가독성 고려

#### 제작 가이드라인

**색상 팔레트 (명함 기반)**
- Primary Blue: `#1E3A8A` 또는 `#2565B2`
- Metallic Silver: `#C0C0C0` 또는 `#B9BBBC`
- Light Gray: `#EFEFF1`
- Background: `#FFFFFF` 또는 `#000000` (섹션별)

**스타일 원칙**
- 미니멀리즘: 불필요한 디테일 제거
- 추상적 형태: 기하학적 패턴, 유기적 흐름
- 메탈릭 효과: 반사, 그라디언트, 엠보스/디보스
- 명함 디자인과의 조화

**기술적 요구사항**
- 투명도 활용 (PNG alpha channel)
- 확장 가능성 (SVG 우선)
- 최적화된 파일 크기 (WebP 변환 권장)
- 반응형 대응 (다양한 해상도)

#### 파일 구조
```
public/images/
├── backgrounds/
│   ├── bg-texture-hero.png
│   ├── bg-pattern-abstract.svg
│   └── bg-gradient-overlay.png
├── parallax/
│   ├── parallax-layer-01.png (전경)
│   ├── parallax-layer-02.png (중경)
│   └── parallax-layer-03.png (배경)
├── interactions/
│   ├── interaction-glass.svg
│   ├── interaction-shard-01.svg
│   └── interaction-shard-02.svg
├── webgl/ (선택적)
│   ├── webgl-noise.png
│   └── webgl-gradient.png
├── sprites/ (선택적)
│   └── sprite-animation-*.png
└── sections/
    ├── section-hero-bg.png
    └── section-cards-bg.png
```

#### 우선순위
1. **필수**: 배경 텍스처, 파라랙스 레이어 (최소 2개)
2. **권장**: 마우스 인터랙션 그래픽
3. **선택적**: WebGL 텍스처, 스프라이트 시트

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

### Phase 6-1: 콘텐츠 연결
- [ ] **Start: LOGO** 섹션 구현
- [ ] **Hero** 섹션 카피 삽입
  - Main Headline: RECODING YOUR VITALITY
  - Subheadline / Section Title / Description / Tech Tags
- [ ] **Core Concept** 섹션 카피 삽입
  - Exercise Is the Switch + 인용 문구
- [ ] **Contents 1: CARD 01~04** 섹션 카피 삽입
  - CARD 01: NAE Platform (SCIENCE) - Tag, One-liner, Hover copy, CTA
  - CARD 02: Peripheral NAE Platform (PLATFORM) - Tag, One-liner, Hover copy, CTA
  - CARD 03: Central NAE Research (R&D) - Tag, One-liner, Hover copy, CTA
  - CARD 04: Training Motivation System (EXPERIENCE) - Tag, One-liner, Hover copy, CTA
- [ ] **Contents 2: 상세 섹션** 카피 삽입
  - Science Page: What are NAEs? / Why exercise matters / Research Updates 안내
  - Peripheral NAE Platform: Scope / Overview / Included Research Concepts
  - Central NAE Research: Scope / Overview / Active Research Areas
- [ ] **Values** 섹션 카피 삽입
  - Purity & Identity / Stability by Design / Automation Mindset
- [ ] **End: LOGO + 하단 고정 메시지** 적용
- [ ] CTA 링크/버튼 텍스트 반영

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
HR_WEB-main/
├── .cursorrules
├── .gitignore
├── requirements.txt
├── 01_data/                          # 데이터 파일 (사용자 추가)
│   ├── 00_NAE_synthesis_automation_guide.md
│   ├── 01_website_contents.md
│   ├── ai.ai
│   ├── color_palette.json
│   ├── Name-card.png
│   ├── svg.svg
│   └── website contents.docx
├── 02_log/                           # 로그 파일
│   └── 02_job/                        # 작업 로그
│       └── (작업 로그 파일들)
├── 03_script/                        # 스크립트 파일
│   ├── 01_extract_colors.py
│   ├── 02_column_automation_analysis.py
│   ├── 03_korea_vendor_analysis.py
│   └── 04_nae_synthesis_analysis.py
├── 04_layout/                        # 디자인 문서 및 레이아웃
│   └── 01_design_guide.md
├── 05_plan/                          # 계획 문서
│   ├── 01_homepage_design_plan.md
│   └── 02_homepage_development_plan.md
├── 06_docs/                          # 기타 문서
│   └── 01_project_info.md
└── public/                            # 웹사이트 파일
    ├── index.html
    ├── css/
    │   ├── style.css
    │   └── variables.css
    ├── js/                            # JavaScript 파일 (생성 예정)
    │   └── main.js
    ├── images/
    │   ├── ai.ai
    │   ├── README.md
    │   └── svg.svg
    └── assets/                        # 추가 에셋 (생성 예정)
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
