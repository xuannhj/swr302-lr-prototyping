# Danh Mục 18 Tài Liệu Nghiên Cứu & Bảng Trích Xuất Dữ Liệu (SWR302 - RP6)

> **Đề tài**: *The Effect of Prototyping on Identifying Missing and Unclear Requirements*  
> **Sinh viên thực hiện**: Nguyễn Phạm Xuân Nhi (SE201170) — SWR302 (Software Requirements)  
> **Tài liệu tham khảo đối sánh**: 3 bài NCKH mẫu tại [`docs/sample_papers/`](sample_papers/)

---

## 1. Bảng Phân Loại & Danh Mục 18 Tài Liệu Nghiên Cứu (Corpus Mapping)

| TT | Mã Citation Key | Tên bài báo / Tài liệu | Tác giả & Năm | Nguồn / Venue | Nhóm | RQ liên quan | Trọng tâm học thuật & Vai trò |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| 1 | `bbau_re_book` | Requirements Engineering (Textbook) | BBAU Faculty | Textbook | Nền tảng | Toàn bộ | Sách giáo trình kiến thức nền về RE, chuẩn quy trình Elicitation & Validation. |
| 2 | `didar2018systematic` | Requirements elicitation techniques maturity: a systematic literature review | Didar et al. (2018) | IET Software | Background | RQ6.1 | SLR nền tổng quan so sánh độ trưởng thành của 18 kỹ thuật elicitation. |
| 3 | `bjarnason2023empirically` | An empirically based model of software prototyping: a mapping study and a multi-case study | Bjarnason, Lang & Mjöberg (2023) | Empirical Software Engineering, Springer | Core (Anchor) | RQ6.1 | **Anchor Paper**: Khung PAM 5 chiều (Purpose, Scope, Media, Exploration, Use); rủi ro *Premature Idea Cementing*. |
| 4 | `rueda2020requirements` | Requirements elicitation methods based on interviews in comparison: A family of experiments | Rueda, Panach & Distante (2020) | Information and Software Technology, Elsevier | Core (Anchor) | RQ6.2 | **Anchor Paper**: Bằng chứng thực nghiệm đối đầu Paper Prototyping vs JAD vs Unstructured Interview ($p=0.02$). |
| 5 | `abad2018loud` | Loud and Interactive Paper Prototyping in Requirements Elicitation: What is it Good for? | Abad et al. (2018) | IEEE EmpiRE Workshop | Background / Core | RQ6.3 | Đột phá NFRs: Loud Paper Prototyping (LPP) kết hợp Wizard-of-Oz & Think-Aloud ($p=0.001$). |
| 6 | `uv2023empirical` | An empirical experiment of a usability requirements elicitation method to design GUIs based on interviews | Ormeño, Panach & Pastor (2023) | Information and Software Technology, Elsevier | Core | RQ6.3 | Đo lường loại requirement (usability/UI) được làm rõ qua GUI mock-up ($p=0.000$, $\eta^2=0.274$). |
| 7 | `rej2022evolve` | How Do Requirements Evolve During Elicitation? An Empirical Study Combining Interviews and App Store Analysis | Ferrari, Spoletini & Debnath (2022) | Requirements Engineering Journal, Springer | Core | RQ6.1 | Làm rõ vai trò prototyping/interactive session trong việc validate và tiến hóa requirement khi đang elicit (42% modification/missing found). |
| 8 | `jserd2019protopersona` | Proto-persona & UX requirement elicitation for non-technical stakeholders | Soares et al. (2019) | JSERD | Background | RQ6.3 | Liên quan RQ6.3 về khía cạnh trải nghiệm người dùng (UX) và stakeholder phi kỹ thuật. |
| 9 | `antonelli2022iterative` | An Iterative and Collaborative Approach to Specify Scenarios using Natural Language | Antonelli et al. (2022) | WER (Workshop on RE, LatAm) | Core | RQ6.1 | Công cụ prototype hỗ trợ verify/refine kịch bản (scenario) lặp đi lặp lại bằng ngôn ngữ tự nhiên. |
| 10 | `bano2023videos` | Can Videos be Used to Communicate Non-functional Requirements? An Early Empirical Investigation | Bano, Zowghi & Ferrari (2023) | IEEE RE Conference (RE@Next) | Core | RQ6.3 | Prototype dạng video đối với NFR (yêu cầu phi chức năng) - bằng chứng thực nghiệm bối cảnh hóa. |
| 11 | `gupta2022strategic` | Strategic prototyping technology adoption in startups: framework, challenges, and opportunities | Gupta, Bjarnason & Gupta (2022) | IEEE IT Professional | Core | RQ6.1 | Mở rộng mô hình PAM sang bối cảnh công nghệ cao và các công ty khởi nghiệp (startups). |
| 12 | `acm2022proposal` | A Proposal for Enhancing Agile Requirements Engineering with Prototyping and Enriched User Stories | Keshk, Lucassen et al. (2022) | ACM FAME-CSE | Core | RQ6.1 / RQ6.2 | Tích hợp prototype + User Story (Enriched User Story) giảm 30-40% rework trong Agile Backlog Grooming. |
| 13 | `diaz2021gender` | Are requirements elicitation sessions influenced by participants' gender? | Díaz, Panach, Rueda, Ruiz & Pastor (2021) | Science of Computer Programming, Elsevier | Core | RQ6.2 | Mở rộng family-of-experiments cùng nhóm tác giả Anchor #2 - kiểm soát biến nhiễu (gender) khi so sánh kỹ thuật. |
| 14 | `cascon2025ambiguity` | Multi-Label Ambiguity Detection in Software Requirements Using Language Models | Cascon, Ferrari & Spoletini (2025) | IEEE CASCON | Core | RQ6.3 | Phân loại 4 nhóm mơ hồ (Ambiguity taxonomy: Lexical, Syntactic, Scope, Vagueness) chuẩn hóa thước đo "unclear requirement". |
| 15 | `hickey1998prototyping` | Prototyping for Requirements Elicitation and Validation: A Participative Prototype Evaluation Methodology | Hickey & Dean (1998) | AMCIS | Background | RQ6.1 | Đặt nền móng lý thuyết cho thuật ngữ *participative prototyping* và cognitive boundary objects. |
| 16 | `ferrari2016ambiguity` | Ambiguity and tacit knowledge in requirements elicitation interviews | Ferrari, Spoletini & Gnesi (2016) | Requirements Engineering Journal | Background | RQ6.3 | Định nghĩa ambiguity gốc và tri thức ẩn (tacit knowledge) trong phỏng vấn kỹ thuật yêu cầu. |
| 17 | `spoletini2018interview` | Interview Review: An Empirical Study on Detecting Ambiguities... | Spoletini et al. (2018) | REFSQ | Background | RQ6.3 | Phương pháp thực nghiệm đo lường sai lệch diễn giải ($\Delta_{\text{interp}}$) giữa analyst và reviewer. |
| 18 | `brill2010videos` | Videos vs. Use Cases: Can Videos Capture More Requirements Under Time Pressure? | Brill, Schneider & Knauss (2010) | REFSQ | Background | RQ6.2 | Bằng chứng thực nghiệm gốc: video (prototype trực quan) phát hiện nhiều yêu cầu hơn use case dạng văn bản. |

---

## 2. Bảng Trích Xuất Dữ Liệu Chuyên Sâu Các Bài Anchor (Deep Extraction Matrix)

### Nghiên cứu 1: Bjarnason et al. (2023) - Khung mô hình PAM
* **Tác giả & Năm**: Elizabeth Bjarnason, Michael Lang, and Markus Mjöberg (2023).
* **Nguồn**: *Empirical Software Engineering* (Springer), Vol. 28, Issue 5.
* **File PDF**: [`papers_pdf/03_bjarnason2023empirically_PAM_Model.pdf`](file:///e:/SEMESTER%205/swr302-lr-prototyping/papers_pdf/03_bjarnason2023empirically_PAM_Model.pdf).
* **RQ6.1 (Cách dùng)**: Đề xuất mô hình PAM gồm 5 chiều: *Purpose* (khám phá, căn chỉnh, kiểm chứng), *Scope* (độ rộng & độ sâu chức năng), *Media* (sketch giấy, mockup đến source code), *Use* (người review, tương tác trực tiếp/demo, scenario-based), và *Exploration Strategy* (đơn tuyến hoặc song song). Thực nghiệm trên 11 startup với 43 trường hợp áp dụng.
* **RQ6.2 (Đối đầu với Text)**: Khẳng định thực tế prototype hữu ích hơn hẳn văn bản đặc tả hình thức (*formal specifications*) để truyền đạt yêu cầu. Giảm thiểu rủi ro thiếu sót, mơ hồ và mâu thuẫn. Case study thực tế tại Company J chứng minh: khi đem prototype thử nghiệm tại hành lang ("corridor testing"), nhóm lập tức nhận ra đã bỏ sót nhiều yêu cầu nghiệp vụ nghiêm trọng (*"realised that we had missed several things"*).
* **RQ6.3 (Phân loại yêu cầu)**: Làm rõ xuất sắc: UI/UX, tính khả dụng (Usability), Customer Tasks/Flows, và PoC cho tính khả thi kỹ thuật (Technical Feasibility). Khó áp dụng kiểm chứng chất lượng phi chức năng sâu (Scalability, Robustness, Security).
* **Rủi ro & Gotchas**: 
  - *Premature Release Pressure*: Khách hàng thấy prototype đẹp mắt tưởng phần mềm đã hoàn thiện 90%, đòi bàn giao sớm trong khi kiến trúc ngầm chưa làm.
  - *Cementing Ideas Too Early*: Nếu vội vã code prototype bằng mã nguồn thật (source code) quá sớm, nhóm phát triển sẽ bị ngại đập đi xây lại, khóa chặt tư duy sai lầm.

### Nghiên cứu 2: Rueda et al. (2020) - Chuỗi Thực Nghiệm Đối Đầu
* **Tác giả & Năm**: Silvia Rueda, J. Ignacio Panach, and Damiano Distante (2020).
* **Nguồn**: *Information and Software Technology* (Elsevier), Vol. 126.
* **File PDF**: [`papers_pdf/04_rueda2020requirements_Family_Experiments.pdf`](file:///e:/SEMESTER%205/swr302-lr-prototyping/papers_pdf/04_rueda2020requirements_Family_Experiments.pdf).
* **RQ6.1 & Quy trình thực nghiệm**: Family of experiments gồm 4 replications (167 sinh viên, 30 nhóm) so sánh 3 phương pháp: Paper Prototyping, JAD, và Phỏng vấn phi cấu trúc qua 3 hệ thống (Hotel, Flight-sale, Cruiser management). Dùng phác thảo giấy (paper mock-ups) làm vật trung gian phỏng vấn.
* **RQ6.2 (Số liệu thực nghiệm & Phép kiểm Kruskal-Wallis)**:
  - *Phép kiểm thống kê*: Toàn bộ so sánh giữa 3 phương pháp sử dụng phép kiểm **Kruskal-Wallis** cho các mẫu độc lập.
  - *Tổng số lượng yêu cầu (Gross Volume)*: Paper Prototyping dẫn đầu với sự khác biệt có ý nghĩa thống kê ($p = 0.02$, effect size $\eta^2 = 0.08$). Kích thích trực quan giúp lôi ra các yêu cầu bị thiếu (missing requirements).
  - *Yêu cầu bị trùng lặp (Overlapping / Redundancy)*: Có ý nghĩa thống kê ($p = 0.03$, effect size $\eta^2 = 0.29$). JAD ít trùng lặp nhất nhờ có thư ký (scribe) ghi chép, phỏng vấn chay bị trùng nhiều nhất.
  - *Độ đầy đủ (Completeness - proxy cho missing)*: Không có khác biệt có ý nghĩa thống kê so với JAD ($p = 0.17$).
  - *Độ chính xác (Correctness / Quality - proxy cho unclear)*: Không có khác biệt có ý nghĩa thống kê so với JAD ($p = 0.59$).
  - *Thời gian chuẩn bị*: Vẽ giấy tốn trung bình 145 phút (median), thấp hơn JAD nhưng tổng hợp tài liệu lâu hơn phỏng vấn chay.
* **RQ6.3 (Phân loại yêu cầu)**: Hiệu quả vượt trội ở Functional Requirements và bố cục màn hình/giao diện (UI layout). Lép vế hoàn toàn ở Non-Functional Requirements (NFRs) (kết quả thấp nhất, trong khi JAD khơi gợi NFRs tốt nhất).
* **Hạn chế & Ghi chú nghiên cứu**:
  - *Ảo giác thị giác (Visual bias)*: Người tham gia bị cuốn vào nút bấm và màu sắc, bỏ quên logic ngầm và NFRs.
  - *Lực lượng thống kê thấp (Low Statistical Power)*: Độ đầy đủ và độ chính xác không đạt ý nghĩa thống kê ($p=0.17$ và $0.59$) do cỡ mẫu chỉ có 30 nhóm (cần tới 102 nhóm để đạt statistical power tối ưu nhằm phát hiện sự khác biệt).
  - Đối tượng là sinh viên đại học (cần mở rộng sang kỹ sư công nghiệp).

### Nghiên cứu 3: Abad et al. (2018) - Loud Paper Prototyping (LPP)
* **Tác giả & Năm**: Zahra Shakeri Hossein Abad et al. (2018).
* **Nguồn**: *IEEE 25th International Requirements Engineering Conference Workshops (REW / EmpiRE)*.
* **File PDF**: [`papers_pdf/05_abad2018loud_Interactive_Paper_Prototyping.pdf`](file:///e:/SEMESTER%205/swr302-lr-prototyping/papers_pdf/05_abad2018loud_Interactive_Paper_Prototyping.pdf).
* **RQ6.1 & Giao thức triển khai**: Đánh giá kỹ thuật Loud and Interactive Paper Prototyping (LPP) dựa trên Wizard of Oz (WOz) kết hợp Think-aloud protocol trên 183 người (50 nhóm phát triển Mobile App). So sánh 3 nhóm: LPP (tương tác + nói to suy nghĩ), SPP (tương tác im lặng), và NPP (họp thông thường không có prototype).
* **RQ6.2 (Bằng chứng số liệu)**:
  - Bổ sung yêu cầu mới (Additions): $p = 0.0001$.
  - Sửa đổi yêu cầu mơ hồ (Modifications): $p = 0.01$.
  - 36% nhóm làm rõ được FRs, 20% phát hiện thêm chức năng và luồng điều hướng bị bỏ sót (ví dụ: thiếu nút Back, chế độ survival mode).
* **RQ6.3 (Đột phá giải quyết điểm mù NFR)**:
  - Bắt trọn UI vượt trội ($p = 0.0001$).
  - Kết hợp Think-aloud giúp paper prototype bắt trọn NFRs về mặt Usability, Navigation và Learnability ($p = 0.001$ so với họp thông thường).
  - LPP vượt trội hơn SPP có ý nghĩa thống kê ở việc điều chỉnh Functional Requirements ($p = 0.01$).
* **Hạn chế**: Việc vừa nghĩ vừa nói làm chậm tốc độ người dùng, làm sai lệch thước đo thời gian học hỏi (learnability metrics); tiềm ẩn rủi ro thiên vị do người điều phối (facilitator bias).

### Nghiên cứu 4: Ormeño et al. (2023) - UREM (GUI Mockup & Usability Decision Tree)
* **Tác giả & Năm**: E. Ormeño, J. I. Panach, and O. Pastor (2023).
* **Nguồn**: *Information and Software Technology* (Elsevier), Vol. 157, 107147.
* **File PDF**: [`papers_pdf/06_uv2023empirical_GUI_Usability_Elicitation (1).pdf`](file:///e:/SEMESTER%205/swr302-lr-prototyping/papers_pdf/06_uv2023empirical_GUI_Usability_Elicitation%20(1).pdf).
* **RQ6.1 & Giao thức triển khai (How & Mechanism)**: Đánh giá phương pháp UREM (Usability Requirements Elicitation Method) kết hợp Low-fidelity GUI Paper Mockup và Cây quyết định (Decision Tree dựa trên hướng dẫn công thái học usability). Thiết kế thực nghiệm trong nhóm (Within-subjects design) gồm 48 người (24 cặp gồm 1 phân tích viên và 1 khách hàng) qua 2 giai đoạn (Phase 1 & Phase 2) trên 2 ứng dụng di động: Mobile Health (mHealth) và Mobile Banking (mBanking).
* **RQ6.2 (Bằng chứng đối đầu với phỏng vấn phi cấu trúc)**:
  - *Hiệu quả khơi gợi Usability (Effectiveness)*: UREM vượt trội có ý nghĩa thống kê cao ($p = 0.000$, effect size $\eta^2 = 0.274$, Statistical Power = 0.978), khơi gợi nhiều hơn 28.5% yêu cầu tính khả dụng so với phỏng vấn phi cấu trúc thông thường.
  - *Mức độ tuân thủ nguyên tắc (Guideline Adherence)*: Vượt trội áp đảo ($p = 0.000$, effect size $\eta^2 = 0.571$, Statistical Power = 1.000).
  - *Thời gian thực hiện (Efficiency)*: Không có khác biệt thống kê ($p = 0.220$), cho thấy UREM đạt chất lượng yêu cầu cao hơn hẳn mà không làm lãng phí thêm thời gian phỏng vấn.
* **RQ6.3 (Đặc thù loại yêu cầu làm rõ)**:
  - Làm rõ và cụ thể hóa xuất sắc các yêu cầu Usability / GUI (vốn là điểm mù của tài liệu văn bản và phỏng vấn chay).
  - Giải quyết triệt để các lỗi thiếu sót giao diện: thiếu dấu hoa thị `*` cho trường bắt buộc (mandatory fields), thiếu hộp thoại cảnh báo lỗi (modal error dialogs), thiếu danh sách chọn (dropdown) chống lỗi nhập liệu, và thiếu hướng dẫn tooltip/help-icon (`?`).
* **Hạn chế & Ghi chú nghiên cứu**: Mẫu thực nghiệm gồm sinh viên đại học và học viên thạc sĩ; hiệu suất thời gian có power thấp (0.230) và phụ thuộc vào bài toán. Prototype có cấu trúc giúp giải quyết điểm mù Usability nhưng đòi hỏi kỹ năng dẫn dắt logic của phân tích viên.

### Nghiên cứu 5: Ferrari, Spoletini & Debnath (2022) - Requirements Evolution & App Store Prototyping
* **Tác giả & Năm**: Alessio Ferrari, Paola Spoletini, and Sourav Debnath (2022).
* **Nguồn**: *Requirements Engineering Journal* (Springer), Vol. 27, Issue 4, pp. 489–519.
* **File PDF**: [`papers_pdf/07_rej2022evolve_Requirements_Evolution.pdf`](file:///e:/SEMESTER%205/swr302-lr-prototyping/papers_pdf/07_rej2022evolve_Requirements_Evolution.pdf).
* **RQ6.1 & Giao thức triển khai (How & Mechanism)**: Nghiên cứu thực nghiệm 2 giai đoạn trên 30 nhà phân tích yêu cầu (analysts) với bài toán Quản lý trại hè dã ngoại (Summer Camp Management System). 
  - *Phase I (Phỏng vấn lời nói)*: 30 analyst phỏng vấn khách hàng qua 2 vòng và viết 50-60 User Stories ban đầu.
  - *Phase II (Tương tác sản phẩm/mẫu tham chiếu)*: Analyst tải về và trực tiếp trải nghiệm 5 ứng dụng tương tự trên Google Play/App Store (đóng vai trò reference prototypes), đọc review người dùng và bổ sung 20 User Stories.
* **RQ6.2 (Bằng chứng đối đầu & Phát hiện yêu cầu bị thiếu)**:
  - *Tỷ lệ bảo tồn ý tưởng gốc (Conservation Rate)*: Sau phỏng vấn, chỉ có **30% đến 38%** ý tưởng ban đầu của khách hàng được giữ nguyên; hơn 60% còn lại bị biến đổi hoặc thêm mới (trong đó có tới **21% chủ đề hoàn toàn mới** do analyst tự sáng tạo).
  - *Khai quật yêu cầu bị thiếu (Missing Requirements)*: Khi được tương tác với sản phẩm/mẫu trực quan thực tế, analyst phát hiện và bổ sung thêm tới **42% yêu cầu mới** mà cả khách hàng lẫn analyst trong phòng họp trước đó hoàn toàn không hề nghĩ tới.
* **RQ6.3 (Đột phá Usability và NFRs)**:
  - Phỏng vấn chay chỉ tập trung vào chức năng nghiệp vụ nội bộ của khách hàng.
  - Khi tương tác trên giao diện sản phẩm thực tế, mức độ chú ý dành cho **Usability (Tính khả dụng) TĂNG VỌT THÊM 45%**.
  - Kéo theo sự xuất hiện của hàng loạt NFRs cốt lõi: Bảo mật (*Security*), Quyền riêng tư (*Privacy*), và Cổng thanh toán (*Online Payment*).
* **Hạn chế & Ghi chú nghiên cứu**: Giai đoạn 2 chỉ cho phép thêm mới (extension) mà chưa đo lường thao tác chỉnh sửa/xóa (edit/deletion); đối tượng thực nghiệm là sinh viên ngành kỹ thuật phần mềm đóng vai analyst với một khách hàng giả định.


