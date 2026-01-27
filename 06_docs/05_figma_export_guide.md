# Figma 디자인에서 이미지 및 코드 가져오기 가이드

## 개요
Figma 디자인 파일에서 이미지와 코드를 가져오는 여러 방법을 안내합니다.

## 방법 1: Figma에서 직접 내보내기 (가장 간단)

### 이미지 내보내기
1. **Figma 웹/앱에서 디자인 열기**
   - 제공된 링크: https://www.figma.com/design/bhZp6s1IGjzeTuYV7UQbTs/바이오_랜딩페이지?node-id=15-6
   
2. **개별 요소 선택 후 내보내기**
   - 내보내고 싶은 프레임/컴포넌트 선택
   - 우측 패널에서 "Export" 섹션 클릭
   - 형식 선택: PNG, JPG, SVG, PDF
   - 해상도 선택: 1x, 2x, 3x
   - "Export [이름]" 버튼 클릭

3. **여러 요소 일괄 내보내기**
   - 여러 프레임/컴포넌트 선택 (Shift + 클릭)
   - 우측 패널에서 "Export" 섹션에서 각각 설정
   - "Export" 버튼 클릭

### 코드 내보내기 (CSS, React, iOS, Android)
1. **개별 요소 선택**
2. **우측 패널에서 "Code" 탭 클릭**
3. **코드 형식 선택**: CSS, React, iOS, Android
4. **코드 복사** 또는 "Copy" 버튼 클릭

### Dev Mode 사용 (고급)
1. **Figma 상단에서 "Dev Mode" 토글 활성화**
2. **요소 선택 시 자동으로 코드 표시**
3. **측정값, 스타일, 레이아웃 정보 확인**

## 방법 2: Figma API 사용 (프로그래밍 방식)

### 사전 준비
1. **Figma Personal Access Token 생성**
   - Figma 계정 설정 > Account Settings > Personal Access Tokens
   - 새 토큰 생성 및 복사 (한 번만 표시됨)

2. **File Key 추출**
   - Figma 파일 URL에서 추출
   - URL 형식: `https://www.figma.com/file/{FILE_KEY}/파일명`
   - 제공된 링크: `bhZp6s1IGjzeTuYV7UQbTs` (File Key)

3. **Node ID 확인**
   - URL의 `node-id` 파라미터에서 확인
   - 제공된 링크: `node-id=15-6` → Node ID: `15:6`

### API 엔드포인트
- **파일 정보 가져오기**: `GET https://api.figma.com/v1/files/{FILE_KEY}`
- **이미지 내보내기**: `GET https://api.figma.com/v1/images/{FILE_KEY}?ids={NODE_ID}&format=png&scale=2`
- **파일 노드 가져오기**: `GET https://api.figma.com/v1/files/{FILE_KEY}/nodes?ids={NODE_ID}`

### Python 스크립트 사용
프로젝트의 `03_script/07_export_figma_assets.py` 스크립트를 사용하세요.

**사용 방법:**
```bash
# 가상 환경 활성화 (Windows)
venv\Scripts\activate

# 스크립트 실행
python 03_script/07_export_figma_assets.py
```

**필수 설정:**
- `.env` 파일에 `FIGMA_ACCESS_TOKEN` 설정
- 스크립트 내에서 File Key와 Node ID 설정

## 방법 3: Figma 플러그인 사용

### 추천 플러그인
1. **Figma to Code**
   - HTML/CSS/React 코드 생성
   - 플러그인 메뉴에서 검색 및 설치

2. **Image Export**
   - 일괄 이미지 내보내기
   - 다양한 형식 및 해상도 지원

3. **Figma to React**
   - React 컴포넌트 자동 생성

### 사용 방법
1. Figma에서 플러그인 메뉴 열기 (Plugins > Browse all plugins)
2. 원하는 플러그인 검색 및 설치
3. 플러그인 실행 후 설정 및 내보내기

## 방법 4: Figma Desktop App 사용

### 장점
- 더 빠른 성능
- 오프라인 작업 가능
- 더 많은 내보내기 옵션

### 사용 방법
1. Figma Desktop App 다운로드 및 설치
2. 파일 열기
3. 내보내기 옵션이 웹 버전보다 더 다양함

## 프로젝트에 적용하기

### 이미지 저장 위치
```
public/images/
├── figma/
│   ├── hero-section.png
│   ├── cards/
│   │   ├── card-01.png
│   │   ├── card-02.png
│   │   ├── card-03.png
│   │   └── card-04.png
│   └── backgrounds/
│       └── hero-bg.png
```

### 코드 적용
1. **CSS 코드**: `public/css/style.css`에 추가
2. **컴포넌트 코드**: 필요시 별도 컴포넌트 파일 생성
3. **스타일 변수**: `public/css/variables.css`에 추가

## 권장 워크플로우

### 1단계: 디자인 분석
- Figma에서 전체 구조 파악
- 섹션별로 구분하여 내보내기 계획 수립

### 2단계: 이미지 내보내기
- 각 섹션별로 필요한 이미지 식별
- PNG (투명 배경 필요시) 또는 JPG 형식 선택
- 2x 해상도 권장 (Retina 디스플레이 대응)

### 3단계: 코드 추출
- CSS 스타일 코드 복사
- 색상 값, 폰트, 간격 등 확인
- 프로젝트의 `variables.css`에 반영

### 4단계: 최적화
- 이미지 최적화 (압축)
- WebP 형식 변환 고려
- 파일 크기 확인 및 조정

## 주의사항

1. **저작권**
   - Figma 파일에 대한 접근 권한 확인
   - 상업적 사용 시 라이선스 확인

2. **이미지 해상도**
   - 웹용: 72-144 PPI
   - Retina 디스플레이: 2x 해상도 권장
   - 파일 크기와 품질의 균형 고려

3. **코드 품질**
   - Figma에서 생성된 코드는 최적화되지 않을 수 있음
   - 프로젝트 구조에 맞게 리팩토링 필요

4. **색상 정확도**
   - Figma 색상과 실제 웹 브라우저 색상 차이 가능
   - 실제 브라우저에서 테스트 필요

## 문제 해결

### API 인증 오류
- Personal Access Token이 올바른지 확인
- 토큰이 만료되지 않았는지 확인

### 이미지 품질 문제
- 해상도를 높여서 다시 내보내기
- SVG 형식 사용 고려 (벡터 그래픽인 경우)

### 코드 스타일 불일치
- Figma 코드를 참고만 하고, 프로젝트 스타일 가이드에 맞게 재작성
- CSS 변수 사용으로 일관성 유지

## 참고 링크

- [Figma API 문서](https://www.figma.com/developers/api)
- [Figma Export 가이드](https://help.figma.com/hc/en-us/articles/360040328153-Export-files-images-videos-and-PDFs)
- [Figma Dev Mode](https://help.figma.com/hc/en-us/articles/360055204533-Use-Dev-Mode-in-Figma)
