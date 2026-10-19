import openpyxl

wb = openpyxl.load_workbook('docs/Synthesis_Matrix_RP6.xlsx')
ws = wb.active

# ==========================================
# ROW 23: lim2008anatomy
# ==========================================
r23 = 23
ws.cell(r23, 1).value = '=A22+1'
ws.cell(r23, 2).value = 'lim2008anatomy'
ws.cell(r23, 3).value = 'The Anatomy of Prototypes: Prototypes as Filters, Prototypes as Manifestations of Design Ideas'
ws.cell(r23, 4).value = 'Youn-Kyung Lim, Erik Stolterman, and Josh Tenenberg (2008)'
ws.cell(r23, 5).value = 'ACM Transactions on Computer-Human Interaction (TOCHI), Vol. 15, No. 2, Article 7, pp. 1–27'
ws.cell(r23, 6).value = 'PDF Downloaded (papers_pdf/)'
ws.cell(r23, 7).value = 'https://doi.org/10.1145/1375761.1375762'

ws.cell(r23, 8).value = (
    'Định nghĩa bản thể luận (Ontology) mang tính bước ngoặt: Prototype là Bộ lọc (Filter) thám hiểm không gian thiết kế '
    'và là Hiện thân (Manifestation) của ý tưởng. Sức mạnh cốt lõi của prototype nằm ở sự "CHƯA HOÀN THIỆN" (Incompleteness as Strength). '
    'Prototype hữu ích chính ở những gì nó CỐ TÌNH BỎ QUA (không code, không tô vẽ chi tiết thừa) để tập trung nhận thức vào các chất lượng cần kiểm chứng. '
    '5 chiều lọc (Filtering Dimensions): Appearance, Data, Functionality, Interactivity, Spatial structure.'
)

ws.cell(r23, 9).value = (
    'Khẳng định văn bản đặc tả hình thức (textual specifications) làm quá tải nhận thức vì nhồi nhét mọi thứ cùng lúc. '
    'Nguyên lý kinh tế của tạo mẫu (Economic Principle of Prototyping): Bản mẫu tốt nhất là bản mẫu đơn giản nhất và hiệu quả nhất, '
    'làm cho các tiềm năng và giới hạn của ý tưởng thiết kế trở nên hiển hiện và đo lường được. '
    'Giúp phát hiện các yêu cầu bị bỏ sót (Missing Requirements) bằng cách cô lập và thử nghiệm từng chiều tương tác độc lập.'
)

ws.cell(r23, 10).value = (
    'Làm rõ xuất sắc các yêu cầu Tương tác (Interactivity), Luồng chức năng (Functionality), Bố cục không gian (Spatial structure) '
    'và Trải nghiệm ngoại quan (Appearance). Cảnh báo: Nếu tăng độ trung thực quá sớm trên tất cả các chiều, nhóm phát triển sẽ bị '
    'rơi vào bẫy "đóng băng tư duy" và tốn kém nguồn lực vô ích.'
)

ws.cell(r23, 11).value = (
    'Khung lý thuyết giải phẫu Prototype (The Anatomy of Prototypes) kiểm chứng qua 2 nghiên cứu điển hình sâu sắc trong thiết kế tương tác '
    'và kỹ nghệ phần mềm. Cung cấp nền tảng triết học trực tiếp cho mô hình PAM 5 chiều (Bjarnason et al., 2023).'
)

ws.cell(r23, 12).value = (
    'Bài báo thiên về lý thuyết bản thể luận và thiết kế tương tác (HCI/Design Theory), không cung cấp các phép kiểm định thống kê suy diễn (p-value); '
    'cần kết hợp với các nghiên cứu thực nghiệm kiểm định trong SE.'
)

ws.cell(r23, 13).value = """Bản thể luận về Prototype (Why?):
- Lỗ hổng trước 2008: Ngành công nghệ chỉ coi prototype là công cụ kiểm thử thụ động ở cuối chu trình (Usability Testing), chia thô sơ Lo-Fi vs Hi-Fi.
- Lim et al. tái định nghĩa: Prototype là công cụ tư duy khám phá (Design-Thinking Enabler) xuyên suốt toàn bộ quá trình phát triển."""

ws.cell(r23, 14).value = """Cơ chế Bộ lọc (How?):
- Incompleteness: Sự chưa hoàn thiện giúp người thiết kế lọc bỏ các chi tiết kỹ thuật phức tạp, giải phóng tải nhận thức để tập trung vào luồng tác vụ người dùng.
- Manifestation: Hiện thân hóa ý tưởng trừu tượng thành vật thể cụ thể qua 3 yếu tố: Vật liệu (Material), Độ phân giải (Resolution), và Phạm vi (Scope)."""

ws.cell(r23, 15).value = """Đóng góp cốt lõi cho đề tài SLR:
- Cung cấp cơ sở lý thuyết gốc giải thích vì sao Paper Prototype lôi được Missing Requirements trong RQ6.1 & RQ6.2.
- Giải thích hiện tượng Premature Idea Cementing khi vi phạm Nguyên lý kinh tế của tạo mẫu. Đóng góp vào Section I và Section III-A."""


# ==========================================
# ROW 24: inayat2015systematic
# ==========================================
r24 = 24
ws.cell(r24, 1).value = '=A23+1'
ws.cell(r24, 2).value = 'inayat2015systematic'
ws.cell(r24, 3).value = 'A systematic literature review on agile requirements engineering practices and challenges'
ws.cell(r24, 4).value = 'Irum Inayat, Siti Salwah Salim, Sabrina Marczak, Maya Daneva, and Shahaboddin Shamshirband (2015)'
ws.cell(r24, 5).value = 'Computers in Human Behavior (Elsevier), Vol. 51, Part B, pp. 915–929'
ws.cell(r24, 6).value = 'PDF Downloaded (papers_pdf/)'
ws.cell(r24, 7).value = 'https://doi.org/10.1016/j.chb.2014.10.046'

ws.cell(r24, 8).value = (
    'Nghiên cứu tổng quan hệ thống (SLR) toàn diện xác định 17 thực hành Agile RE và 8 thách thức lớn. '
    'Xếp Prototyping (Thực hành số 8) là công cụ trọng yếu để xem xét đặc tả yêu cầu với khách hàng và thu nhận phản hồi kịp thời trước mỗi Sprint. '
    'Cung cấp cho khách hàng "Bản thiết kế trực quan (Visual Blueprint)" của sản phẩm, giúp chuyển dịch việc thẩm định yêu cầu (Validation) lên sớm ngay từ đầu chu kỳ.'
)

ws.cell(r24, 9).value = (
    'Bóc trần nghịch lý của Agile RE: User Stories ngắn gọn giúp linh hoạt nhưng dẫn đến điểm mù "Minimal Documentation", '
    'hiểu lầm từ khách hàng đại diện (Surrogate Customers) và làm gia tăng khối lượng làm lại (Massive Rework). '
    'Prototyping đứng đầu trong các thực hành giúp giảm thiểu Rework và hóa giải mâu thuẫn yêu cầu. '
    'Trích dẫn định lý Tomayko (2002): "With prototyping, there are no wrong requirements; the only requirements are those waiting to be discovered."'
)

ws.cell(r24, 10).value = (
    'Chỉ ra điểm yếu chí mạng của User Stories thông thường: Chỉ tập trung vào tính năng bề mặt của hệ thống (System/Product Features), '
    'bỏ quên hoàn toàn các yêu cầu phi chức năng (NFRs như Security, Performance, Scalability). '
    'Prototyping kết hợp Acceptance Tests và User Stories giúp bù đắp lỗ hổng này.'
)

ws.cell(r24, 11).value = (
    'Tổng hợp từ hàng chục nghiên cứu thực nghiệm công nghiệp. Chứng minh Prototyping kết hợp Face-to-face communication là cặp đôi '
    'hoàn hảo giải quyết triệt để khoảng cách giao tiếp (Communication Gap) và hiện tượng phình phạm vi (Overscoping) của RE truyền thống.'
)

ws.cell(r24, 12).value = (
    'Cảnh báo: Tạo mẫu nhiều bản High-fidelity Prototypes trong Agile có thể tốn kém chi phí quá mức (prohibitively expensive); '
    'cần áp dụng Low-fi và Rapid Prototyping trong các Sprint đầu.'
)

ws.cell(r24, 13).value = """Thách thức sống còn trong Agile RE (Why?):
- RE truyền thống bị bế tắc vì tài liệu SRS quá dày và khó thẩm định.
- Agile chuyển sang User Stories nhưng lại mắc bẫy tài liệu quá sơ sài, thiếu vắng NFRs và gây bùng nổ rework khi hiểu lầm yêu cầu."""

ws.cell(r24, 14).value = """Prototyping giải cứu Agile RE (How?):
- Prototyping cung cấp "Visual Blueprint" cụ thể hóa User Story.
- Khách hàng không cần phải đọc tài liệu kỹ thuật phức tạp mà trực tiếp trải nghiệm bản mẫu, phát hiện yêu cầu còn thiếu và chốt tiêu chí nghiệm thu (Acceptance Criteria)."""

ws.cell(r24, 15).value = """Đóng góp cốt lõi cho đề tài SLR:
- Cung cấp bằng chứng thực nghiệm cấp độ SLR bảo vệ cho RQ6.2.
- Là cơ sở lý thuyết trực tiếp cho đề xuất "Enriched User Stories" (Keshk 2022) tại Section VI-A của bài báo."""


# ==========================================
# ROW 25: berry2003contract
# ==========================================
r25 = 25
ws.cell(r25, 1).value = '=A24+1'
ws.cell(r25, 2).value = 'berry2003contract'
ws.cell(r25, 3).value = 'From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity'
ws.cell(r25, 4).value = 'Daniel M. Berry, Erik Kamsties, and Michael M. Krieger (2003)'
ws.cell(r25, 5).value = 'Technical Report / Reference Handbook, University of Waterloo & University of Essen, 80 pages'
ws.cell(r25, 6).value = 'PDF Downloaded (papers_pdf/)'
ws.cell(r25, 7).value = 'https://cs.uwaterloo.ca/~dberry/handbook/ambiguityHandbook.pdf'

ws.cell(r25, 8).value = (
    'Cẩm nang kinh điển của GS. Daniel M. Berry thiết lập mối liên hệ giữa soạn thảo hợp đồng pháp lý và viết đặc tả yêu cầu phần mềm (SRS). '
    'Khảo sát chứng minh 71.8% tài liệu yêu cầu được viết bằng ngôn ngữ tự nhiên thông thường (Common Natural Language), '
    'biến sự mơ hồ (Ambiguity) thành nguồn gốc số 1 của lỗi phần mềm. '
    'Đề xuất việc kết hợp ngôn ngữ tự nhiên với các biểu diễn trực quan (Diagrams, Wireframes, Formulae) để khử mơ hồ.'
)

ws.cell(r25, 9).value = (
    'Phát hiện hiện tượng tâm lý học ngôn ngữ nguy hiểm nhất: "Giải mơ hồ vô thức" (Unconscious Disambiguation). '
    'Người đọc tự động hiểu câu theo nghĩa đầu tiên xuất hiện trong đầu và tin chắc đó là nghĩa duy nhất, '
    'dẫn đến việc PO và Dev hiểu theo hai hướng hoàn toàn trái ngược nhau mà không hề hay biết! '
    'Văn bản thô (SRS/User Story) không thể tự triệt tiêu được bẫy này; cần Prototype làm vật đối chứng cụ thể.'
)

ws.cell(r25, 10).value = (
    'Thiết lập Khung phân loại 4 loại mơ hồ ngôn ngữ học chuẩn mực thế giới: '
    '1. Structural/Syntactic Ambiguity (Mơ hồ Cấu trúc/Cú pháp). '
    '2. Scope/Semantic Ambiguity (Mơ hồ Phạm vi Lượng từ). '
    '3. Anaphoric/Pragmatic Ambiguity (Mơ hồ Đại từ Thay thế & Ngữ cảnh). '
    '4. Vagueness/Generality (Mơ hồ Định tính & Ranh giới mập mờ).'
)

ws.cell(r25, 11).value = (
    'Cung cấp định nghĩa hình thức và hàng trăm ví dụ thực tế về các cạm bẫy ngôn từ trong SRS. '
    'Là nền tảng lý thuyết trực tiếp cho toàn bộ các nghiên cứu về phát hiện mơ hồ sau này trong RE (Ferrari 2016, Spoletini 2018, Cascon 2025).'
)

ws.cell(r25, 12).value = (
    'Cẩm nang tập trung vào phân tích ngôn ngữ học và các quy tắc viết văn bản; việc tự động hóa phát hiện mơ hồ thời điểm 2003 còn sơ khai '
    '(ngày nay đã được AI/LLM giải quyết như trong Cascon 2025).'
)

ws.cell(r25, 13).value = """Cội nguồn của sự mơ hồ trong RE (Why?):
- 71.8% yêu cầu viết bằng ngôn ngữ tự nhiên vốn chứa đầy sự đa nghĩa.
- "Unconscious Disambiguation" khiến các bên tưởng mình đã thống nhất nhưng thực tế đang hiểu sai lệch hoàn toàn."""

ws.cell(r25, 14).value = """Taxonomy 4 loại mơ hồ (How?):
- Phân loại rõ ràng 4 loại lỗi: Structural (cấu trúc ngữ pháp), Scope (phạm vi lượng từ), Anaphoric (đại từ không rõ tiền ngữ), và Vagueness (tính từ mập mờ).
- Đặt ra các chiến lược phát hiện và né tránh mơ hồ."""

ws.cell(r25, 15).value = """Đóng góp cốt lõi cho đề tài SLR:
- Là NỀN TẢNG LÝ THUYẾT TRỰC TIẾP cho Bộ Checklist 4 loại mơ hồ trong Thực nghiệm Pilot Test của Nhi (Section VI-B).
- Giải thích cơ chế vì sao Wireframe triệt tiêu được 93.3% mơ hồ ngôn từ. Đóng góp vào Section III-B, Section V và Section VI-B."""

wb.save('docs/Synthesis_Matrix_RP6.xlsx')
print('Rows 23 (Lim 2008), 24 (Inayat 2015), and 25 (Berry 2003) updated successfully in docs/Synthesis_Matrix_RP6.xlsx!')
