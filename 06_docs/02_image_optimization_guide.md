# 이미지 최적화 가이드

## 개요
HUMMAN RESEARCH 웹사이트의 이미지 최적화 가이드입니다.

## 로고 이미지

### SVG 로고
- `logo.svg`: 일반 로고 (200x200px)
- `logo-circle.svg`: 원형 로고 (히어로 섹션용, 200x200px)
- `favicon.svg`: 파비콘 (64x64px)

### 로고 사용 가이드
- SVG 형식으로 벡터 기반이므로 확대/축소 시 품질 손실 없음
- CSS에서 크기 조절 가능
- 메탈릭 효과가 내장되어 있음

## 이미지 최적화 방법

### 1. 서비스 섹션 이미지
- **위치**: `public/images/service-1.jpg`, `service-2.jpg`, `service-3.jpg`
- **권장 크기**: 
  - 데스크톱: 1920x1080px (Full HD)
  - 최적화: WebP 형식 권장
- **압축**: 
  - JPEG 품질: 80-85%
  - 파일 크기: 200KB 이하 권장
- **Lazy Loading**: HTML에 이미 적용됨

### 2. 이미지 형식 선택

#### JPEG
- 사진, 복잡한 이미지에 사용
- 품질: 80-85%
- 용도: 서비스 섹션 이미지

#### WebP
- JPEG 대비 25-35% 작은 파일 크기
- 모던 브라우저 지원
- Fallback으로 JPEG 제공 권장

#### PNG
- 투명 배경이 필요한 경우
- 로고, 아이콘에 사용
- 24-bit PNG 권장

#### SVG
- 벡터 그래픽 (로고, 아이콘)
- 확대/축소 시 품질 손실 없음
- 파일 크기가 작음

### 3. 이미지 최적화 도구

#### 온라인 도구
- **TinyPNG**: PNG/JPEG 압축
- **Squoosh**: Google의 이미지 압축 도구
- **ImageOptim**: Mac용 이미지 최적화

#### 명령줄 도구
- **ImageMagick**: 이미지 변환 및 최적화
- **Sharp**: Node.js 이미지 처리 라이브러리
- **cwebp**: WebP 변환 도구

### 4. 반응형 이미지

#### srcset 사용 (권장)
```html
<img 
  srcset="
    /images/service-1-small.jpg 480w,
    /images/service-1-medium.jpg 768w,
    /images/service-1-large.jpg 1920w
  "
  sizes="(max-width: 768px) 100vw, 100vw"
  src="/images/service-1-large.jpg"
  alt="Service 1"
  loading="lazy"
>
```

#### picture 요소 사용
```html
<picture>
  <source media="(max-width: 768px)" srcset="/images/service-1-mobile.webp">
  <source media="(min-width: 769px)" srcset="/images/service-1-desktop.webp">
  <img src="/images/service-1-desktop.jpg" alt="Service 1" loading="lazy">
</picture>
```

## 이미지 파일 구조

```
public/images/
├── logo.svg              # 일반 로고
├── logo-circle.svg       # 원형 로고 (히어로 섹션)
├── favicon.svg           # 파비콘 SVG
├── favicon.png           # 파비콘 PNG (fallback)
├── service-1.jpg         # 서비스 이미지 1
├── service-2.jpg         # 서비스 이미지 2
├── service-3.jpg         # 서비스 이미지 3
├── og-image.jpg          # Open Graph 이미지 (1200x630px)
└── twitter-image.jpg     # Twitter Card 이미지 (1200x675px)
```

## SEO 이미지

### Open Graph 이미지
- **크기**: 1200x630px
- **형식**: JPEG 또는 PNG
- **파일 크기**: 300KB 이하
- **위치**: `public/images/og-image.jpg`

### Twitter Card 이미지
- **크기**: 1200x675px
- **형식**: JPEG 또는 PNG
- **파일 크기**: 300KB 이하
- **위치**: `public/images/twitter-image.jpg`

## 성능 최적화 팁

1. **Lazy Loading**: 이미지에 `loading="lazy"` 속성 사용 (이미 적용됨)
2. **적절한 크기**: 실제 표시 크기보다 큰 이미지 사용 지양
3. **파일 형식**: WebP 사용 권장 (fallback 제공)
4. **CDN 사용**: 이미지 CDN 사용 시 성능 향상
5. **캐싱**: 적절한 캐시 헤더 설정

## 체크리스트

- [ ] 로고 SVG 파일 생성 완료
- [ ] 서비스 섹션 이미지 준비 (3개)
- [ ] Open Graph 이미지 준비
- [ ] Twitter Card 이미지 준비
- [ ] Favicon PNG 생성 (SVG fallback)
- [ ] 이미지 최적화 (압축, WebP 변환)
- [ ] 반응형 이미지 설정 (srcset)
- [ ] Lazy loading 적용 확인
