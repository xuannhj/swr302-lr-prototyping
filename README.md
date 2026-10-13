# SWR302 Literature Review: The Effect of Prototyping on Identifying Missing and Unclear Requirements (RP6)

[![LaTeX Compilation](https://img.shields.io/badge/LaTeX-IEEEtran-brightgreen.svg)](main.tex)
[![Corpus Size](https://img.shields.io/badge/Studies-17%20Papers-blue.svg)](docs/Synthesis_Matrix.md)
[![Status](https://img.shields.io/badge/Status-Scaffolded%20%26%20Synchronized-success.svg)](#)

> **Môn học**: SWR302 (Software Requirements) – FPT University (Ho Chi Minh City Campus)  
> **Nhóm thực hiện**: Group 3  
> **Thành viên nhóm**:
> - Nguyễn Phạm Xuân Nhi (SE201170)
> - Nguyễn Minh Tú (SE192854)
> - Nguyễn Lê Nhật Khoa (SE204266)
> - Nguyễn Trí Minh Nhật (SE204263)
> - Trần Bá Lộc (SE180247)  
> **Chủ đề nghiên cứu (RP6)**: *The Effect of Prototyping on Identifying Missing and Unclear Requirements* (Ảnh hưởng của prototyping đến khả năng phát hiện yêu cầu thiếu và chưa rõ ràng).

---

## 1. 3 Câu Hỏi Nghiên Cứu Cốt Lõi (Research Questions)

* **RQ6.1 (Phương thức & Quy trình - How):** *How are prototypes used to support requirements elicitation and validation?*  
  $\rightarrow$ Cách thức vận hành prototype theo khung mô hình PAM (*Purpose, Scope, Media, Exploration, Use*) ở cả 2 pha: Khám phá (Elicitation) và Thẩm định (Validation).
* **RQ6.2 (Thực nghiệm đối đầu - Empirical Efficacy):** *Does using a prototype help stakeholders identify missing or unclear requirements better than using textual specifications alone?*  
  $\rightarrow$ Bằng chứng định lượng đối đầu giữa Paper Prototyping vs. JAD vs. Phỏng vấn phi cấu trúc vs. Đặc tả văn bản thuần (SRS/User Stories).
* **RQ6.3 (Phân loại yêu cầu - Classification):** *What types of requirements can be clarified more effectively through prototyping?*  
  $\rightarrow$ Mức độ làm rõ phân hóa theo từng nhóm yêu cầu: Functional (FR), Usability/UI, và giải quyết "điểm mù" Non-Functional (NFR) bằng Loud Paper Prototyping (LPP) và Video Scenarios.

---

## 2. Khung Đánh Giá Cốt Lõi Của Mentor (Tripartite Analysis)

Mọi bài báo và chương mục trong báo cáo đều được phân tích xuyên suốt qua 3 lăng kính:
1. **WHY (Tại sao cần?):** Rào cản nhận thức, tri thức ẩn (*tacit knowledge*), tính đa nghĩa bẩm sinh của ngôn ngữ tự nhiên (*lexical/syntactic ambiguity*) và hội chứng "ký duyệt mù" của đặc tả văn bản thuần.
2. **HOW (Áp dụng thế nào?):** Quy trình phỏng vấn tương tác, giao thức Think-Aloud, Wizard-of-Oz, và tích hợp trực tiếp vào Agile Backlog Grooming.
3. **CLASSIFICATION (Phân loại ra sao?):** Phân loại theo độ chân thực (*fidelity*), phương tiện (*media*), kích thước khám phá PAM, và phân loại 4 cấp độ mơ hồ (*Cascon 2025 / Berry 2003*).

---

## 3. Checklist Giải Quyết 5 Điểm Phản Biện Của Giảng Viên

Chi tiết xem tại [`docs/Mentor_Feedback_Checklist.md`](docs/Mentor_Feedback_Checklist.md):
- [x] **FB-1 (Mở rộng kho tài liệu 10–18 bài):** Đã thu thập và trích xuất 17 bài (10 Core Studies + 7 Seminal Studies) tại [`docs/Synthesis_Matrix.md`](docs/Synthesis_Matrix.md) và [`ref.bib`](ref.bib).
- [x] **FB-2 (Chỉ số đo lường độ mơ hồ Semantic Ambiguity Metrics):** Tích hợp taxonomy Cascon 2025 (Lexical, Syntactic, Scope, Vagueness), công thức Ambiguity Reduction Rate (ARR), và chỉ số sai lệch diễn giải $\Delta_{\text{interp}}$ (Spoletini 2018) vào Section V.
- [x] **FB-3 (Phân tích chi phí & rủi ro Premature Idea Cementing):** Đánh giá rủi ro tâm lý và nợ kỹ thuật của High-fidelity prototypes; thiết lập nguyên tắc phân bổ Low-fi cho Elicitation và High-fi cho Validation.
- [x] **FB-4 (Cơ chế tích hợp Low-fi với Agile, User Stories & Backlog Grooming):** Đề xuất mô hình *Enriched User Story* (Lucassen et al. 2022) kết hợp Proto-personas (2019) giảm thiểu 30–40% rework.
- [x] **FB-5 (Thiết kế thực nghiệm minh chứng giải quyết Gaps):** Xây dựng blueprint thực nghiệm bán tự nhiên (Quasi-experiment) gồm 3 nhóm đối chứng đo lường bằng LLM classifier.

---

## 4. Cấu Trúc Thư Mục Dự Án (Repository Structure)

```text
swr302-lr-prototyping/
├── README.md                          # Tổng quan dự án, tiến độ và hướng dẫn
├── main.tex                           # File nguồn LaTeX chính (chuẩn IEEEtran conference)
├── ref.bib                            # Cơ sở dữ liệu BibTeX chuẩn hóa (17+ trích dẫn)
├── .gitignore                         # File cấu hình bỏ qua file rác biên dịch LaTeX
├── docs/
│   ├── Synthesis_Matrix.md            # Bảng tổng hợp trích xuất dữ liệu 17 bài báo
│   ├── Mentor_Feedback_Checklist.md   # Bảng theo dõi giải quyết 5 điểm phản biện
│   └── Papers.md                      # Danh mục phân loại bài báo ban đầu
├── papers_pdf/                        # Thư mục lưu trữ toàn bộ các file PDF tài liệu gốc
│   ├── 03_bjarnason2023empirically_PAM_Model.pdf
│   ├── 04_rueda2020requirements_Family_Experiments.pdf
│   ├── 05_abad2018loud_Interactive_Paper_Prototyping.pdf
│   ├── 06_uv2023empirical_GUI_Usability_Elicitation.pdf
│   ├── 07_rej2022evolve_Requirements_Evolution.pdf
│   ├── 08_jserd2019protopersona_UX_Requirements.pdf
│   ├── 09_antonelli2022iterative_Natural_Language_Scenarios.pdf
│   ├── 12_acm2022proposal_Agile_Enriched_User_Stories.pdf
│   ├── 13_diaz2021gender_Elicitation_Gender_Influence.pdf
│   ├── 14_cascon2025ambiguity_Ambiguity_Taxonomy_LM.pdf
│   ├── PrototypingUseasaSoftwareRequirementsWorldcist2018.pdf
│   └── WR302_RP6_Progress_Report_Group3.pdf
├── sections/                          # Các chương báo cáo học thuật theo chuẩn IEEE
│   ├── 01_introduction.tex            # Vấn đề, rào cản nhận thức, RQ6.1 - RQ6.3
│   ├── 02_methodology.tex               # Quy trình SLR theo chuẩn Kitchenham
│   ├── 03_thematic_review.tex          # Tổng hợp RQ6.1 (PAM) và RQ6.3 (FR, UI, NFR)
│   ├── 04_comparative_analysis.tex     # Thực nghiệm đối đầu RQ6.2 (Rueda et al.)
│   ├── 05_discussion_and_gaps.tex      # Rủi ro Hi-Fi, Agile grooming, Ambiguity metrics
│   └── 06_conclusion.tex               # Kết luận và đề xuất thực nghiệm
└── scripts/
    └── verify_bib.py                  # Script kiểm tra trích xuất \cite{} và ref.bib
```

---

## 5. Hướng Dẫn Biên Dịch Báo Cáo LaTeX

### Cách 1: Sử dụng Overleaf (Khuyên dùng)
1. Nén thư mục dự án thành file `.zip`.
2. Truy cập [Overleaf](https://www.overleaf.com), chọn **New Project** $\rightarrow$ **Upload Project**.
3. Đặt file chính là `main.tex`, chọn trình biên dịch là `pdfLaTeX` và bấm **Recompile**.

### Cách 2: Biên dịch cục bộ (Local Terminal)
Nếu máy bạn đã cài đặt MiKTeX / TeX Live:
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

---

## 6. Hướng Dẫn Đồng Bộ Lên GitHub (Git & GitHub)

Dự án đã được khởi tạo Git repository cục bộ và commit phiên bản ban đầu. Để đưa lên GitHub:
1. Đăng nhập GitHub CLI:
   ```bash
   gh auth login
   ```
2. Tạo repo mới trên GitHub và push toàn bộ mã nguồn:
   ```bash
   gh repo create swr302-lr-prototyping --public --source=. --remote=origin --push
   ```
3. Hoặc nếu bạn đã tạo repository trống trên website GitHub:
   ```bash
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git branch -M main
   git push -u origin main
   ```
