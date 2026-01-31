#!/usr/bin/env python3
"""
NAE (N-Acylethanolamide) Synthesis Cost-Benefit Analysis
========================================================
This script analyzes the cost-benefit of synthesizing vs purchasing NAEs,
calculates BBB penetration properties, and evaluates purification strategies.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def nae_cost_analysis():
    """Analyze cost comparison between synthesis and purchase"""
    
    print("="*80)
    print("NAE 합성 vs 구매 비용 분석")
    print("="*80)
    
    # NAE 기본 데이터
    nae_data = {
        'NAE': ['PEA', 'OEA', 'SEA', 'AEA', 'DHEA'],
        'Full_Name': [
            'Palmitoylethanolamide',
            'Oleoylethanolamide', 
            'Stearoylethanolamide',
            'Anandamide',
            'Docosahexaenoylethanolamide'
        ],
        'MW': [299, 325, 327, 347, 371],
        'LogP': [5.8, 6.2, 6.0, 6.8, 7.5],
        'BBB_Penetration': ['Very Poor', 'Very Poor', 'Unknown', 'Moderate', 'Good'],
        'Purchase_Price_1g': [8000, 10000, 12000, 15000, 20000],  # USD
        'Synthesis_Cost_1g': [25, 30, 25, 60, 90],  # Raw materials
        'Purification_Method': ['Recrystallization', 'Recrystallization', 
                               'Recrystallization', 'Column Required', 'Column Required']
    }
    
    df = pd.DataFrame(nae_data)
    
    # 비용 계산
    total_purchase = df['Purchase_Price_1g'].sum()
    total_synthesis = df['Synthesis_Cost_1g'].sum() + 115  # Additional reagents
    savings = total_purchase - total_synthesis
    savings_percent = (savings / total_purchase) * 100
    
    print(f"\n💰 비용 비교 (1g 각각)")
    print(f"구매 총비용: ${total_purchase:,}")
    print(f"합성 총비용: ${total_synthesis:,}")
    print(f"절약 금액: ${savings:,}")
    print(f"절약 비율: {savings_percent:.1f}%")
    
    # 시각화
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. 가격 비교
    ax1 = axes[0, 0]
    x = range(len(df))
    width = 0.35
    
    ax1.bar([i - width/2 for i in x], df['Purchase_Price_1g']/1000, 
           width, label='Purchase', color='red', alpha=0.7)
    ax1.bar([i + width/2 for i in x], df['Synthesis_Cost_1g']/1000, 
           width, label='Synthesis', color='green', alpha=0.7)
    
    ax1.set_xlabel('NAE Type')
    ax1.set_ylabel('Cost (K USD)')
    ax1.set_title('Purchase vs Synthesis Cost Comparison')
    ax1.set_xticks(x)
    ax1.set_xticklabels(df['NAE'])
    ax1.legend()
    ax1.set_yscale('log')
    
    # 2. BBB 투과도
    ax2 = axes[0, 1]
    bbb_counts = df['BBB_Penetration'].value_counts()
    colors = ['lightcoral', 'lightblue', 'lightgreen', 'gold']
    ax2.pie(bbb_counts.values, labels=bbb_counts.index, autopct='%1.0f%%',
            colors=colors[:len(bbb_counts)])
    ax2.set_title('BBB Penetration Distribution')
    
    # 3. 분자량 vs LogP
    ax3 = axes[1, 0]
    scatter = ax3.scatter(df['MW'], df['LogP'], s=100, 
                         c=df['Purchase_Price_1g'], cmap='viridis', alpha=0.7)
    for i, nae in enumerate(df['NAE']):
        ax3.annotate(nae, (df['MW'][i], df['LogP'][i]), 
                    xytext=(5, 5), textcoords='offset points')
    
    ax3.set_xlabel('Molecular Weight (g/mol)')
    ax3.set_ylabel('LogP (Lipophilicity)')
    ax3.set_title('Molecular Properties vs Price')
    plt.colorbar(scatter, ax=ax3, label='Price (USD)')
    
    # BBB 이상적 영역 표시
    ax3.axhline(y=5, color='red', linestyle='--', alpha=0.5, label='LogP = 5 (BBB limit)')
    ax3.axvline(x=450, color='red', linestyle='--', alpha=0.5, label='MW = 450 (BBB limit)')
    ax3.legend()
    
    # 4. 정제 전략
    ax4 = axes[1, 1]
    purification_counts = df['Purification_Method'].value_counts()
    colors_purif = ['lightblue', 'lightcoral']
    ax4.pie(purification_counts.values, labels=purification_counts.index, 
            autopct='%1.0f%%', colors=colors_purif)
    ax4.set_title('Purification Method Requirements')
    
    plt.tight_layout()
    plt.savefig('/mnt/user-data/outputs/NAE_analysis.png', dpi=300, bbox_inches='tight')
    print("\n✅ 시각화 저장: NAE_analysis.png")
    
    return df

def synthesis_protocol():
    """Generate detailed synthesis protocol"""
    
    protocol = """
    NAE 합성 프로토콜 (Schotten-Baumann 반응)
    =============================================
    
    시약:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    • Fatty acids (각 10g):
      - Palmitic acid: $25
      - Oleic acid: $30  
      - Stearic acid: $25
      - Arachidonic acid (2g): $60
      - DHA (2g): $90
    • Ethanolamine (100ml): $25
    • SOCl₂ (100ml): $45
    • Et₃N (100ml): $30
    • CH₂Cl₂, EtOH, etc.: $40
    
    총 시약비: ~$370
    
    프로토콜:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    Step 1: Acid Chloride 형성
    ────────────────────────────────────────────────────────
    1. Round-bottom flask에 fatty acid (10 mmol) 넣기
    2. SOCl₂ (2 eq, 20 mmol) 천천히 첨가
    3. Reflux 2시간 (oil bath 80°C)
    4. 과량 SOCl₂ 제거 (rotavap, 40°C)
    5. 무수 조건 유지
    
    Step 2: Amide 형성 (Acylation)
    ────────────────────────────────────────────────────────
    1. Acid chloride를 CH₂Cl₂ (50ml)에 용해
    2. Ice bath로 0°C 냉각
    3. Et₃N (3 eq, 30 mmol) 첨가
    4. Ethanolamine (1.1 eq, 11 mmol) 천천히 첨가
    5. 0°C → RT, 3시간 stirring
    6. 반응 모니터링: TLC (CHCl₃:MeOH = 9:1)
    
    Step 3: Work-up
    ────────────────────────────────────────────────────────
    1. 1N HCl (50ml)로 washing (과량 amine 제거)
    2. Sat. NaHCO₃ (50ml)로 washing (과량 acid 제거)
    3. Brine (50ml)로 washing
    4. Na₂SO₄로 건조
    5. 용매 증발 (rotavap)
    
    Step 4: 정제
    ────────────────────────────────────────────────────────
    
    PEA, OEA, SEA (재결정만):
    • Hot EtOH에 용해
    • 서서히 냉각
    • 결정 여과, 진공 건조
    • 순도: 95-98%
    
    AEA, DHEA (컬럼 크로마토그래피 필수):
    • Flash/MPLC 정제
    • CHCl₃:MeOH gradient
    • 순수 fraction 수집
    • 재결정 (선택적)
    • 순도: >98%
    
    예상 수율:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    • PEA: 70-80%
    • OEA: 65-75%  
    • SEA: 70-80%
    • AEA: 60-70% (산화 손실)
    • DHEA: 55-65% (산화 손실)
    
    특별 주의사항 (AEA, DHEA):
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    • 불활성 분위기 (Ar 또는 N₂)
    • 산화방지제 첨가 (BHT, 0.1%)
    • 빛 차단
    • 저온 작업 (<30°C)
    • 신속한 정제
    """
    
    print(protocol)
    return protocol

def column_requirements():
    """Analyze column chromatography requirements"""
    
    column_data = {
        'NAE': ['PEA', 'OEA', 'SEA', 'AEA', 'DHEA'],
        'Column_Required': ['Optional', 'Optional', 'Optional', 'Essential', 'Essential'],
        'Reason': [
            'Saturated FA, simple impurities',
            'Monounsaturated FA, simple impurities', 
            'Saturated FA, simple impurities',
            'PUFA oxidation products, complex',
            'PUFA oxidation products, complex'
        ],
        'Recryst_Purity': ['95-98%', '94-97%', '94-97%', '85-92%', '85-92%'],
        'Column_Purity': ['>99%', '>98%', '>98%', '>98%', '>98%'],
        'Time_Manual': ['5-6h', '5-6h', '5-6h', '9-11h', '9-11h'],
        'Time_Auto': ['5-6h', '5-6h', '5-6h', '6h', '6h']
    }
    
    df_col = pd.DataFrame(column_data)
    
    print("\n" + "="*80)
    print("컬럼 크로마토그래피 요구 사항 분석")
    print("="*80)
    print(df_col.to_string(index=False))
    
    return df_col

if __name__ == "__main__":
    print("NAE Synthesis Analysis Tool")
    print("=" * 50)
    
    # 실행
    nae_df = nae_cost_analysis()
    protocol = synthesis_protocol()
    column_df = column_requirements()
    
    print(f"\n📊 분석 완료!")
    print(f"• NAE 데이터: {len(nae_df)} 종류")
    print(f"• 총 절약: ${(nae_df['Purchase_Price_1g'].sum() - nae_df['Synthesis_Cost_1g'].sum() - 115):,}")
    print(f"• 컬럼 필요 NAE: {len([x for x in column_df['Column_Required'] if x == 'Essential'])}종")
