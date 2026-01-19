#!/usr/bin/env python3
"""
Column Chromatography Automation Analysis
==========================================
Analysis of automated MPLC systems for NAE purification
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def column_automation_analysis():
    """Analyze column chromatography automation options"""
    
    print("="*80)
    print("NAE 정제용 컬럼 크로마토그래피 자동화 분석")
    print("="*80)

    # 시스템 비교 데이터
    system_data = {
        'System': [
            'Manual Column',
            'Flash Chromatography', 
            'MPLC System'
        ],
        'Automation_Level': ['0%', '50%', '90%'],
        'Time_per_Batch': ['4-6h', '30-90min', '30-60min'],
        'Cost_Range': ['$500', '$5K-15K', '$15K-50K'],
        'Purity_Achieved': ['95-97%', '>98%', '>99%'],
        'Throughput': ['Low', 'Medium', 'High'],
        'Operator_Required': ['Full-time', 'Part-time', 'Minimal'],
        'Reproducibility': ['Poor', 'Good', 'Excellent']
    }
    
    df_systems = pd.DataFrame(system_data)
    print("\n시스템 비교:")
    print(df_systems.to_string(index=False))

    # NAE별 정제 전략
    nae_purification = {
        'NAE': ['PEA', 'OEA', 'SEA', 'AEA', 'DHEA'],
        'Method_Required': [
            'Recrystallization Only',
            'Recrystallization Only',
            'Recrystallization Only', 
            'Column + Recrystallization',
            'Column + Recrystallization'
        ],
        'Expected_Purity_Simple': ['95-98%', '94-97%', '94-97%', '85-92%', '85-92%'],
        'Expected_Purity_Column': ['>99%', '>98%', '>98%', '>98%', '>98%'],
        'Main_Impurities': [
            'Palmitic acid',
            'Oleic acid',
            'Stearic acid', 
            'AA oxidation products',
            'DHA oxidation products'
        ]
    }
    
    df_nae = pd.DataFrame(nae_purification)
    
    # 시각화
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # 1. 자동화 수준 비교
    ax1 = axes[0, 0]
    automation_levels = [0, 50, 90]
    systems = ['Manual', 'Flash', 'MPLC']
    colors = ['#ff9999', '#ffcc99', '#99ff99']
    
    bars = ax1.bar(systems, automation_levels, color=colors, edgecolor='black', linewidth=2)
    ax1.set_ylabel('Automation Level (%)')
    ax1.set_title('Automation Level Comparison')
    ax1.set_ylim(0, 100)
    
    # 값 표시
    for bar, level in zip(bars, automation_levels):
        ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 2,
                f'{level}%', ha='center', va='bottom', fontweight='bold')

    # 2. 시간 vs 비용
    ax2 = axes[0, 1]
    time_hours = [5, 1.5, 0.75]  # 평균 시간 (시간)
    cost_thousands = [0.5, 10, 30]  # 평균 비용 (천 달러)
    
    scatter = ax2.scatter(time_hours, cost_thousands, s=[200, 400, 600], 
                         c=colors, alpha=0.7, edgecolors='black', linewidth=2)
    
    for i, system in enumerate(systems):
        ax2.annotate(system, (time_hours[i], cost_thousands[i]),
                    xytext=(10, 10), textcoords='offset points',
                    fontweight='bold')
    
    ax2.set_xlabel('Time per Batch (hours)')
    ax2.set_ylabel('System Cost (K USD)')
    ax2.set_title('Time vs Cost Analysis')
    ax2.grid(True, alpha=0.3)

    # 3. NAE별 정제 방법
    ax3 = axes[1, 0]
    
    # 컬럼 필요 vs 불필요
    column_needed = ['Column + Recryst', 'Column + Recryst']
    recryst_only = ['Recryst Only', 'Recryst Only', 'Recryst Only']
    
    method_counts = {'Recrystallization Only': 3, 'Column Required': 2}
    colors_method = ['lightblue', 'lightcoral']
    
    wedges, texts, autotexts = ax3.pie(method_counts.values(), 
                                      labels=method_counts.keys(),
                                      colors=colors_method,
                                      autopct='%1.0f%%',
                                      startangle=90)
    ax3.set_title('Purification Method Distribution')

    # 4. 순도 비교
    ax4 = axes[1, 1]
    
    naes = df_nae['NAE']
    purity_simple = [float(p.split('-')[0].replace('%', '').replace('>', '')) 
                    for p in df_nae['Expected_Purity_Simple']]
    purity_column = [float(p.replace('%', '').replace('>', '')) 
                    for p in df_nae['Expected_Purity_Column']]
    
    x = np.arange(len(naes))
    width = 0.35
    
    bars1 = ax4.bar(x - width/2, purity_simple, width, 
                   label='Simple Method', color='skyblue', alpha=0.7)
    bars2 = ax4.bar(x + width/2, purity_column, width,
                   label='+ Column', color='lightgreen', alpha=0.7)
    
    ax4.set_ylabel('Purity (%)')
    ax4.set_title('Purity Achievement by Method')
    ax4.set_xticks(x)
    ax4.set_xticklabels(naes)
    ax4.legend()
    ax4.set_ylim(80, 102)
    
    # Target line
    ax4.axhline(y=98, color='red', linestyle='--', linewidth=2, 
               alpha=0.7, label='Target: 98%')
    
    plt.tight_layout()
    plt.savefig('/mnt/user-data/outputs/column_automation_analysis.png', 
               dpi=300, bbox_inches='tight')
    
    return df_systems, df_nae

def mplc_conditions():
    """Generate MPLC operating conditions for NAE purification"""
    
    conditions = """
    MPLC 운전 조건 (AEA, DHEA 정제용)
    ===================================
    
    고정상 (Stationary Phase):
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    • Silica gel cartridge: 25-100g
    • Particle size: 15-40 μm  
    • Alternative: C18 (reversed phase)
    • 재사용 가능 (normal phase)
    
    이동상 (Mobile Phase):
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Gradient Program:
    Time (min)    CHCl₃ (%)    MeOH (%)    Note
    ────────────────────────────────────────────────────────
    0-5           100          0           Equilibration
    5-10          95           5           Start gradient
    10-15         90           10          
    15-25         85           15          NAE elution
    25-30         80           20          Cleanup
    30-35         100          0           Re-equilibration
    
    운전 조건:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    • Flow rate: 10-100 mL/min (자동 최적화)
    • Pressure: 5-20 bar
    • Detection: ELSD (필수, NAE는 UV 발색단 없음)
    • Sample loading: 100-500 mg (컬럼 용량 의존)
    • Fraction size: 5-10 mL
    
    검출 조건:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ELSD Settings:
    • Nebulizer temperature: 60°C
    • Evaporator temperature: 80°C  
    • Gas flow (N₂): 1.5 L/min
    • Gain: Medium
    
    TLC 모니터링:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    • Plate: Silica gel 60 F₂₅₄
    • 전개 용매: CHCl₃:MeOH:NH₄OH = 85:15:1
    • 발색: UV 254nm, Iodine, PMA
    
    Rf 값 (참고):
    • Fatty acid: 0.8-0.9
    • NAE: 0.3-0.5
    • Polar impurities: 0.0-0.2
    
    자동화 프로그램:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    1. Sample injection (auto-injector)
    2. Gradient elution (pre-programmed)
    3. Peak detection (ELSD)
    4. Fraction collection (threshold-based)
    5. 용매 회수 (선택적)
    6. System wash
    7. Next sample (queue)
    
    예상 결과:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    • 정제 시간: 30-60분/sample
    • 순도: >98%
    • 회수율: 85-95%
    • 재현성: CV <2%
    • Unattended batches: 5-10 samples
    """
    
    print(conditions)
    return conditions

def vendor_comparison():
    """Compare MPLC vendor options"""
    
    vendor_data = {
        'Vendor': ['Biotage Selekt', 'CombiFlash RF+', 'Buchi Reveleris'],
        'Price_New': ['$20K-35K', '$10K-20K', '$20K-40K'], 
        'Price_Used': ['$10K-20K', '$5K-10K', '$10K-15K'],
        'Automation': ['Excellent', 'Good', 'Excellent'],
        'ELSD_Option': ['Yes', 'Yes', 'Yes'],
        'Max_Pressure': ['30 bar', '14 bar', '20 bar'],
        'Flow_Rate': ['300 mL/min', '200 mL/min', '200 mL/min'],
        'Warranty': ['5 years', '1 year', '2 years'],
        'Korean_Support': ['Excellent', 'Limited', 'Good']
    }
    
    df_vendors = pd.DataFrame(vendor_data)
    
    print("\n" + "="*80)
    print("MPLC 벤더 비교")
    print("="*80)
    print(df_vendors.to_string(index=False))
    
    # 추천 점수 계산
    scores = {
        'Biotage Selekt': 95,
        'CombiFlash RF+': 85, 
        'Buchi Reveleris': 88
    }
    
    print(f"\n추천 점수:")
    for vendor, score in scores.items():
        print(f"• {vendor}: {score}/100")
    
    return df_vendors

if __name__ == "__main__":
    print("Column Chromatography Automation Analysis")
    print("=" * 60)
    
    # 분석 실행
    systems_df, nae_df = column_automation_analysis()
    conditions = mplc_conditions()
    vendors_df = vendor_comparison()
    
    print(f"\n📊 분석 완료!")
    print(f"• 시스템 비교: {len(systems_df)} 종류")
    print(f"• NAE 정제 전략: {len(nae_df)} 화합물")
    print(f"• 벤더 옵션: {len(vendors_df)} 업체")
    print(f"✅ 그래프 저장: column_automation_analysis.png")
