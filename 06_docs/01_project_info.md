# HUMMAN RESEARCH 웹 홈페이지 프로젝트 정보

## 프로젝트 개요
- **프로젝트명**: HUMMAN RESEARCH 웹 홈페이지
- **목적**: 회사 공식 홈페이지 제작
- **디자인 기준**: Name-card.png (명함 디자인)

## 프로젝트 구조
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
│       ├── 01_project_setup_20260119T075522.md
│       ├── 02_setup_and_planning_20260119T080127.md
│       ├── 03_plan_update_activetheory_20260119T083550.md
│       ├── 04_css_variables_20260119T084053.md
│       ├── 05_html_structure_20260119T084608.md
│       ├── 06_css_styling_20260119T084907.md
│       ├── 07_logo_and_images_20260119T085110.md
│       ├── 08_file_organization_and_service_images_20260119T090000.md
│       ├── 08_file_organization_and_service_images_20260119T091201.md
│       ├── 09_service_images_layout_fix_20260119T091826.md
│       ├── 10_logo_assets_recreated_from_name_card_20260119T093554.md
│       ├── 11_logo_horn_vertices_fix_20260119T095049.md
│       ├── 12_logo_horn_vertices_and_gray_circle_fix_20260119T095347.md
│       ├── 13_logo_mark_recreated_20260119T095453.md
│       ├── 15_script_cleanup_and_logo_regeneration_20260119T100135.md
│       ├── 16_logo_alpha_mask_refined_20260119T100459.md
│       ├── 17_logo_alpha_mask_white_only_20260119T100719.md
│       ├── 17_logo_text_cut_silver_preserved_20260119T100844.md
│       ├── 18_git_repository_initialization_20260119T101331.md
│       ├── 19_github_remote_setup_and_push_20260119T101637.md
│       ├── 20_logo_vector_style_script_update_20260120T202855.md
│       ├── 21_logo_vector_style_assets_generated_20260120T204053.md
│       ├── 22_logo_detail_tuning_20260120T204613.md
│       └── 23_website_contents_docx_to_md_20260123T114848.md
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
└── public/
    ├── index.html
    ├── css/
    │   ├── style.css
    │   └── variables.css
    └── images/
        ├── ai.ai
        ├── README.md
        └── svg.svg
```

## 디자인 컨셉
명함 디자인을 기반으로 한 프리미엄하고 전문적인 웹사이트 디자인

### 주요 특징
- 로얄/코발트 블루와 실버 메탈릭 색상 조합
- 미니멀하고 깔끔한 레이아웃
- 브랜드 일관성 유지

## 진행 상황
- [x] 프로젝트 구조 생성
- [x] 디자인 계획 수립
- [ ] 색상 코드 정확히 추출
- [ ] HTML/CSS 기본 구조 작성
- [ ] 섹션별 디자인 구현
- [ ] 반응형 디자인 적용
- [ ] 최종 테스트 및 배포
