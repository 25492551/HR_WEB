# 파일 정리 및 서비스 이미지 생성 작업 로그

## 작업 일시
2026-01-19T091201

## 작업 내용
1. 외부에서 가져온 파일들을 적절한 폴더로 이동 및 인덱싱 재정렬
2. 서비스 이미지 생성 스크립트 작성 및 실행

## 수행 작업

### 1. 파일 이동 및 인덱싱 재정렬

#### Python 스크립트 이동 (`03_script/`)
- `column_automation_analysis.py` → `03_script/02_column_automation_analysis.py`
- `korea_vendor_analysis.py` → `03_script/03_korea_vendor_analysis.py`
- `nae_synthesis_analysis.py` → `03_script/04_nae_synthesis_analysis.py`

#### 문서 파일 이동 (`06_docs/`)
- `NAE_Synthesis_Automation_Complete_Guide.md` → `06_docs/03_nae_synthesis_automation_guide.md`

#### 최종 인덱싱 구조
```
03_script/
├── 01_extract_colors.py
├── 02_column_automation_analysis.py
├── 03_korea_vendor_analysis.py
├── 04_nae_synthesis_analysis.py
└── 05_generate_service_images.py (새로 생성)

06_docs/
├── 01_project_info.md
├── 02_image_optimization_guide.md
└── 03_nae_synthesis_automation_guide.md
```

### 2. 서비스 이미지 생성 스크립트 작성

#### `03_script/05_generate_service_images.py` 생성
- 분석 스크립트들의 내용을 바탕으로 서비스 이미지 생성
- 명함 디자인 색상 (블루 #1E3A8A) 적용
- 3개의 서비스 이미지 생성:
  1. **Service 1: Research** - Column Automation Analysis
  2. **Service 2: Consulting** - Vendor Analysis
  3. **Service 3: Analysis** - NAE Synthesis Cost-Benefit

#### 이미지 특징
- 배경: 명함 블루 색상 (#1E3A8A)
- 텍스트: 흰색 (#FFFFFF), 실버 (#C0C0C0)
- 크기: 16:9 비율 (1920x1080px 권장)
- 해상도: 150 DPI
- 형식: JPEG

### 3. 의존성 추가
- `requirements.txt`에 pandas, matplotlib 추가
- 패키지 설치 완료

### 4. 서비스 이미지 상세

#### Service 1: Research (service-1.jpg)
- 제목: "RESEARCH - Column Chromatography Automation"
- 내용:
  - 자동화 수준 비교 (Manual, Flash, MPLC)
  - 시간 비교 (시간당 배치)
- 데이터 소스: `02_column_automation_analysis.py`

#### Service 2: Consulting (service-2.jpg)
- 제목: "CONSULTING - Korean Vendor Analysis & Procurement"
- 내용:
  - 벤더 가격 비교 (Biotage Korea, YL Instruments, LabX Used)
  - 평점 표시
- 데이터 소스: `03_korea_vendor_analysis.py`

#### Service 3: Analysis (service-3.jpg)
- 제목: "ANALYSIS - NAE Synthesis Cost-Benefit Analysis"
- 내용:
  - 구매 vs 합성 비용 비교 (5종 NAE)
  - 절약 금액 표시
- 데이터 소스: `04_nae_synthesis_analysis.py`

### 5. 생성된 파일
- `public/images/service-1.jpg` ✅
- `public/images/service-2.jpg` ✅
- `public/images/service-3.jpg` ✅
- `03_script/05_generate_service_images.py` ✅

## 기술적 세부사항

### 이미지 생성 방법
- matplotlib을 사용한 데이터 시각화
- 명함 디자인 색상 팔레트 적용
- activetheory.net 스타일의 미니멀 텍스트 레이아웃

### 스크립트 특징
- 유니코드 인코딩 문제 해결 (Windows cp949 호환)
- matplotlib 스타일 fallback 처리
- 명함 색상 일관성 유지

## 다음 단계
1. 서비스 이미지 최적화 (필요시)
2. HTML에서 이미지 경로 확인
3. 반응형 이미지 설정 (srcset)
4. SEO 이미지 메타 태그 업데이트

## 참고 사항
- 모든 서비스 이미지는 명함 디자인 색상 (#1E3A8A)을 사용
- 분석 스크립트의 실제 데이터를 기반으로 생성
- 웹사이트 서비스 섹션에서 바로 사용 가능
