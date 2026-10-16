# Mentor Feedback Resolution Checklist (SWR302 - RP6)

> **Dự án**: The Effect of Prototyping on Identifying Missing and Unclear Requirements  
> **Sinh viên thực hiện**: Nguyễn Phạm Xuân Nhi - SE201170 (Department of Software Engineering, FPT University)  
> **Mục tiêu**: Theo dõi và giải quyết triệt để 5 điểm phản biện cốt lõi từ Giảng viên hướng dẫn (Mentor).

---

## 1. Tổng quan 5 Điểm phản biện then chốt

| STT | Vấn đề phản biện từ Mentor | Trạng thái | Chương / Phần xử lý tương ứng |
| :---: | :--- | :---: | :--- |
| **FB-1** | **Mở rộng kho tài liệu nghiên cứu (10 - 18 bài)**: Tránh dựa dẫm vào quá ít bài báo; cần đủ dung lượng đại diện cho SLR. | `[x] Đã hoàn thành` | `docs/Papers.md`, `ref.bib` (17 bài: 10 Core + 7 Seminal) |
| **FB-2** | **Bổ sung chỉ số đo lường độ mơ hồ ngôn ngữ (Semantic Ambiguity Metrics)**: Đo lường khách quan "Unclear Requirements" thay vì chỉ đếm số lượng cảm tính. | `[x] Đã hoàn thành` | `sections/02_methodology.tex`, `sections/03_thematic_review.tex` (Taxonomy Cascon 2025, RoBERTa F1=78.84%, Spoletini Metrics) |
| **FB-3** | **Phân tích sâu chi phí vận hành & rủi ro cam kết ý tưởng sớm (Premature Idea Cementing)** của High-fidelity Prototypes. | `[x] Đã hoàn thành` | `sections/03_thematic_review.tex` (Mô hình PAM Bjarnason 2023, Gupta 2022 IEEE) |
| **FB-4** | **Cơ chế tích hợp Paper Prototyping (Low-fi) với Agile, User Stories & Backlog Grooming** nhằm giảm thiểu rework trong Sprint. | `[x] Đã hoàn thành` | `sections/03_thematic_review.tex` (Keshk/ACM 2022, Soares/JSERD 2019, giảm 30-40% rework) |
| **FB-5** | **Bổ sung thực nghiệm minh chứng tính khả thi giải quyết Research Gaps**: Tránh để gaps mang tính lý thuyết suông; đề xuất thiết kế thực nghiệm khả thi. | `[x] Đã cấu trúc` | `sections/05_discussion_and_gaps.tex`, `sections/06_conclusion.tex` (Khung thực nghiệm quasi-experiment, metrics đối chứng) |

---

## 2. Chi tiết giải pháp kỹ thuật theo từng phản biện

### FB-1: Mở rộng kho tài liệu nghiên cứu (10 - 18 bài)
- [x] **Trích xuất 10 bài Core Studies**:
  - `Bjarnason et al. (2023)` (PAM framework, multi-case study 11 startups)
  - `Rueda et al. (2020)` (Family of 4 experiments so sánh Paper Prototyping vs JAD vs Interviews)
  - `Panach et al. (2023)` (Empirical study đo usability & GUI mockups)
  - `Rej et al. (2022)` (Tiến hóa yêu cầu qua interactive discovery sessions)
  - `Antonelli et al. (2022)` (Lặp lại scenarios tự nhiên qua prototyping tool)
  - `Bano et al. (2023)` (Video prototyping giải quyết Non-functional requirements)
  - `Gupta et al. (2022)` (Áp dụng prototyping chiến lược trong startups)
  - `Lucassen et al. / ACM (2022)` (Kết hợp Prototyping với Enriched User Stories trong Agile)
  - `Díaz et al. (2021)` (Kiểm soát biến nhiễu gender trong thực nghiệm elicitation)
  - `Cascon et al. (2025)` (Multi-label ambiguity detection bằng Language Models)
- [x] **Tích hợp 7 bài Seminal/Background Studies**:
  - `Hickey & Dean (1998)` (Participative prototype evaluation methodology)
  - `Abad et al. (2018)` (Loud and Interactive Paper Prototyping - LPP)
  - `Soares et al. / JSERD (2019)` (Proto-personas & UX requirements)
  - `Davis et al. / IET (2018)` (Maturity SLR của 18 kỹ thuật elicitation)
  - `Ferrari et al. (2016)` (Ambiguity and tacit knowledge trong phỏng vấn)
  - `Spoletini et al. (2018)` (Interview review & ambiguity detection metrics)
  - `Brill et al. (2010)` (Video vs Use cases phát hiện requirements dưới áp lực thời gian)
- [x] Cập nhật đầy đủ file trích dẫn BibTeX chuẩn hóa: `ref.bib`.

---

### FB-2: Bổ sung chỉ số đo lường độ mơ hồ ngôn ngữ (Semantic Ambiguity Metrics)
- [x] **Xác lập Taxonomy phân loại Ambiguity**:
  - Áp dụng phân loại 4 nhóm từ Cascon et al. (2025) & Berry et al. (2003):
    1. *Lexical/Semantic Ambiguity* (Từ đa nghĩa, thuật ngữ kỹ thuật mâu thuẫn).
    2. *Syntactic/Structural Ambiguity* (Cấu trúc câu gây hiểu nhầm phạm vi điều kiện).
    3. *Scope Ambiguity* (Mơ hồ phạm vi tác động của toán tử hoặc modifier).
    4. *Vagueness / Incompleteness* (Thiếu tiêu chí nghiệm thu định lượng, ranh giới mờ).
- [x] **Công thức đo lường mức độ giảm thiểu mơ hồ**:
  $$\text{Ambiguity Reduction Rate (ARR)} = \frac{A_{\text{pre-proto}} - A_{\text{post-proto}}}{A_{\text{pre-proto}}} \times 100\%$$
- [x] **Tích hợp chỉ số Spoletini et al. (2018)**:
  - Tỉ lệ bất đồng diễn giải giữa Analyst và Reviewer/Stakeholder ($\Delta_{\text{interpretation}}$).

---

### FB-3: Phân tích sâu chi phí vận hành & rủi ro Cam kết ý tưởng sớm (Premature Idea Cementing)
- [x] **Khái niệm Premature Idea Cementing**:
  - Khi stakeholder và developer nhìn thấy High-fidelity prototype quá sớm (pixel-perfect), họ ngộ nhận hệ thống sắp hoàn thiện, dẫn đến "chốt cứng" kiến trúc và giao diện, bỏ qua việc đào sâu các nghiệp vụ cốt lõi và Non-functional requirements (NFRs).
- [x] **Ma trận Đánh đổi Chi phí - Lợi ích (Cost-Benefit Trade-off)**:
  - *Low-fi (Paper/Sketches)*: Chi phí tạo lập cực thấp ($\approx 10-15\%$ thời gian), tốc độ lặp (iteration velocity) cao, mức độ sẵn sàng vứt bỏ (throwaway readiness) cao $\rightarrow$ Ngăn chặn hiệu quả hiện tượng Idea Cementing.
  - *High-fi (Figma/Code)*: Chi phí bảo trì cao khi spec thay đổi, áp lực giao hàng sớm (premature release pressure), hạn chế phản hồi tiêu cực từ người dùng vì họ ngại chê thiết kế đẹp.

---

### FB-4: Cơ chế tích hợp Paper Prototyping (Low-fi) với Agile, User Stories & Backlog Grooming
- [x] **Mô hình phối hợp Sprint 0 & Just-in-Time (JIT) Discovery**:
  - Sử dụng Low-fi Paper Prototype / Wizard-of-Oz trong buổi Backlog Refinement / Grooming trước mỗi Sprint.
- [x] **Cơ chế Enriched User Story**:
  - User Story chuẩn: *As a [User], I want to [Action], So that [Value]*.
  - User Story bổ sung (Enriched): Đính kèm Low-fi Sketch Artifact + Thỏa thuận nghiệm thu trực quan (Visual Acceptance Criteria) $\rightarrow$ Giảm thiểu rework tới 30-40% trong giai đoạn coding.
- [x] **Phối hợp Proto-personas (JSERD 2019)**:
  - Tạo chân dung người dùng giả định để định hướng elicitation phiên họp sprint.

---

### FB-5: Đề xuất Thiết kế Thực nghiệm minh chứng giải quyết Research Gaps
- [x] **Mô hình Thực nghiệm Đề xuất (Quasi-Experimental Design)**:
  - Thiết kế 3 nhóm đối chứng (Control Group vs Experimental Groups):
    - Nhóm A: Textual Specifications thuần (SRS / User Stories không hình minh họa).
    - Nhóm B: Textual Specs + High-Fidelity Interactive Mockup.
    - Nhóm C: Textual Specs + Loud Interactive Paper Prototyping (LPP) kèm Think-Aloud.
- [x] **Hệ tiêu chí định lượng (Dependent Variables)**:
  - Tỉ lệ phát hiện yêu cầu thiếu (Missing Requirements Recall $\%$).
  - Tỉ lệ làm rõ yêu cầu mơ hồ (Ambiguity Clarification Rate $\%$).
  - Thời gian elicitation và tổng chi phí giờ công (Man-hours spent).
  - Chi phí làm lại sau bàn giao (Post-elicitation Rework Cost).
