import openpyxl

wb = openpyxl.load_workbook('docs/Synthesis_Matrix_RP6.xlsx')
ws = wb.active

row = 11

ws.cell(row, 1).value = '=A10+1'
ws.cell(row, 2).value = 'acm2022proposal'
ws.cell(row, 3).value = 'A Proposal for Enhancing Agile Requirements Engineering with Prototyping and Enriched User Stories'
ws.cell(row, 4).value = 'N. Keshk, M. El-Ramly, and A. Salah (2022)'
ws.cell(row, 5).value = "ACM FAMECSE '22 (Federated Africa and Middle East Conference on Software Engineering), pp. 59–63"
ws.cell(row, 6).value = 'Downloaded (12_acm2022proposal_Agile_Enriched_User_Stories.pdf)'
ws.cell(row, 7).value = 'https://doi.org/10.1145/3531056.3542773'

ws.cell(row, 8).value = (
    'Đề xuất mô hình lai (Hybrid ARE Process) kết hợp Prototyping độ trung thực cao (High-fidelity Mockups) '
    'và Câu chuyện người dùng mở rộng (Enriched User Stories) để tích hợp vào quy trình Agile Scrum, '
    'giải quyết bài toán thiếu hụt tài liệu và bất đồng cách hiểu.'
)

ws.cell(row, 9).value = (
    'User Stories truyền thống quá ngắn và mơ hồ, dẫn đến hiểu lầm và làm lại (rework) nghiêm trọng cuối Sprint. '
    'Việc cho PO và UI/UX Designer tạo prototype và viết Enriched User Story chạy trước đội lập trình ít nhất 1 Sprint '
    '(precede by at least one sprint) giúp giảm 30-40% rework mà không làm chậm nhịp độ Agile.'
)

ws.cell(row, 10).value = (
    'Làm rõ xuất sắc: Luồng giao diện (UI Flows), Ràng buộc phi chức năng trong tiêu chí chấp nhận (NFR Acceptance Criteria), '
    'và Từ điển dữ liệu (Data Dictionary). Ngăn ngừa việc bỏ quên NFRs vốn là điểm yếu cố hữu của User Stories thông thường.'
)

ws.cell(row, 11).value = (
    'Nghiên cứu đề xuất quy trình nâng cao gồm 8 bước tăng dần (từ Business Process Model, UI Mockup, Enriched User Story '
    'đến Backlog Grooming) dựa trên việc tổng hợp và giải quyết 17 thách thức của Agile RE từ các nghiên cứu thực nghiệm trước đó.'
)

ws.cell(row, 12).value = (
    'Mô hình đề xuất dựa trên khung khái niệm và bài học kinh nghiệm; nhóm tác giả đang triển khai thử nghiệm '
    'trên dự án quy mô lớn và khảo sát chuyên gia để thu thập thêm số liệu định lượng chi tiết.'
)

why_text = """Tại sao cần Prototype & Enriched User Story trong Agile? (Why?):
- Bối cảnh & Vấn đề: Agile chủ trương giảm thiểu tài liệu văn bản, chỉ dùng User Stories ngắn gọn. Tuy nhiên, lập trình viên không thể hình dung màn hình trông như thế nào và luồng dữ liệu ra sao; khách hàng chỉ nhận ra sai lệch khi sản phẩm được giao cuối Sprint, dẫn đến khối lượng làm lại (rework) khổng lồ.
- Giải pháp: Cần một cầu nối trực quan và cụ thể hóa yêu cầu mà không phá vỡ tính linh hoạt của Agile."""

how_text = """Quy trình lai 8 bước triển khai thế nào? (How?):
- Nguyên tắc sống còn: PO và UI/UX Designer chạy song song và PHẢI ĐI TRƯỚC ĐỘI DEV ÍT NHẤT 1 SPRINT (Sprint N-1).
- 8 bước: (1) Sơ đồ quy trình nghiệp vụ tổng thể; (2) Chọn tính năng ưu tiên; (3) Dựng High-fi Mockups bằng tool chuyên nghiệp (Adobe XD/Figma); (4) Validate với khách hàng; (5) Validate tính khả thi với Dev; (6) Viết Enriched User Story (kèm NFRs, Data Dictionary, Prototype); (7) Khách hàng duyệt lần 2; (8) Đưa vào Backlog sẵn sàng cho Sprint N."""

taxonomy_text = """Phân loại yêu cầu & Tác động (Taxonomy & RQ6.3):
- Khắc phục điểm mù NFR trong Agile: Biến các yêu cầu phi chức năng (bảo mật, kiểm tra tính hợp lệ dữ liệu, hiệu năng) thành các Tiêu chí chấp nhận nâng cao (Enhanced Acceptance Criteria) gắn chặt vào từng User Story.
- Trực quan hóa UI/UX: High-fidelity Mockup giúp lập trình viên biết chính xác bảng dữ liệu và thành phần giao diện cần tác động."""

ws.cell(row, 13).value = why_text
ws.cell(row, 14).value = how_text
ws.cell(row, 15).value = taxonomy_text
ws.cell(row, 16).value = 'https://doi.org/10.1145/3531056.3542773'

wb.save('docs/Synthesis_Matrix_RP6.xlsx')
print('Successfully populated Row 11 for acm2022proposal in docs/Synthesis_Matrix_RP6.xlsx!')
