#!/usr/bin/env python3
"""
Korean MPLC Vendor Analysis
============================
Analysis of MPLC/Flash chromatography vendors and purchasing options in Korea
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def korea_vendor_analysis():
    """Analyze Korean MPLC vendor landscape"""
    
    print("="*80)
    print("한국 내 MPLC/Flash 크로마토그래피 시스템 공급업체 분석")
    print("="*80)

    # 주요 벤더 데이터
    vendor_data = {
        'Company': [
            'Biotage Korea',
            'Shimadzu Scientific Korea', 
            'DKSH Korea (Buchi)',
            '영인크로매스 (YL Instruments)',
            '영진바이오크롬',
            'LabX (중고)',
            'American Lab Trading',
            'New Life Scientific'
        ],
        'Products': [
            'Selekt Flash/MPLC',
            'Nextra Prep, LC Systems',
            'Pure Chromatography Systems', 
            'Custom HPLC/Flash Systems',
            'Prep HPLC, Column Manufacturing',
            'Used Biotage Selekt',
            'Refurbished Selekt',
            'Refurbished CombiFlash'
        ],
        'Location': [
            '성남시 분당구',
            '서울 강남구',
            '서울 금천구',
            '안양시',
            '안양시', 
            'Online (Global)',
            'Online (USA)',
            'Online (USA)'
        ],
        'Contact_Phone': [
            '031-706-8500',
            '02-540-5541',
            'DKSH 문의',
            '031-423-6800',
            '웹사이트 문의',
            'www.labx.com',
            '+1-860-572-0773',
            '+1-573-468-5128'
        ],
        'Support_Level': [
            'Excellent',
            'Good', 
            'Good',
            'Excellent',
            'Good',
            'None',
            'Limited',
            'Limited'
        ],
        'Price_Range_USD': [
            '25K-45K',
            '15K-40K',
            '25K-60K',
            '15K-30K', 
            '15K-35K',
            '8K-25K',
            '10K-20K',
            '4K-8K'
        ]
    }
    
    df_vendors = pd.DataFrame(vendor_data)
    print("\n주요 공급업체:")
    print(df_vendors[['Company', 'Products', 'Contact_Phone', 'Price_Range_USD']].to_string(index=False))

    # 추천 우선순위
    recommendations = {
        'Company': [
            'Biotage Korea',
            '영인크로매스 (YL)', 
            'LabX 중고 Selekt',
            'Shimadzu Korea',
            'American Lab Trading'
        ],
        'Scenario': [
            '최고 성능 + 완벽 지원',
            '가성비 + 현지 지원',
            '연구용 + 예산 절약',
            '안정성 + 브랜드',
            '성능 + 중간 예산'
        ],
        'Investment': [
            '$35K-45K',
            '$20K-30K',
            '$12K-20K',
            '$25K-40K', 
            '$15K-25K'
        ],
        'ROI_Years': [
            '2-3년',
            '1.5-2년',
            '1-1.5년',
            '2-3년',
            '1.5-2.5년'
        ],
        'Rating': [5, 4, 3, 4, 4]
    }
    
    df_recommendations = pd.DataFrame(recommendations)
    
    # 시각화
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # 1. 가격 범위 비교
    ax1 = axes[0, 0]
    
    # 가격 데이터 추출 및 변환
    price_data = []
    companies_short = []
    for i, price_range in enumerate(df_vendors['Price_Range_USD']):
        company = df_vendors['Company'].iloc[i]
        if '-' in price_range:
            min_price, max_price = price_range.replace('K', '').split('-')
            price_data.append([int(min_price), int(max_price)])
        else:
            price = int(price_range.replace('K', ''))
            price_data.append([price, price])
        companies_short.append(company.split()[0])
    
    # 가격 범위 막대그래프
    y_pos = np.arange(len(companies_short))
    for i, (min_p, max_p) in enumerate(price_data):
        ax1.barh(y_pos[i], max_p - min_p, left=min_p, 
                color='lightcoral' if '중고' in df_vendors['Company'].iloc[i] or 'Lab' in df_vendors['Company'].iloc[i] 
                else 'skyblue', alpha=0.7)
    
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(companies_short, fontsize=10)
    ax1.set_xlabel('Price Range (K USD)')
    ax1.set_title('Price Comparison by Vendor')
    ax1.grid(axis='x', alpha=0.3)

    # 2. 지원 수준 분포
    ax2 = axes[0, 1]
    support_counts = df_vendors['Support_Level'].value_counts()
    colors_support = ['gold', 'lightgreen', 'lightcoral', 'lightgray']
    
    wedges, texts, autotexts = ax2.pie(support_counts.values, 
                                      labels=support_counts.index,
                                      colors=colors_support[:len(support_counts)],
                                      autopct='%1.0f%%',
                                      startangle=90)
    ax2.set_title('Support Level Distribution')

    # 3. 추천 매트릭스
    ax3 = axes[1, 0]
    
    # 추천 점수 시각화
    scenarios = df_recommendations['Scenario']
    ratings = df_recommendations['Rating']
    companies_rec = df_recommendations['Company']
    
    colors_rating = ['red', 'orange', 'yellow', 'lightgreen', 'green']
    bars = ax3.barh(range(len(scenarios)), ratings, 
                   color=[colors_rating[r-1] for r in ratings], alpha=0.7)
    
    ax3.set_yticks(range(len(scenarios)))
    ax3.set_yticklabels([f"{comp}\n({scen})" for comp, scen in 
                        zip(companies_rec, scenarios)], fontsize=9)
    ax3.set_xlabel('Rating (1-5)')
    ax3.set_title('Recommendation Matrix')
    ax3.set_xlim(0, 5.5)
    
    # 값 표시
    for i, (bar, rating) in enumerate(zip(bars, ratings)):
        ax3.text(rating + 0.1, bar.get_y() + bar.get_height()/2, 
                f'{rating}/5', va='center', fontweight='bold')

    # 4. ROI 비교
    ax4 = axes[1, 1]
    
    # 투자 금액 vs ROI
    investments = []
    roi_years = []
    
    for inv, roi in zip(df_recommendations['Investment'], df_recommendations['ROI_Years']):
        # 투자 금액 파싱
        inv_clean = inv.replace('$', '').replace('K', '')
        if '-' in inv_clean:
            inv_avg = sum(map(int, inv_clean.split('-'))) / 2
        else:
            inv_avg = int(inv_clean)
        investments.append(inv_avg)
        
        # ROI 연수 파싱  
        roi_clean = roi.replace('년', '')
        if '-' in roi_clean:
            roi_avg = sum(map(float, roi_clean.split('-'))) / 2
        else:
            roi_avg = float(roi_clean)
        roi_years.append(roi_avg)
    
    scatter = ax4.scatter(investments, roi_years, 
                         s=[r*100 for r in ratings], 
                         c=ratings, cmap='RdYlGn', alpha=0.7,
                         edgecolors='black', linewidth=2)
    
    for i, comp in enumerate(companies_rec):
        ax4.annotate(comp.split()[0], 
                    (investments[i], roi_years[i]),
                    xytext=(10, 10), textcoords='offset points',
                    fontweight='bold')
    
    ax4.set_xlabel('Investment (K USD)')
    ax4.set_ylabel('ROI Period (Years)')
    ax4.set_title('Investment vs ROI Analysis')
    ax4.grid(True, alpha=0.3)
    plt.colorbar(scatter, ax=ax4, label='Rating (1-5)')
    
    plt.tight_layout()
    plt.savefig('/mnt/user-data/outputs/korea_vendor_analysis.png', 
               dpi=300, bbox_inches='tight')
    
    return df_vendors, df_recommendations

def action_plan_generator():
    """Generate step-by-step action plan for purchasing"""
    
    action_plan = """
    NAE 합성 자동화를 위한 즉시 실행 액션 플랜
    =============================================
    
    🎯 목표: AEA, DHEA 정제용 MPLC 시스템 확보
    
    Week 1: 정보 수집 및 초기 연락
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    1일차 (월요일):
    □ Biotage Korea 연락
      📞 전화: 031-706-8500
      📧 이메일: korea_info@biotage.com
      요청사항:
      • Selekt + ELSD 시스템 정보
      • NAE 분리 application note
      • 데모 일정 협의
      • 견적서 요청
    
    2일차 (화요일):
    □ 영인크로매스 연락
      📞 전화: 031-423-6800
      요청사항:
      • 맞춤형 Flash/Prep 시스템 상담
      • NAE 정제 특화 가능성 논의
      • 기술지원 수준 확인
      • 예비 견적
    
    3일차 (수요일):
    □ 중고 시장 조사
      🌐 LabX.com 계정 생성
      🔍 "Biotage Selekt" 검색
      📧 Alert 설정 (새 매물 알림)
      💰 현재 시장가 조사
    
    4일차 (목요일):
    □ 백업 옵션 조사
      • Shimadzu Korea (02-540-5541)
      • DKSH Korea (Buchi 대리점)
      • American Lab Trading 온라인 문의
    
    5일차 (금요일):
    □ 정보 정리 및 비교표 작성
      • 각 업체 응답 정리
      • 가격 비교표 작성
      • 기술 스펙 비교
      • 다음 주 계획 수립
    
    Week 2-3: 데모 및 현장 평가
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    Biotage 데모 (2-3일 할당):
    ─────────────────────────────────────────────────────────
    준비물:
    • AEA crude sample (100-500mg)
    • DHEA crude sample (100-500mg)
    • 기대 순도 목표 (>98%)
    
    평가 항목:
    ✓ 분리 효율 (Resolution)
    ✓ 순도 달성도 (HPLC 확인)
    ✓ 회수율 (Recovery rate)
    ✓ 재현성 (Reproducibility)
    ✓ 자동화 수준
    ✓ 사용 편의성
    ✓ 교육 프로그램
    
    YL Instruments 방문 (1-2일):
    ─────────────────────────────────────────────────────────
    협의 사항:
    • NAE 정제 특화 시스템 설계
    • 맞춤형 컬럼 개발 가능성
    • 검출기 옵션 (ELSD 포함)
    • 교육 및 기술지원 계획
    • 납기 및 설치 일정
    
    Week 4: 최종 결정
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    평가 매트릭스:
    ─────────────────────────────────────────────────────────
    성능 (40점):
    • 분리 효율: /10
    • 순도 달성: /10  
    • 자동화 수준: /10
    • 재현성: /10
    
    지원 (30점):
    • 한국 A/S: /10
    • 교육 프로그램: /10
    • 소모품 공급: /10
    
    비용 (20점):
    • 초기 투자: /10
    • 운영비용: /10
    
    납기 (10점):
    • 설치 일정: /10
    
    총점: /100
    
    의사결정 기준:
    ─────────────────────────────────────────────────────────
    • 80점 이상: 구매 확정
    • 70-79점: 조건부 구매 (협상)
    • 70점 미만: 재검토
    
    최종 체크리스트:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    □ 예산 승인 완료
    □ 설치 공간 준비
    □ 전력/가스 공급 확인
    □ 교육 일정 협의
    □ 보증 및 서비스 계약 검토
    □ 소모품 초기 구매 계획
    □ 레퍼런스 확인
    
    예상 투자 및 ROI:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    시나리오 A (Biotage Selekt):
    • 초기 투자: $40,000
    • 연간 절약: $15,000 (시간 + 순도)
    • ROI: 2.7년
    • 5년 총 이익: $35,000
    
    시나리오 B (YL 맞춤형):
    • 초기 투자: $25,000
    • 연간 절약: $12,000
    • ROI: 2.1년  
    • 5년 총 이익: $35,000
    
    시나리오 C (중고 Selekt):
    • 초기 투자: $18,000
    • 연간 절약: $10,000
    • ROI: 1.8년
    • 5년 총 이익: $32,000
    
    ⚠️ 위험 요소:
    • 중고 장비: A/S 제한, 예상치 못한 수리비
    • 신품: 높은 초기 투자, 현금 흐름 압박
    • 맞춤형: 개발 지연, 성능 불확실성
    """
    
    print(action_plan)
    return action_plan

def contact_information():
    """Generate formatted contact information"""
    
    contacts = {
        '1순위': {
            'company': 'Biotage Korea',
            'phone': '031-706-8500',
            'email': 'korea_info@biotage.com',
            'address': '경기도 성남시 분당구 양현로 322 코리아디자인센터 803호',
            'products': 'Biotage Selekt + ELSD',
            'price': '$35,000-45,000',
            'advantage': '한국 직접 지원, 최고 자동화'
        },
        '2순위': {
            'company': '영인크로매스 (YL Instruments)',
            'phone': '031-423-6800', 
            'email': '웹사이트 문의',
            'address': '경기도 안양시 동안구 엘에스로 142',
            'products': '맞춤형 Flash/Prep 시스템',
            'price': '$20,000-30,000',
            'advantage': '가성비 우수, 맞춤 설계 가능'
        },
        '3순위': {
            'company': 'LabX 중고 마켓',
            'phone': 'Online only',
            'email': 'www.labx.com',
            'address': 'Global marketplace',
            'products': '중고 Biotage Selekt',
            'price': '$12,000-20,000 (통관비 포함)',
            'advantage': '50-70% 비용 절약'
        }
    }
    
    print("\n" + "="*80)
    print("즉시 연락 추천 순서")
    print("="*80)
    
    for priority, info in contacts.items():
        print(f"\n{priority}: {info['company']}")
        print(f"📞 전화: {info['phone']}")
        print(f"📧 이메일: {info['email']}")
        print(f"📍 주소: {info['address']}")
        print(f"🏷️ 제품: {info['products']}")
        print(f"💰 가격: {info['price']}")
        print(f"✅ 장점: {info['advantage']}")
        print("-" * 60)
    
    return contacts

if __name__ == "__main__":
    print("Korean MPLC Vendor Analysis Tool")
    print("=" * 50)
    
    # 분석 실행
    vendors_df, recommendations_df = korea_vendor_analysis()
    action_plan = action_plan_generator()
    contacts = contact_information()
    
    print(f"\n📊 분석 완료!")
    print(f"• 한국 공급업체: {len(vendors_df)} 곳")
    print(f"• 추천 옵션: {len(recommendations_df)} 시나리오")
    print(f"• 1순위 연락처: {contacts['1순위']['phone']}")
    print(f"✅ 그래프 저장: korea_vendor_analysis.png")
