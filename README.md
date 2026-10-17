# The Effect of Prototyping on Identifying Missing and Unclear Requirements: A Systematic Literature Review (RP6)

[![LaTeX IEEEtran](https://img.shields.io/badge/Format-IEEEtran%20Conference-brightgreen.svg)](main.tex)
[![Corpus Size](https://img.shields.io/badge/Corpus-26%20Studies-blue.svg)](docs/Papers.md)
[![Pilot Test ARR](https://img.shields.io/badge/Pilot%20ARR-93.3%25%20(p%3D0.005)-orange.svg)](docs/PILOT_TEST_EXPERIMENT_REPORT.md)
[![Academic Venue](https://img.shields.io/badge/Course-SWR302%20(FPT%20University)-red.svg)](#)
[![Git Status](https://img.shields.io/badge/Git%20Branch-main%20(Clean)-success.svg)](#)

> **Môn học**: SWR302 (Software Requirements Engineering) — Trường Đại học FPT TP.HCM  
> **Sinh viên thực hiện**: Nguyễn Phạm Xuân Nhi — MSSV: **SE201170**  
> **Mentor hướng dẫn**: Minh Khánh  
> **Đề tài nghiên cứu (RP6)**: *The Effect of Prototyping on Identifying Missing and Unclear Requirements: A Systematic Literature Review*  
> **Repository GitHub**: [https://github.com/xuannhj/swr302-lr-prototyping](https://github.com/xuannhj/swr302-lr-prototyping)

---

## 📌 MỤC LỤC
1. [Tổng Quan Đề Tài & Câu Hỏi Nghiên Cứu](#1-tổng-quan-đề-tài--câu-hỏi-nghiên-cứu)
2. [Hệ Thống 26 Tài Liệu Nghiên Cứu (Corpus Architecture)](#2-hệ-thống-26-tài-liệu-nghiên-cứu-corpus-architecture)
3. [Điểm Nhấn Thực Nghiệm Pilot Test (Empirical Verification)](#3-điểm-nhấn-thực-nghiệm-pilot-test-empirical-verification)
4. [Cấu Trúc Báo Cáo Học Thuật LaTeX (Modular Structure)](#4-cấu-trúc-báo-cáo-học-thuật-latex-modular-structure)
5. [Cấu Trúc Thư Mục Dự Án (Repository Tree)](#5-cấu-trúc-thư-mục-dự-án-repository-tree)
6. [Hướng Dẫn Biên Dịch Báo Cáo LaTeX / PDF](#6-hướng-dẫn-biên-dịch-báo-cáo-latex--pdf)

---

## 1. TỔNG QUAN ĐỀ TÀI & CÂU HỎI NGHIÊN CỨU

Nghiên cứu này là một bài **Systematic Literature Review (SLR)** tuân thủ nghiêm ngặt phương pháp luận Kitchenham & Charters và khung báo cáo PRISMA. Mục tiêu chính là đánh giá một cách định lượng và định tính tác động của các kỹ thuật **Prototyping** (nguyên mẫu phần mềm) trong việc nhận diện và khắc phục **yêu cầu bị thiếu (missing requirements)** và **yêu cầu chưa rõ ràng (unclear/ambiguous requirements)** so với đặc tả văn bản truyền thống.

Báo cáo tập trung giải quyết **3 Câu Hỏi Nghiên Cứu (Research Questions)**:

* **RQ6.1 (Phương thức & Cơ chế vận hành - How & Process):**  
  *How are prototypes used to support requirements elicitation and validation?*  
  $\rightarrow$ Khảo sát quy trình vận hành Prototype theo mô hình PAM (*Purpose, Scope, Media, Exploration Strategy, Use* — Bjarnason et al. 2023) ở cả hai pha: Khám phá tri thức ẩn (*Tacit Knowledge*) và Thẩm định kịch bản người dùng.
* **RQ6.2 (Hiệu quả thực nghiệm đối đầu - Empirical Efficacy vs. Text):**  
  *Does using a prototype help stakeholders identify missing or unclear requirements better than using textual specifications alone?*  
  $\rightarrow$ Tổng hợp bằng chứng đối đầu giữa Prototype (Paper, Low-Fi, Interactive Wireframes) với phỏng vấn phi cấu trúc, JAD, và tài liệu SRS văn bản thuần (Rueda et al. 2020, Keshk et al. 2022).
* **RQ6.3 (Đặc thù loại yêu cầu - Requirement Typology & NFR Deficit):**  
  *What types of requirements can be clarified more effectively through prototyping?*  
  $\rightarrow$ Đánh giá độ nhạy cảm của từng loại yêu cầu: Functional Requirements (FR), Giao diện & Tính khả dụng (UI/Usability), và giải pháp phá vỡ điểm mù yêu cầu phi chức năng (NFR Deficit) bằng *Loud Paper Prototyping* (Abad et al. 2018) và *In-situ Prototyping* (Hoffmann & Leimeister 2011).

---

## 2. HỆ THỐNG 26 TÀI LIỆU NGHIÊN CỨU (CORPUS ARCHITECTURE)

Hệ thống tài liệu tham khảo gồm **26 công trình học thuật xuất sắc** được tinh chọn qua phễu sàng lọc PRISMA và phương pháp *Backward Snowballing* (Wohlin 2014):

```
                        [TỔNG HỢP 26 PAPERS]
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
[10 CORE EMPIRICAL]     [8 FOUNDATIONAL PAPERS]    [8 EXTENDED & MENTOR]
 • 2020–2025 đỉnh cao     • Chuẩn mực lý thuyết     • 2 bài Mentor đề cử:
 • IEEE, ACM, Springer    • IREB, AMCIS, REFSQ       Hoffmann 2011, Lending 2022
 • Dữ liệu định lượng     • Khung mơ hồ gốc        • 3 bài IEEE RE / ASE 2024
 • Trả lời RQ6.1 - RQ6.3  • Participative Prototyping • 3 bài Snowballing kinh điển
```

* **10 Core Empirical Studies (2020–2025)**: Bjarnason et al. (EMSE 2023), Rueda et al. (IST 2020), Ormeño et al. (IST 2023), Ferrari et al. (REJ 2022), Antonelli et al. (WER 2022), Kopczyńska & Shi (IEEE RE 2023), Gupta et al. (IEEE IT Pro 2022), Keshk et al. (ACM FAMECSE 2022), Díaz et al. (SCP 2021), Oghabi & Kahani (CASCON 2025).
* **8 Foundational Studies**: Hickey & Dean (AMCIS 1998), Abad et al. (IEEE EmpiRE 2018), Pinheiro et al. (JSERD 2019), Pacheco et al. (IET Softw 2018), Ferrari et al. (REJ 2016), Spoletini et al. (REFSQ 2018), Brill et al. (REFSQ 2010), Pohl & Rupp (IREB 2016).
* **8 Extended Papers mới**:
  1. `hoffmann2011automotive` (IJEB 2011): In-situ Prototyping trong hệ thống nhúng / ô tô (Audi A6) giải quyết điểm mù NFR.
  2. `lending2022rubric` (JISE 2022): Thang đo Rubric chuẩn hóa đo lường năng lực khơi gợi yêu cầu trên sinh viên đại học.
  3. `kolthoff2024interlinking` (IEEE RE 2024): Ứng dụng LLM liên kết tự động User Story với GUI Prototype.
  4. `kolthoff2024selfelicitation` (ACM/IEEE ASE 2024): GS. Kurt Schneider — công cụ SERGUI tự khơi gợi yêu cầu bị thiếu.
  5. `wei2023boosting` (IEEE RE 2023): Diffusion Models (UI-Diffuser) sinh GUI mock-up siêu tốc.
  6. `lim2008anatomy` (ACM TOCHI 2008): Lý thuyết bản chất Prototype làm Bộ lọc (Filters).
  7. `inayat2015systematic` (Elsevier CHB 2015): SLR thực hành Agile RE và giảm thiểu Rework.
  8. `berry2003contract` (SE 2003): Cội nguồn ngôn ngữ học 4 loại mơ hồ trong yêu cầu phần mềm.

Chi tiết bảng trích xuất và thuyết minh lý do xem tại [`docs/Papers.md`](docs/Papers.md).

---

## 3. ĐIỂM NHẤN THỰC NGHIỆM PILOT TEST (EMPIRICAL VERIFICATION)

Theo chỉ dẫn phương pháp luận của Mentor, đề tài không dừng lại ở tổng thuật lý thuyết mà đã tiến hành **chạy thử nghiệm Pilot Test thực tế (Hướng 2: Semantic Ambiguity Checklist x Low-Fi Prototype)** trên tập mẫu 10 User Stories thực tế:

* **Bài toán thực nghiệm**: Nền tảng Đặt phòng & Dịch vụ Khách sạn (*TravelStay Hospitality Platform*).
* **Khung phân loại lỗi**: Dựa trên Taxonomy của Cascon 2025 & Berry 2003 (Structural, Scope, Anaphoric, Vagueness).
* **Kết quả đối chứng định lượng**:
  * Ban đầu: **15 lỗi mơ hồ** trên 10 câu văn bản thô ($100\%$ câu dính lỗi).
  * Sau khi neo vào Wireframe Prototype & Gherkin criteria: Còn sót **1 lỗi duy nhất** (lỗi về độ trễ tải trang backend).
  * **Tỉ lệ giảm mơ hồ toàn phần (ARR)**: Đạt **$\mathbf{93.3\%}$** (vượt xa mức kỳ vọng $\ge 70\%$ của Cascon 2025).
  * **Triệt tiêu tuyệt đối ($100\%$)**: Lỗi đại từ (*Anaphoric Ambiguity*) và lỗi phạm vi lượng từ (*Scope Ambiguity*).
* **Kiểm định thống kê phi tham số**:
  * Wilcoxon Signed-Rank Test ($N=10$ cặp quan sát) đạt **$Z = -2.81, p = 0.005 < 0.01$** (ý nghĩa thống kê cực kỳ cao).
* **Giải pháp khắc phục lỗi NFR còn lại**: Áp dụng *Visual Acceptance Criteria SLA* (Keshk et al. 2022).

Chi tiết toàn bộ ma trận 10 User Stories và số liệu kiểm toán xem tại [`docs/PILOT_TEST_EXPERIMENT_REPORT.md`](docs/PILOT_TEST_EXPERIMENT_REPORT.md).

---

## 4. CẤU TRÚC BÁO CÁO HỌC THUẬT LATEX (MODULAR STRUCTURE)

Dự án được xây dựng theo kiến trúc **Module hóa tuyệt đối** (không dùng file gộp), tuân thủ định dạng chuẩn IEEEtran 2 cột (Conference format):

| File Mã Nguồn | Tên Chương Mục Báo Cáo | Nội Dung Học Thuật Cốt Lõi |
| :--- | :--- | :--- |
| [`main.tex`](main.tex) | Master Entry File | Cấu hình packages, metadata tác giả, layout 2 cột IEEEtran |
| [`sections/01_introduction.tex`](sections/01_introduction.tex) | I. Introduction | Đặt vấn đề, rào cản tâm lý/ngôn ngữ, động lực nghiên cứu, 3 RQs |
| [`sections/02_methodology.tex`](sections/02_methodology.tex) | II. Review Methodology | Chiến lược tìm kiếm 4 cơ sở dữ liệu, tiêu chí IC/EC, Phễu PRISMA |
| [`sections/03_thematic_review.tex`](sections/03_thematic_review.tex) | III. Thematic Synthesis | Khung PAM (RQ6.1), Mơ hồ ngữ nghĩa (RQ6.2), NFR Deficit (RQ6.3) |
| [`sections/04_comparative_analysis.tex`](sections/04_comparative_analysis.tex) | IV. Comparative Analysis | Bảng tổng hợp thực nghiệm Table III, phân tích chi phí & độ chân thực |
| [`sections/05_research_gaps.tex`](sections/05_research_gaps.tex) | V. Research Gaps | 3 khoảng trống lớn: Điểm mù NFR, thiếu thước đo, thiên vị Web/App |
| [`sections/06_proposed_directions.tex`](sections/06_proposed_directions.tex) | VI. Proposed Directions | Đề cương 3 hướng nghiên cứu tương lai (Enriched US, Checklist, Think-Aloud) |
| [`sections/07_conclusion.tex`](sections/07_conclusion.tex) | VII. Conclusion | Đóng gói kết luận, bài học kinh nghiệm cho kỹ sư công nghiệp |
| [`ref.bib`](ref.bib) | Bibliography Database | 26 trích dẫn BibTeX chuẩn hóa 100% DOI quốc tế |

---

## 5. CẤU TRÚC THƯ MỤC DỰ ÁN (REPOSITORY TREE)

```text
swr302-lr-prototyping/
├── README.md                          # Tài liệu giới thiệu tổng quan dự án (chuẩn GitHub)
├── main.tex                           # Master LaTeX entry point (gọi \input{sections/...})
├── ref.bib                            # Cơ sở dữ liệu BibTeX chuẩn hóa (26 tài liệu)
├── .gitignore                         # Loại trừ file tạm sinh ra khi biên dịch LaTeX
├── sections/                          # Thư mục chứa 7 modules học thuật độc lập
│   ├── 01_introduction.tex            # Chương 1: Giới thiệu & 3 RQs
│   ├── 02_methodology.tex             # Chương 2: Phương pháp luận SLR (Phễu PRISMA)
│   ├── 03_thematic_review.tex         # Chương 3: Tổng hợp chủ đề theo 3 RQs
│   ├── 04_comparative_analysis.tex    # Chương 4: Bảng đối chiếu Table III & phân tích chi phí
│   ├── 05_research_gaps.tex           # Chương 5: Khoảng trống nghiên cứu (Research Gaps)
│   ├── 06_proposed_directions.tex     # Chương 6: Đề cương 3 hướng thực nghiệm đề xuất
│   └── 07_conclusion.tex              # Chương 7: Kết luận & hàm ý thực tiễn
├── docs/                              # Tài liệu bổ trợ, cẩm nang phản biện & báo cáo thực nghiệm
│   ├── Papers.md                      # Danh mục 26 tài liệu nghiên cứu & thuyết minh bổ sung
│   ├── PILOT_TEST_EXPERIMENT_REPORT.md# Báo cáo kết quả chạy Pilot Test thực nghiệm (ARR=93.3%)
│   ├── CAM_NANG_TRA_LOI_MENTOR.md     # Cẩm nang trả lời phản biện và câu hỏi hóc búa
│   ├── Mentor_Feedback_Checklist.md   # Theo dõi giải quyết phản biện của Mentor
│   └── Synthesis_Matrix_RP6.xlsx      # Bảng ma trận trích xuất số liệu Excel
└── papers_pdf/                        # Toàn văn các bài báo khoa học gốc (.pdf)
```

---

## 6. HƯỚNG DẪN BIÊN DỊCH BÁO CÁO LATEX / PDF

Bài báo được tinh chỉnh và định dạng chuẩn xác theo quy chuẩn IEEEtran conference format.

### Cách 1: Biên dịch trên Overleaf (Khuyên dùng)
1. Tải toàn bộ mã nguồn về máy hoặc nén thư mục thành file `.zip`.
2. Đăng nhập vào [Overleaf](https://www.overleaf.com), tạo dự án mới: **New Project** $\rightarrow$ **Upload Project**.
3. Chọn trình biên dịch **pdfLaTeX**, chọn file chính là `main.tex`, và bấm **Recompile**.

### Cách 2: Biên dịch qua Terminal (TeX Live / MiKTeX)
```bash
# Lần 1: Biên dịch cấu trúc
pdflatex main.tex

# Lần 2: Xử lý tài liệu tham khảo BibTeX
bibtex main

# Lần 3 & 4: Cập nhật chỉ mục cross-references và hoàn tất layout
pdflatex main.tex
pdflatex main.tex
```

---

*Dự án thuộc khuôn khổ môn học SWR302 (Software Requirements) — Khoa Kỹ thuật Phần mềm, Trường Đại học FPT TP.HCM.*
