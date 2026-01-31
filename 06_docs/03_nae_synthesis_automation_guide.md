# NAE (N-Acylethanolamide) 합성 자동화 완전 가이드

> 이 문서는 NAE 합성부터 자동화 컬럼 크로마토그래피 구매까지 모든 내용을 정리한 종합 가이드입니다.

## 📋 목차

1. [NAE 기본 정보](#nae-기본-정보)
2. [합성 방법](#합성-방법)
3. [정제 전략](#정제-전략)
4. [컬럼 크로마토그래피 자동화](#컬럼-크로마토그래피-자동화)
5. [장비 구매 가이드](#장비-구매-가이드)
6. [한국 내 구매처](#한국-내-구매처)
7. [생성된 코드 모음](#생성된-코드-모음)

---

## NAE 기본 정보

### 5종 NAE 분류

| NAE | 전체명 | 분자량 | BBB 투과 | 정제 난이도 |
|-----|--------|--------|----------|-------------|
| **PEA** | Palmitoylethanolamide | 299 | 매우 낮음 | 낮음 (재결정) |
| **OEA** | Oleoylethanolamide | 325 | 매우 낮음 | 낮음 (재결정) |
| **SEA** | Stearoylethanolamide | 327 | 알려지지 않음 | 낮음 (재결정) |
| **AEA** | Anandamide | 347 | 보통 | **높음 (컬럼 필수)** |
| **DHEA** | Docosahexaenoylethanolamide | 371 | 좋음 | **높음 (컬럼 필수)** |

### BBB(Blood-Brain Barrier) 투과 분석

**Poor BBB Penetration:**
- PEA, OEA, SEA: 말초 작용 (항염, 식욕 조절)
- 간접적 뇌 효과 (BBB 보호, 신경염증 감소)

**Good BBB Penetration:**
- AEA: CB1/CB2 수용체 활성화 (중추+말초)
- DHEA (Synaptamide): 시냅스 보호, 학습/기억 향상

---

## 합성 방법

### Schotten-Baumann 반응

```
Step 1: Acid Chloride Formation
Fatty acid + SOCl₂ → Fatty acyl chloride
(Reflux 2h, remove excess SOCl₂)

Step 2: Acylation  
Fatty acyl-Cl + Ethanolamine + Et₃N (base)
→ NAE + Et₃N·HCl
(0°C → RT, 3 hours, CH₂Cl₂ solvent)

Step 3: Work-up
- Wash with 1N HCl
- Wash with sat. NaHCO₃  
- Dry over Na₂SO₄
- Evaporate solvent
- Recrystallize (EtOH or MeOH)

Expected yield: 60-80%
Purity: >95% after recrystallization
```

### 비용 분석

**구매 vs 합성 (1g 기준):**
- 구매: $65,000 (모든 NAE)
- 합성: $370 (재료비)
- **절약: 99.4% ($64,630)**

---

## 정제 전략

### 컬럼 크로마토그래피 요구사항

| NAE | 컬럼 필요? | 이유 | 재결정만으로 달성 가능 순도 |
|-----|-----------|------|---------------------------|
| PEA | ❌ 불필요 | 포화지방산, 단순 부산물 | 95-98% |
| OEA | ❌ 불필요 | 단일불포화, 단순 부산물 | 94-97% |
| SEA | ❌ 불필요 | 포화지방산, 단순 부산물 | 94-97% |
| **AEA** | ✅ **필수** | PUFA 산화물, 복잡 부산물 | 85-92% (불충분) |
| **DHEA** | ✅ **필수** | PUFA 산화물, 복잡 부산물 | 85-92% (불충분) |

### 정제 워크플로우

**PEA, OEA, SEA (간단):**
1. 합성 (3시간)
2. Aqueous work-up
3. 재결정 (EtOH)
4. 순도: 95-98%
5. **총 시간: 5-6시간**

**AEA, DHEA (고급):**
1. 합성 (불활성 분위기, 3시간)
2. Aqueous work-up (신속)
3. **컬럼 크로마토그래피 (30-60분, 자동화시)**
4. 재결정 (선택적)
5. 순도: >98%
6. **총 시간: 6시간 (자동화), 9-11시간 (수동)**

---

## 컬럼 크로마토그래피 자동화

### 시스템 비교

| 시스템 | 자동화 수준 | 시간/배치 | 비용 | 순도 |
|--------|------------|----------|------|------|
| 수동 컬럼 | 0% | 4-6시간 | $500 | 95-97% |
| Flash Chrom | 50% | 30-90분 | $5K-15K | >98% |
| **MPLC** | **90%** | **30-60분** | **$15K-50K** | **>99%** |

### 추천 MPLC 조건

```
고정상: Silica gel cartridge (25-100g)
이동상: CHCl₃:MeOH gradient
  - Start: CHCl₃ 100%
  - → CHCl₃:MeOH = 95:5
  - → CHCl₃:MeOH = 90:10  
  - → CHCl₃:MeOH = 85:15 (NAE 용출)

검출: ELSD (권장, NAE는 UV 발색단 없음)
유량: 10-100 mL/min
압력: 5-20 bar
```

---

## 장비 구매 가이드

### TOP 3 추천 시스템

#### 1. Biotage Selekt ⭐⭐⭐⭐⭐
- **가격:** $20K-35K (신품)
- **특징:** 최고 자동화, ELSD 옵션, 5년 보증
- **장점:** NAE 정제 최적화, 완전 무인 운전

#### 2. Teledyne CombiFlash ⭐⭐⭐⭐  
- **가격:** $10K-20K (신품)
- **특징:** 가성비 우수, 검증된 성능
- **장점:** 경제적, 안정적 자동화

#### 3. Buchi Reveleris ⭐⭐⭐⭐
- **가격:** $20K-40K (신품)  
- **특징:** Flash + Prep LC 겸용
- **장점:** 다용도, 고품질

### 중고/리퍼비시 옵션

| 출처 | 가격 절약 | 보증 | 신뢰도 |
|------|----------|------|--------|
| American Laboratory Trading | 50-80% | 1년 | 매우 높음 |
| LabX.com | 50-70% | 없음 | 높음 |
| New Life Scientific | 50-70% | 90-120일 | 높음 |

---

## 한국 내 구매처

### 🏆 최우선 추천

#### 1. Biotage Korea ⭐⭐⭐⭐⭐
```
📞 전화: 031-706-8500
📧 이메일: korea_info@biotage.com  
📍 주소: 경기도 성남시 분당구 양현로 322

제품: Biotage Selekt + ELSD
가격: $35K-45K (VAT별도)
납기: 4-6주

✅ 장점:
• 한국 직접 지원 (현지 엔지니어)
• 무료 데모 + 교육
• 즉시 A/S 가능  
• 소모품 현지 재고
```

#### 2. 영인크로매스 (YL Instruments) ⭐⭐⭐⭐
```
📞 전화: 031-423-6800
📍 주소: 경기도 안양시 동안구

제품: 맞춤형 Flash/Prep 시스템
가격: $20K-30K
납기: 2-4주

✅ 장점:  
• 가격 경쟁력 (40% 절약)
• 맞춤 설계 가능 (NAE 특화)
• 한국 기술, 빠른 지원
```

### 기타 공급업체

| 업체 | 제품 | 전화 | 특징 |
|------|------|------|------|
| Shimadzu Korea | Nextra Prep | 02-540-5541 | 안정적, 교육센터 |
| DKSH (Buchi) | Pure Systems | - | 공식대리점, 전문지원 |
| 영진바이오크롬 | 맞춤 Prep | - | 컬럼 전문, 바이오 특화 |

### 중고 옵션

- **LabX.com:** 중고 Selekt $8K-25K
- **유엠씨사이언스:** 현지 중고/리퍼브

---

## 즉시 실행 액션 플랜

### Week 1: 정보 수집
```
□ Biotage Korea 연락 (031-706-8500)
  → Selekt + ELSD 데모 신청
  → NAE 분리 application note 요청

□ 영인크로매스 연락 (031-423-6800)  
  → 맞춤형 시스템 상담
  → 가격 견적 요청

□ LabX.com 모니터링
  → "Biotage Selekt" 검색 설정
  → Alert 등록 (새 매물 알림)
```

### Week 2-3: 데모 & 평가
```
□ Biotage 데모
  → AEA, DHEA crude sample 준비
  → 실제 분리 테스트
  → 자동화 기능 평가

□ YL Instruments 방문
  → 기술진과 NAE 분리 논의
  → 맞춤형 시스템 스펙 협의
```

### Week 4: 최종 결정
```
평가 기준:
• 성능 (40%): 분리효율, 순도, 재현성
• 지원 (30%): A/S, 교육, 소모품
• 비용 (20%): 초기비용, 운영비  
• 납기 (10%): 설치 시기
```

### 투자 예상

| 시나리오 | 총비용 | ROI |
|----------|--------|-----|
| Biotage Selekt (신품) | $45K | 2-3년 |
| YL 맞춤형 | $32K | 1.5-2년 |
| 중고 Selekt | $22K | 1-1.5년 |

---

## 최종 결론

### NAE 합성 자동화 전략

```
🎯 목표: AEA, DHEA 고순도 정제 자동화

💡 핵심 발견:
• PEA, OEA, SEA → 재결정만으로 충분
• AEA, DHEA → 컬럼 크로마토그래피 필수
• MPLC 자동화 → 4-6시간 → 30-60분

🏆 최적 솔루션:
1순위: Biotage Selekt + ELSD (한국 지원)
2순위: YL Instruments 맞춤형 (가성비)  
3순위: 중고 Selekt (예산 절약)
```

### 즉시 연락할 곳

```
🥇 Biotage Korea: 031-706-8500
   → Selekt 데모 신청 (최우선)

🥈 영인크로매스: 031-423-6800  
   → 맞춤형 상담 (가성비)

🥉 LabX.com 검색: "Biotage Selekt"
   → 중고 모니터링 (예산형)
```

**⚠️ 중요:** 반드시 실제 AEA/DHEA 샘플로 데모 테스트 후 구매 결정!

---

*이 가이드는 2026년 1월 기준으로 작성되었으며, 가격과 연락처는 변동될 수 있습니다.*
