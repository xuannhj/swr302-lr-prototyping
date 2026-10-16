import openpyxl

wb = openpyxl.load_workbook('docs/Synthesis_Matrix_RP6.xlsx')
ws = wb.active

# Row 6 is Paper 7: Ferrari, Spoletini & Debnath (2022) - rej2022evolve
row = 6

ws.cell(row, 1).value = '=A5+1'
ws.cell(row, 2).value = 'rej2022evolve'
ws.cell(row, 3).value = 'How do requirements evolve during elicitation? An empirical study combining interviews and app store analysis'
ws.cell(row, 4).value = 'A. Ferrari, P. Spoletini, and S. Debnath (2022)'
ws.cell(row, 5).value = 'Requirements Engineering (Springer), Vol. 27(4), pp. 489–519'
ws.cell(row, 6).value = 'Downloaded (07_rej2022evolve_Requirements_Evolution.pdf)'
ws.cell(row, 7).value = 'https://doi.org/10.1007/s00766-022-00383-7'

ws.cell(row, 8).value = (
    'Khảo sát sự tiến hóa yêu cầu (Requirements Evolution) và cơ chế "đồng kiến tạo" (co-creation). '
    'So sánh giữa phỏng vấn truyền thống và tương tác với mẫu tham chiếu trực quan (app store / reference prototypes) '
    'để hoàn thiện User Stories.'
)

ws.cell(row, 9).value = (
    'Bằng chứng thực nghiệm đối đầu: Phỏng vấn bằng lời chỉ giữ lại 30–38% ý tưởng gốc và bỏ sót nhiều yêu cầu. '
    'Khi tương tác trực tiếp với sản phẩm/mẫu trực quan, nhà phân tích phát hiện và bổ sung thêm 42% yêu cầu bị thiếu (missing requirements).'
)

ws.cell(row, 10).value = (
    'Phỏng vấn bằng lời thuần túy chỉ tập trung vào chức năng nghiệp vụ nội bộ. '
    'Tương tác với mẫu thực tế làm tăng vọt 45% sự chú ý tới tính khả dụng (Usability), '
    'đồng thời làm rõ các yêu cầu phi chức năng (NFRs) cốt lõi như Bảo mật (Security), Quyền riêng tư (Privacy), và Thanh toán (Payment).'
)

ws.cell(row, 11).value = (
    'Thực nghiệm kiểm soát 2 giai đoạn trên 30 nhà phân tích (analysts). Kiểm định thống kê 95% tin cậy '
    '(Shapiro-Wilk, One-sample t-test & Percentile method): Conservation rate chỉ đạt 30–38%, 21% chủ đề hoàn toàn mới xuất hiện; '
    'tương tác mẫu tham chiếu giúp bổ sung tới 42% yêu cầu bị thiếu, mức độ quan tâm Usability tăng 45%.'
)

ws.cell(row, 12).value = (
    'Giai đoạn 2 chỉ cho phép thêm mới (extension) mà chưa đo lường chỉnh sửa/xóa (edit/deletion); '
    'đối tượng thực nghiệm là sinh viên phần mềm đóng vai analyst với một khách hàng giả định; cần mở rộng bối cảnh ngoài ứng dụng di động.'
)

why_text = """Tại sao lại cần Prototype / Mẫu tham chiếu tương tác? (Why?):
- Bối cảnh & Vấn đề: Ảo tưởng về "thu thập yêu cầu" (Elicitation Fallacy) xem yêu cầu như có sẵn trong đầu khách hàng. Thực tế, phỏng vấn bằng lời thuần túy khiến hơn 60% yêu cầu bị biến dạng và bỏ sót nghiêm trọng các khía cạnh trải nghiệm thực tế.
- Cơ chế: Yêu cầu là quá trình "đồng kiến tạo" (co-creation). Tương tác với mẫu tham chiếu trực quan (reference prototypes / app store exploration) đóng vai trò như "chất xúc tác nhận thức" (cognitive catalyst), kích hoạt tri thức ẩn của cả khách hàng lẫn người phân tích để nhận diện các thiếu sót."""

how_text = """Người ta áp dụng sao? (How?):
- Thiết kế thực nghiệm: Nghiên cứu thực nghiệm 2 giai đoạn (Phase I: Phỏng vấn tương tác 2 vòng với khách hàng; Phase II: Khám phá và tương tác trực tiếp 5 ứng dụng tham chiếu trên App Store/Google Play) với 30 nhà phân tích trên bài toán Quản lý trại hè dã ngoại.
- Quy trình: Mỗi analyst phỏng vấn khách hàng để sinh 50-60 User Stories ban đầu, sau đó tải và trải nghiệm các app thực tế, đọc review người dùng để viết bổ sung 20 User Stories. Các tác giả tiến hành mã hóa và phân tích định lượng (t-test, percentile method, 95% CI) về độ bảo tồn và mức độ tiến hóa yêu cầu."""

taxonomy_text = """Người ta chia thành mấy loại? (Taxonomy & RQ6.3):
- Phân loại so sánh: Phỏng vấn bằng lời truyền thống (Interview-based) vs Khám phá mẫu tham chiếu tương tác (App Store-inspired Prototyping).
- Phân loại yêu cầu & Tỷ lệ thay đổi:
  + Functional Requirements: Chiếm đa số ở phỏng vấn ban đầu nhưng chỉ giữ lại 30-38% nguyên bản, bổ sung thêm 42% yêu cầu chức năng mới sau khi tương tác mẫu thử.
  + Usability Requirements: Tăng vọt thêm 45% sau khi tương tác với sản phẩm trực quan, chứng minh prototype là công cụ hiệu quả nhất để khai phá yêu cầu tính khả dụng.
  + Non-Functional Requirements (NFRs): Các nhóm NFRs ẩn như Security, Privacy (theo dõi vị trí trẻ em), và Payment chỉ xuất hiện và được hoàn thiện khi người phân tích quan sát sản phẩm thực tế.
- Hạn chế: Thử nghiệm trên bài toán mobile app với sinh viên kỹ thuật; chưa đo lường thao tác xóa yêu cầu sai lệch ở giai đoạn 2."""

ws.cell(row, 13).value = why_text
ws.cell(row, 14).value = how_text
ws.cell(row, 15).value = taxonomy_text
ws.cell(row, 16).value = 'https://doi.org/10.1007/s00766-022-00383-7'

wb.save('docs/Synthesis_Matrix_RP6.xlsx')
print('Successfully populated Row 6 for rej2022evolve in docs/Synthesis_Matrix_RP6.xlsx!')
