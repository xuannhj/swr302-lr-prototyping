# CẨM NANG BẢO VỆ & TRẢ LỜI MENTOR / GIẢNG VIÊN
## BÀI SYSTEMATIC LITERATURE REVIEW (SWR302 - RP6)
> **Đề tài**: *The Effect of Prototyping on Identifying Missing and Unclear Requirements*  
> **Sinh viên thực hiện**: Nguyễn Phạm Xuân Nhi (SE201170) — Trường Đại học FPT TP.HCM  

---

## 🌟 1. CÂU CHUYỆN CỐT LÕI CỦA BÀI BÁO (Tóm tắt trong 3 câu)
> 1. Đặc tả yêu cầu bằng văn bản truyền thống (SRS/User Story) luôn mắc phải bẫy ngôn từ và tri thức ẩn (*tacit knowledge*), dẫn đến việc bỏ sót và hiểu sai yêu cầu.  
> 2. Prototyping đóng vai trò là một **mỏ neo nhận thức trực quan (shared cognitive artifact)** giúp kích thích người dùng và nhà phân tích phát hiện thêm tới **42% yêu cầu bị thiếu** và triệt tiêu mơ hồ giao diện.  
> 3. Tuy nhiên, prototype **không phải là viên đạn bạc thần kỳ**: nếu chỉ nhìn màn hình tĩnh thì vẫn bị "mù" yêu cầu phi chức năng (NFRs) và logic ngầm, do đó phải kết hợp **nói to suy nghĩ (Think-Aloud)** và gắn vào **Enriched User Stories** để cắt giảm 30–40% làm lại (*rework*) trong Agile.

---

## 🎯 2. TRẢ LỜI 3 CÂU HỎI NGHIÊN CỨU (RESEARCH QUESTIONS)

### 📌 RQ6.1: Prototypes được sử dụng như thế nào để hỗ trợ requirements elicitation và validation?
* **Khung mô hình PAM (Bjarnason et al., 2023 - Springer)**:
  * Phân rã hoạt động tạo mẫu thành 5 chiều: *Purpose* (Mục đích), *Scope* (Độ rộng/sâu), *Media* (Phương tiện từ giấy đến code), *Use* (Tương tác trực tiếp/kịch bản), và *Exploration Strategy* (Đơn tuyến/song song).
* **Hai chế độ vòng đời**:
  * **Elicitation Mode**: Biến tri thức từ *Vô thức sang Có ý thức*. Người dùng không biết mình muốn gì cho đến khi nhìn thấy và bấm thử trên màn hình.
  * **Validation Mode**: Thẩm định và tiến hóa yêu cầu. Thực nghiệm của **Ferrari et al. (2022 - Springer REJ)** chứng minh: chỉ có 30%–38% câu chữ ban đầu được giữ nguyên, tương tác với prototype mẫu giúp **phát hiện thêm 42% yêu cầu bị thiếu**.

---

### 📌 RQ6.2: Sử dụng prototype có giúp phát hiện missing/unclear requirements tốt hơn chỉ dùng text không?
* **Thực nghiệm đối đầu kinh điển của Rueda et al. (2020 - Elsevier)** (*167 sinh viên, 30 nhóm, 3 hệ thống*):
  * **Tổng số lượng yêu cầu (Gross Volume)**: Paper Prototype vượt trội có ý nghĩa thống kê so với JAD và Phỏng vấn ($p = 0.02, \eta^2 = 0.08$). Thao tác trực quan kích thích người dùng tự giác nói ra các yêu cầu bị bỏ sót.
  * **Độ đầy đủ ($p = 0.17$) và Độ chính xác ($p = 0.59$)**: Không có sự khác biệt có ý nghĩa thống kê so với JAD.
  * **Lý do khoa học (Selective Visual Bias)**: Người dùng bị "ảo giác thị giác", chỉ mải mê xem nút bấm và giao diện đẹp mắt mà quên mất các thuật toán ngầm, ràng buộc toàn vẹn cơ sở dữ liệu.
  * **Môi trường bình đẳng (Díaz et al., 2021 - Elsevier)**: Trong khi mô hình quy trình BPMN bị chi phối bởi giới tính ($p = 0.018$), thì **Prototype tạo ra một môi trường tương tác bình đẳng giới tuyệt đối ($p = 0.132$)**, xóa bỏ sự lấn át của những người nói to trong phòng họp.

---

### 📌 RQ6.3: Những loại requirements nào được làm rõ tốt hơn thông qua prototype?
* **Functional Requirements (FR)**: Trực quan hóa giúp người dùng đi qua từng luồng giao dịch, phát hiện ngay các điều kiện Else, kiểm tra dữ liệu đầu vào và các trường hợp ngoại lệ bị bỏ sót.
* **Usability / GUI Requirements**: 
  * **Ormeño et al. (2023 - Elsevier)** chứng minh phương pháp UREM (GUI Mockup + Cây quyết định) nâng cao vượt bậc hiệu quả thu thập usability ($p = 0.000, \eta^2 = 0.274$) mà không tốn thêm thời gian ($p = 0.220$).
  * Giải quyết dứt điểm các lỗi thiếu dấu `*` trường bắt buộc, thiếu popup cảnh báo lỗi, thiếu dropdown.
* **Non-Functional Requirements (NFR - Bước đột phá điểm mù)**:
  * Prototype giấy tĩnh vốn bị "mù" NFRs. Nhưng bài báo chứng minh 2 giải pháp cứu vớt:
    1. **Loud Paper Prototyping (Abad et al., 2018 - IEEE)**: Bắt người dùng vừa bấm giấy vừa nói to suy nghĩ (Think-Aloud) $\rightarrow$ Thu thập NFRs về Usability, Navigation, Learnability vượt trội ($p = 0.001$).
    2. **Video-based Prototyping (Bano et al., 2023; Brill et al., 2010)**: Video thể hiện bối cảnh rung lắc, tiếng ồn, áp lực thời gian để người xem cảm nhận được yêu cầu về độ trễ và an toàn.

---

## 🏛️ 3. PHÂN TÍCH CHI TIẾT TỪNG SECTION TRONG BÀI BÁO

| Section | Tên mục | Nội dung trọng tâm em đã làm | Bằng chứng học thuật then chốt |
| :---: | :--- | :--- | :--- |
| **I** | **Introduction** | Đặt vấn đề bằng chuẩn **IREB CPRE (Pohl & Rupp)**; định nghĩa 4 thuật ngữ; đưa 3 RQs theo khung phân tích 3 phần (*Rationale, Protocol, Classification*). | Chuẩn IREB Principle 4 (Đổi hình thức tài liệu để phá vỡ ảo giác đầy đủ). |
| **II** | **Review Methodology** | Quy trình SLR theo **Kitchenham (2007)** & **PRISMA**; tìm kiếm trên 4 thư viện điện tử lớn (IEEE, ACM, ScienceDirect, Springer) thu được 312 bài thô $\rightarrow$ Phễu 5 bước chốt đúng **18 bài** (10 Core + 8 Foundational). | Table I (Tiêu chuẩn chọn/loại) & Table II (Phễu lọc số lượng). |
| **III** | **Thematic Review** | Tổng hợp theo chiều dọc (themes): Khung PAM 5 chiều; Phân biệt Elicitation vs Validation; Phân hóa theo 4 nhóm yêu cầu (FR, GUI, NFR Usability, NFR Context). | Table III; Case study Company J; Số liệu 42% missing (Ferrari 2022); UREM $p=0.000$ (Ormeño 2023); LPP $p=0.001$ (Abad 2018). |
| **IV** | **Comparative Analysis** | Đối sánh thực nghiệm trực diện: Prototype vs Text SRS vs JAD vs Phỏng vấn; Bóc tách hiện tượng "ảo giác thị giác"; Chứng minh tính bình đẳng giới. | Table IV; Thống kê Kruskal-Wallis của Rueda 2020 ($p=0.02, p=0.17, p=0.59$); Kiểm định giới tính Díaz 2021 ($p=0.132$). |
| **V** | **Research Gaps** | Phân loại 4 nhóm mơ hồ (*Cascon 2025, Berry 2003*); Cảnh báo 2 rủi ro của Hi-Fi prototype (*Premature Idea Cementing & Release Pressure*); Đưa giải pháp **Enriched User Stories** giảm 30-40% rework (*Keshk 2022*); Đánh giá 4 Threats to Validity. | 4 loại mơ hồ (Lexical, Syntactic, Scope, Vagueness); Nguyên tắc: Lo-Fi khám phá, Hi-Fi chỉ dùng xác thực trước khi code. |
| **VI** | **Proposed Directions** | Đề xuất 3 hướng nghiên cứu khả thi ở bậc đại học / đồ án tốt nghiệp: (1) Thực nghiệm Enriched User Story trên đồ án sinh viên; (2) Checklist phát hiện mơ hồ cho Backlog Grooming; (3) Ứng dụng Think-Aloud vào Wireframe để bắt NFR. | Phù hợp năng lực sinh viên đại học, đo lường trực tiếp trên Sprint Backlog. |
| **VII** | **Conclusion** | Tóm lược cô đọng đáp án cho 3 RQs kèm đầy đủ 6 chỉ số $p$-value; Đưa khuyến nghị vòng đời hoàn thiện. | Vừa khít đúng 8.0 trang chuẩn IEEEtran conference paper. |

---

## 💡 4. CÁC CON SỐ "MỎ NEO" CẦN HỌC THUỘC ĐỂ TRẢ LỜI MENTOR
* **42%**: Tỷ lệ yêu cầu bị thiếu được phát hiện thêm nhờ tương tác với prototype (*Ferrari et al., 2022*).
* **45%**: Mức độ chú ý dành cho Usability tăng vọt khi có prototype (*Ferrari et al., 2022*).
* **$p = 0.02$**: Paper prototype phát hiện tổng số lượng yêu cầu vượt trội hơn JAD và Phỏng vấn (*Rueda et al., 2020*).
* **$p = 0.000$**: Mockup giao diện kết hợp hướng dẫn giúp bắt trọn yêu cầu Usability (*Ormeño et al., 2023*).
* **$p = 0.001$**: Loud Paper Prototyping (kèm Think-Aloud) bắt trọn NFRs so với họp thông thường (*Abad et al., 2018*).
* **$p = 0.132$**: Prototype xóa bỏ hoàn toàn rào cản thiên vị giới tính trong giao tiếp yêu cầu (*Díaz et al., 2021*).
* **30%–40%**: Khối lượng làm lại (*rework*) được cắt giảm trong Agile nhờ Enriched User Stories (*Keshk et al., 2022*).
