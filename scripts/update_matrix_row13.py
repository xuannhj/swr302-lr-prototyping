import openpyxl

wb = openpyxl.load_workbook('docs/Synthesis_Matrix_RP6.xlsx')
ws = wb.active

row = 13

ws.cell(row, 1).value = '=A12+1'
ws.cell(row, 2).value = 'diaz2021gender'
ws.cell(row, 3).value = 'Are requirements elicitation sessions influenced by participants\' gender? An empirical experiment'
ws.cell(row, 4).value = 'E. Díaz, J. I. Panach, S. Rueda, M. Ruiz, and O. Pastor (2021)'
ws.cell(row, 5).value = 'Science of Computer Programming (Elsevier), Vol. 204, 102595'
ws.cell(row, 6).value = 'Downloaded (13_diaz2021gender_Elicitation_Gender_Influence.pdf)'
ws.cell(row, 7).value = 'https://doi.org/10.1016/j.scico.2020.102595'

ws.cell(row, 8).value = (
    'Nghiên cứu thực nghiệm kiểm tra mức độ ảnh hưởng của biến nhiễu giới tính (gender bias / participant gender) '
    'đối với nỗ lực thời gian và độ chính xác của yêu cầu trong các phiên khơi gợi và mô hình hóa (BPMN vs GUI Prototypes).'
)

ws.cell(row, 9).value = (
    'Trong khi mô hình hóa trừu tượng (BPMN) cho thấy sự chênh lệch có ý nghĩa thống kê về thời gian (nữ dành nhiều nỗ lực hơn nam, '
    'p = 0.018, d = 0.37) và độ chính xác theo giới tính khách hàng (p = 0.048), thì việc tạo mẫu giao diện (GUIs Prototype) '
    'HOÀN TOÀN KHÔNG có sự khác biệt có ý nghĩa thống kê giữa các giới tính (p = 0.132). '
    'Chứng minh Prototype là vật trung gian bình đẳng (equalizing boundary object).'
)

ws.cell(row, 10).value = (
    'Làm rõ xuất sắc nhóm Yêu cầu Giao diện (GUIs / Interface Requirements) và Yêu cầu Chức năng nghiệp vụ. '
    'Bản mẫu trực quan giúp loại bỏ rào cản diễn đạt và thiên vị giới tính vốn tồn tại trong các mô hình trừu tượng hoặc phỏng vấn lời nói.'
)

ws.cell(row, 11).value = (
    'Thực nghiệm có đối chứng trên 59 sinh viên kỹ nghệ phần mềm đóng vai kỹ sư yêu cầu qua 2 khóa học (2018/2019 và 2019/2020). '
    'Áp dụng mô hình hỗn hợp (Mixed Model test) kiểm định các giả thuyết về nỗ lực, độ chính xác BPMN và độ chính xác GUI.'
)

ws.cell(row, 12).value = (
    'Thực nghiệm sử dụng video stakeholder mô phỏng thay vì phỏng vấn trực tiếp mặt đối mặt; '
    'đối tượng là sinh viên đại học (cần mở rộng sang kỹ sư công nghiệp giàu kinh nghiệm); '
    'nghiên cứu tập trung vào 2 bài toán nghiệp vụ cụ thể.'
)

why_text = """Tại sao cần kiểm soát biến nhiễu Giới tính trong Prototyping? (Why?):
- Bối cảnh & Vấn đề: Trong nghiên cứu thực nghiệm RE, câu hỏi phản biện cốt lõi là: "Liệu sự vượt trội của Prototype có bị chi phối bởi biến nhiễu về giới tính của người tham gia không?". Các nghiên cứu tâm lý xã hội chỉ ra phong cách giao tiếp giữa nam và nữ có sự khác biệt lớn khi phỏng vấn bằng lời nói hoặc văn bản.
- Vai trò của Prototype: Khẳng định tính vững chắc của phương pháp Prototyping khi chứng minh bản mẫu trực quan xóa nhòa mọi khoảng cách nhận thức cá nhân."""

how_text = """Quy trình thực nghiệm và Phép kiểm thống kê (How?):
- Thiết kế thực nghiệm: 59 người tham gia đóng vai kỹ sư yêu cầu xem video phỏng vấn khách hàng (nam và nữ) để thu thập yêu cầu cho 2 bài toán phần mềm, sau đó xây dựng mô hình BPMN và thiết kế GUIs.
- Phép kiểm thống kê: Sử dụng Mixed Model test để phân tích tác động chính của giới tính kỹ sư yêu cầu, giới tính khách hàng và các tương tác đa yếu tố."""

taxonomy_text = """Phân loại yêu cầu & Tác động của Prototype (Taxonomy & RQ6.3):
- So sánh BPMN vs GUIs Prototype:
  + BPMN (Mô hình quy trình trừu tượng): Bị ảnh hưởng bởi giới tính về thời gian (p = 0.018) và độ chính xác (p = 0.048).
  + GUIs Prototype (Mẫu thử trực quan): Đạt sự bình đẳng nhận thức tuyệt đối, độ chính xác không phụ thuộc vào giới tính (p = 0.132).
- Kết luận: Prototype là công cụ trung hòa nhận thức, đảm bảo mọi thành viên trong nhóm phát triển đều nắm bắt yêu cầu chính xác như nhau."""

ws.cell(row, 13).value = why_text
ws.cell(row, 14).value = how_text
ws.cell(row, 15).value = taxonomy_text
ws.cell(row, 16).value = 'https://doi.org/10.1016/j.scico.2020.102595'

wb.save('docs/Synthesis_Matrix_RP6.xlsx')
print('Successfully populated Row 13 for diaz2021gender in docs/Synthesis_Matrix_RP6.xlsx!')
