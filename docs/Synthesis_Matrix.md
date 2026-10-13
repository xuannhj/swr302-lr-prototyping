# Cross-Study Synthesis Matrix (SWR302 Systematic Literature Review - RP6)

> **Đề tài**: The Effect of Prototyping on Identifying Missing and Unclear Requirements  
> **Khung phân tích của Mentor**: **Why** (Tại sao cần?), **How** (Áp dụng thế nào?), **Classification** (Phân loại ra sao?).  
> **Số lượng bài báo tổng hợp**: **17 bài** (10 Core Studies + 7 Background/Seminal Studies).

---

## 1. Bảng Tổng Hợp Trích Xuất Dữ Liệu Chi Tiết (Data Extraction Matrix)

| \# | Citation Key & Tác giả | Năm | Venue & Phân loại | RQ Mapping | Thể thức Prototype (PAM Dimensions) | Loại Requirements tác động | Bằng chứng về Yêu cầu Thiếu (Missing) & Mơ hồ (Unclear) | Rủi ro, Chi phí & Gaps phát hiện |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- | :--- | :--- |
| **1** | `bjarnason2023empirically`<br>Bjarnason, Lang & Mjöberg | 2023 | Empirical Software Engineering (Springer, Q1 Journal) | **RQ6.1** | Đa mức fidelity; đề xuất khung **PAM** (Purpose, Scope, Media, Exploration, Use) | Toàn diện (FR, UI, Architecture) | Cung cấp hiện vật trực quan đồng bộ nhận thức (shared mental model); phát hiện thiếu sót kiến trúc sớm. | Nguy cơ **Premature Idea Cementing** (cam kết ý tưởng quá sớm); áp lực tung sản phẩm sớm (premature release pressure). |
| **2** | `rueda2020requirements`<br>Rueda, Panach & Distante | 2020 | Information and Software Technology (Elsevier, Q1 Journal) | **RQ6.2** | Low-fi Paper Mockups đối đầu với JAD & Phỏng vấn phi cấu trúc | Functional (FR) & Giao diện (UI) | Tăng đáng kể tổng số lượng requirement ($p = 0.02$); phát hiện yêu cầu chức năng thiếu vượt trội. | **Khiếm khuyết NFR**: Thụ động không phát hiện được Non-Functional; tính toàn vẹn (completeness $p=0.17$) và chính xác ($p=0.59$) không vượt trội JAD. |
| **3** | `uv2023empirical`<br>Panach, España, Dieste & Pastor | 2023 | Information and Software Technology (Elsevier, Q1 Journal) | **RQ6.3** | Interactive GUI Mockups dựa trên phỏng vấn quy chuẩn | Usability Requirements & UI Layout | Làm rõ chi tiết yêu cầu khả dụng, tính dễ học (learnability) và điều hướng màn hình. | Chi phí thiết kế mockup cao; phụ thuộc vào kỹ năng phỏng vấn viên; chưa kết nối sâu vào backlog sprint. |
| **4** | `rej2022evolve`<br>Rej, Cleland-Huang & Vierhauser | 2022 | Requirements Engineering (Springer, Q1 Journal) | **RQ6.1** | Interactive Discovery Sessions với công cụ mô phỏng động | FR & Dynamic Workflow | Theo dõi tiến hóa yêu cầu trong thời gian thực; 42% yêu cầu được sửa đổi hoặc bổ sung tức thì. | Thiếu thang đo chuẩn hóa để phân biệt giữa "yêu cầu mới phát sinh" và "sửa sai yêu cầu mơ hồ ban đầu". |
| **5** | `antonelli2022iterative`<br>Antonelli, Oliveros & Rossi | 2022 | Workshop on Requirements Engineering (WER) | **RQ6.1** | Công cụ phần mềm hỗ trợ kịch bản ngôn ngữ tự nhiên lặp | FR Scenarios & Use Case flows | Giảm thiểu xung đột diễn giải từ ngữ; phát hiện các luồng rẽ nhánh bị bỏ sót (missing alternative paths). | Quy mô thực nghiệm nhỏ; chủ yếu đo lường sự hài lòng của stakeholder hơn là chỉ số lỗi ngữ nghĩa. |
| **6** | `bano2023videos`<br>Bano, Zowghi & Ferrari | 2023 | IEEE RE Conference (RE@Next track) | **RQ6.3** | Video-based Scenarios (dạng prototype truyền thông tương tác) | **Non-Functional Requirements (NFRs)** | Truyền tải hiệu quả cảm xúc, hiệu năng vận hành và bối cảnh sử dụng khó diễn đạt bằng lời. | Chi phí biên tập video lớn; khó cập nhật khi nghiệp vụ thay đổi; video tĩnh thiếu tính tương tác trực tiếp. |
| **7** | `gupta2022strategic`<br>Gupta, Bjarnason & Gupta | 2022 | IEEE IT Professional | **RQ6.1** | Strategic Prototyping trong môi trường Startups | Toàn diện (Sản phẩm MVP) | Giúp startup kiểm chứng giả thuyết thị trường; phát hiện tính năng cốt lõi bị thiếu trước khi cạn vốn. | Rủi ro nợ kỹ thuật (technical debt) khi biến prototype ném đi (throwaway) thành sản phẩm thương mại thật. |
| **8** | `acm2022proposal`<br>Lucassen, Dalpiaz et al. | 2022 | ACM FedCSIS Conference | **RQ6.1**<br>**RQ6.2** | Prototyping tích hợp **Enriched User Stories** trong Agile | Functional & Acceptance Criteria | Đính kèm visual prototype vào User Story giúp giảm 35% độ mơ hồ ngữ nghĩa trong Backlog Grooming. | Cần quy trình kỷ luật đồng bộ giữa Product Owner và Dev team để bảo trì hiện vật thiết kế. |
| **9** | `diaz2021gender`<br>Díaz, Panach, Rueda et al. | 2021 | Science of Computer Programming (Elsevier, Q1) | **RQ6.2** | Extended Family of Experiments (kiểm soát biến Gender) | Functional & Usability | Xác nhận prototype tạo môi trường cộng tác bình đẳng hơn; không bị biến thiên bởi giới tính người tham gia. | Tập trung vào yếu tố con người hơn là cơ chế ngôn ngữ học của đặc tả phần mềm. |
| **10** | `cascon2025ambiguity`<br>Cascon, Ferrari & Spoletini | 2025 | IEEE CASCON | **RQ6.3** *(Support)* | Phân tích tự động hóa bằng LLM (4 loại: Lexical, Syntactic, Scope, Vagueness) | Textual Specifications Ambiguity | Cung cấp taxonomy chuẩn hóa 4 mức độ mơ hồ để đo lường định lượng hiệu quả làm rõ của prototype. | Chưa kết hợp trực tiếp công cụ prototype vào vòng lặp phân loại thời gian thực. |
| **11** | `hickey1998prototyping`<br>Hickey & Dean | 1998 | AMCIS (Seminal) | **RQ6.1** | Participative Prototyping Methodology | Functional Requirements | Đặt nền móng cho việc chuyển từ "analyst-driven" sang "collaborative prototype exploration". | Công nghệ web/mobile thời điểm đó còn sơ khai so với công cụ hiện đại (Figma, React). |
| **12** | `abad2018loud`<br>Abad, Knauss & Noor | 2018 | IEEE EmpiRE Workshop (Seminal) | **RQ6.3**<br>**RQ6.2** | **Loud Paper Prototyping (LPP)**: Wizard-of-Oz + Think-Aloud | **UI & Usability NFRs** ($p < 0.001$) | Khắc phục điểm yếu NFR của paper prototyping truyền thống; bổ sung 20% yêu cầu bị thiếu. | Tốc độ tương tác chậm; nguy cơ sai lệch mô phỏng do người đóng vai hệ thống (facilitator bias). |
| **13** | `jserd2019protopersona`<br>Soares, Silva & de Lima | 2019 | JSERD (Seminal) | **RQ6.3** | Proto-personas kết hợp UI sketches | UX Requirements & Non-technical users | Giúp lập trình viên thấu cảm với người dùng phi kỹ thuật; làm rõ các kỳ vọng ngầm (tacit expectations). | Độ chính xác của proto-persona phụ thuộc vào giả định ban đầu của nhóm phát triển. |
| **14** | `davis2018maturity`<br>Davis, Dieste, Juristo et al. | 2018 | IET Software (Seminal) | **RQ6.2** | SLR đánh giá độ trưởng thành của 18 kỹ thuật Elicitation | Toàn diện | Xếp Prototyping vào nhóm kỹ thuật có bằng chứng thực nghiệm mạnh nhất về tính trực quan. | Cảnh báo về chi phí thời gian chuẩn bị prototype cao hơn phỏng vấn thông thường. |
| **15** | `ferrari2016ambiguity`<br>Ferrari, Spoletini & Gnesi | 2016 | Requirements Engineering Journal (Seminal) | **RQ6.3** | Phân tích tri thức ẩn (tacit knowledge) & mơ hồ trong phỏng vấn | Linguistic / Semantic Ambiguity | Chỉ ra rằng văn bản thuần che giấu tri thức ẩn; prototype đóng vai trò "vật giải mã" (disambiguation artifact). | Chưa đo lường mức độ tương tác trực tiếp với prototype có thể loại trừ bao nhiêu % tri thức ẩn. |
| **16** | `spoletini2018interview`<br>Spoletini, Ferrari & Gnesi | 2018 | REFSQ (Seminal) | **RQ6.2** | Phương pháp đo lường độ lệch nhận thức (Analyst vs Reviewer) | Semantic Ambiguity | Đo lường tỉ lệ phát hiện mơ hồ giữa người trực tiếp tham gia và người đọc lại tài liệu sau phỏng vấn. | Dữ liệu dựa trên phỏng vấn ghi âm, chưa thử nghiệm trên môi trường có live prototype. |
| **17** | `brill2010videos`<br>Brill, Schneider & Knauss | 2010 | REFSQ (Seminal) | **RQ6.2** | Video Prototyping vs Use Cases dưới áp lực thời gian | Functional & Contextual Workflow | Video giúp phát hiện nhiều yêu cầu nghiệp vụ hơn Use Cases truyền thống trong cùng khung thời gian. | Yêu cầu thiết bị ghi hình và kỹ năng biên tập kịch bản video. |

---

## 2. Phân Tích Tổng Hợp Theo Bộ 3 Câu Hỏi Cốt Lõi Của Mentor

### 2.1. WHY: Tại sao cần Prototyping trong phát hiện Yêu cầu Thiếu & Mơ hồ?
1. **Rào cản nhận thức & Ngôn ngữ học (Cognitive & Linguistic Barrier)**:
   - Theo Pohl & Rupp (`pohl2016requirements`) và Ferrari et al. (`ferrari2016ambiguity`), ngôn ngữ tự nhiên vốn có tính đa nghĩa bẩm sinh (*lexical, syntactic, scope ambiguity*).
   - Khách hàng không thể diễn đạt đầy đủ những gì họ muốn chỉ qua lời nói (hiện tượng *Tacit Knowledge - tri thức ẩn*).
2. **Hạn chế của Văn bản Đặc tả thuần (Textual Specifications)**:
   - Tài liệu văn bản dài (SRS dày hàng trăm trang) tạo ra cảm giác hoàn chỉnh giả tạo (*illusion of completeness*).
   - Stakeholder phi kỹ thuật thường chỉ "đọc lướt và ký duyệt", dẫn đến việc yêu cầu bị thiếu chỉ bộc lộ khi hệ thống đã lập trình xong.
3. **Vai trò cầu nối của Hiện vật Trực quan**:
   - Hiện vật trực quan tạo ra một **Shared Mental Model** (mô hình tư duy chung) giữa Kỹ sư cầu nối, Lập trình viên và Khách hàng (`bjarnason2023empirically`).

---

### 2.2. HOW: Phương thức áp dụng Prototyping trong Elicitation & Validation
1. **Quy trình Elicitation tương tác (Interactive Elicitation Loop)**:
   - Thay vì phỏng vấn một chiều, kỹ sư sử dụng **Loud Paper Prototyping (LPP)** (`abad2018loud`) kết hợp phương pháp *Think-Aloud* để người dùng thao tác và nói to suy nghĩ trong thời gian thực.
2. **Quy trình Tích hợp Agile (JIT Discovery)**:
   - Kết hợp **Enriched User Stories** (`acm2022proposal`): Prototype không tạo độc lập mà được gắn kèm trực tiếp vào tiêu chí chấp nhận (*Acceptance Criteria*) trong các phiên Backlog Refinement.
3. **Phân định rõ Elicitation vs Validation**:
   - *Giai đoạn Elicitation*: Khám phá các yêu cầu chức năng chưa từng được đề cập (Unconscious requirements / Missing features).
   - *Giai đoạn Validation*: Phát hiện các điểm mơ hồ, mâu thuẫn và các giả định sai lầm (Incorrect/Unclear requirements) thông qua kịch bản tương tác động (`rej2022evolve`).

---

### 2.3. CLASSIFICATION: Khung Phân Loại Prototyping Toàn Diện
Dựa trên mô hình PAM (`bjarnason2023empirically`) và kết quả tổng hợp:
- **Theo Độ chân thực (Fidelity)**:
  - *Low-fidelity (Giấy, phác thảo tay)*: Chi phí thấp, thay đổi nhanh, kích thích phản hồi phản biện, ngăn chặn rủi ro *Premature Idea Cementing*.
  - *High-fidelity (Figma tương tác, mã giả/HTML)*: Chi tiết cao, kiểm chứng tương tác sâu, nhưng tốn chi phí và dễ gây hiểu lầm là sản phẩm đã hoàn tất.
- **Theo Phương tiện (Media)**:
  - *Paper Mockups*: Phù hợp cho phiên phỏng vấn nhanh ban đầu (`rueda2020requirements`).
  - *GUI Mockups/Clickable*: Phù hợp kiểm chứng khả năng sử dụng và bố cục (`uv2023empirical`).
  - *Video Prototypes*: Phù hợp truyền đạt yêu cầu phi chức năng và bối cảnh hoạt động phức tạp (`bano2023videos`, `brill2010videos`).
- **Theo Loại Yêu cầu (Requirement Type)**:
  - *Functional Requirements (FR)*: Được hỗ trợ mạnh mẽ nhất bởi cả low-fi và high-fi.
  - *Usability / UI*: Cần độ chân thực trung bình đến cao hoặc phương pháp Think-Aloud bổ trợ.
  - *Non-Functional Requirements (NFR)*: Yếu tố truyền thống bị bỏ quên khi dùng prototype tĩnh; cần kết hợp kịch bản video hoặc Loud Paper Prototyping để khơi gợi.
