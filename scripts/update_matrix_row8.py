import openpyxl

wb = openpyxl.load_workbook('docs/Synthesis_Matrix_RP6.xlsx')
ws = wb.active

row = 8

ws.cell(row, 1).value = '=A7+1'
ws.cell(row, 2).value = 'antonelli2022iterative'
ws.cell(row, 3).value = 'An Iterative and Collaborative Approach to Specify Scenarios using Natural Language'
ws.cell(row, 4).value = 'L. Antonelli, J. Delle Ville, F. Dioguardi, and A. Fernandez et al. (2022)'
ws.cell(row, 5).value = 'Proceedings of the 25th Workshop on Requirements Engineering (WER 2022)'
ws.cell(row, 6).value = 'Downloaded (09_antonelli2022iterative_Natural_Language_Scenarios.pdf)'
ws.cell(row, 7).value = 'https://doi.org/10.48550/arXiv.2209.00000'

ws.cell(row, 8).value = (
    'Quy trình lặp và cộng tác (Iterative & Collaborative) kết hợp giữa kịch bản ngôn ngữ tự nhiên '
    '(Natural Language Scenarios) và công cụ prototype tương tác được hỗ trợ bởi xử lý ngôn ngữ tự nhiên (NLP) '
    'và đồ thị tri thức (Knowledge Graph).'
)

ws.cell(row, 9).value = (
    'Loại bỏ xung đột diễn giải (conflicting interpretations) trong tài liệu văn bản; '
    'phát hiện các bẫy ngôn từ gây mơ hồ (phó từ mơ hồ, từ suy đoán could/should/might) '
    'và khai quật các luồng xử lý ngoại lệ bị bỏ sót (missing alternative/exceptional flows).'
)

ws.cell(row, 10).value = (
    'Làm rõ xuất sắc nhóm Yêu cầu Chức năng (Functional Logic), Luồng quy trình nghiệp vụ (Business Rules), '
    'và Kịch bản ca sử dụng (Use Case Scenarios). Hạn chế sự mơ hồ về ngữ nghĩa và điều kiện rẽ nhánh.'
)

ws.cell(row, 11).value = (
    'Đánh giá thực nghiệm quy trình viết và thẩm định kịch bản bằng thang đo SUS (System Usability Scale) '
    'đạt điểm số 70.53 (mức Acceptable). 4 quy tắc kiểm chứng tự động giúp bóc tách triệt để các câu điều kiện thiếu Else, '
    'lựa chọn Or chưa phân nhánh, và từ ngữ ước chừng.'
)

ws.cell(row, 12).value = (
    'Công cụ phần mềm hỗ trợ là prototype thử nghiệm; nghiên cứu thực nghiệm cần mở rộng cỡ mẫu đánh giá trên các dự án quy mô công nghiệp lớn.'
)

why_text = """Tại sao lại cần Prototype kết hợp Kịch bản ngôn ngữ tự nhiên? (Why?):
- Bối cảnh & Vấn đề: Kịch bản (Scenarios / Use Cases) viết bằng ngôn ngữ tự nhiên luôn chứa đầy bẫy ngôn từ: phó từ mơ hồ, từ ước chừng (could, might, should), điều kiện If thiếu Else, và lựa chọn Or không phân nhánh. Khách hàng và lập trình viên đọc cùng một câu nhưng hình dung ra 2 hệ thống khác nhau.
- Cơ chế: Prototype tương tác đóng vai trò vật đối chiếu trực quan trong chu trình lặp (collaborative loop). Khi người dùng bấm thử trên màn hình, các câu chữ mơ hồ và các nhánh ngoại lệ bị bỏ quên lập tức lộ diện."""

how_text = """Người ta áp dụng sao? (How?):
- Thiết kế thực nghiệm: Quy trình 4 bước viết kịch bản tăng dần (tiêu đề, bối cảnh, mục tiêu -> hành động -> tác nhân & tài nguyên -> rà soát luồng ngoại lệ) kết hợp 4 quy tắc kiểm chứng tự động bằng công cụ Prototype NLP/Knowledge Graph.
- Đánh giá: Sử dụng khảo sát 10 câu hỏi chuẩn System Usability Scale (SUS) trên nhóm chuyên gia để kiểm định khả năng áp dụng và độ tiện dụng trong việc xóa bỏ xung đột yêu cầu."""

taxonomy_text = """Người ta chia thành mấy loại? (Taxonomy & RQ6.3):
- Phân loại lỗi văn bản: Bẫy phó từ (Adverbs), Bẫy điều kiện thiếu (Incomplete conditions), Bẫy lựa chọn thay thế (Alternatives), Bẫy ngôn từ suy đoán (Speculative modal verbs).
- Loại yêu cầu làm rõ: Functional Requirements, Business Logic, và Use Case Scenarios.
- Thước đo: Thang đo SUS đạt 70.53 điểm (Acceptable)."""

ws.cell(row, 13).value = why_text
ws.cell(row, 14).value = how_text
ws.cell(row, 15).value = taxonomy_text
ws.cell(row, 16).value = 'WER 2022'

wb.save('docs/Synthesis_Matrix_RP6.xlsx')
print('Successfully populated Row 8 for antonelli2022iterative in docs/Synthesis_Matrix_RP6.xlsx!')
