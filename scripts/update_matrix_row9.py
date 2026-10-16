import openpyxl

wb = openpyxl.load_workbook('docs/Synthesis_Matrix_RP6.xlsx')
ws = wb.active

row = 9

ws.cell(row, 1).value = '=A8+1'
ws.cell(row, 2).value = 'bano2023videos'
ws.cell(row, 3).value = 'Can Videos be Used to Communicate Non-functional Requirements? An Early Empirical Investigation'
ws.cell(row, 4).value = 'S. Kopczyńska and J. Shi (2023)'
ws.cell(row, 5).value = 'IEEE 31st International Requirements Engineering Conference (RE@Next 2023), pp. 112–117'
ws.cell(row, 6).value = 'Published (IEEE Xplore Paywalled / DOI: 10.1109/REW57880.2023.00028)'
ws.cell(row, 7).value = 'https://doi.org/10.1109/REW57880.2023.00028'

ws.cell(row, 8).value = (
    'Khảo sát việc sử dụng video tầm nhìn (Vision Videos / Video Prototyping) như một phương thức tạo mẫu '
    'đa phương tiện (multimedia prototype) để truyền đạt và khơi gợi các thuộc tính chất lượng phần mềm trước khi phát triển.'
)

ws.cell(row, 9).value = (
    'Khắc phục hạn chế của đặc tả văn bản trừu tượng và bản vẽ giấy tĩnh (vốn không thể mô phỏng thời gian và môi trường thực tế); '
    'video kết hợp hình ảnh, phản ứng người dùng và thuyết minh giúp các bên liên quan dễ dàng nhận diện và thống nhất các yêu cầu phi chức năng (NFRs).'
)

ws.cell(row, 10).value = (
    'Làm rõ xuất sắc nhóm Yêu cầu Phi chức năng (NFRs), nổi bật nhất là 3 nhóm: '
    'Thời gian đáp ứng / Hiệu năng (Time behavior / Performance), Tính tương tác liên thông (Interoperability), '
    'và Tính khả dụng trong bối cảnh thực (Usability in context).'
)

ws.cell(row, 11).value = (
    'Nghiên cứu thực nghiệm trên 5 video tầm nhìn sản phẩm. Xác định 3 cơ chế truyền tải NFRs chính: '
    'phản ứng người dùng (user reactions), thuyết minh (voiceover/narrator), và phụ đề thông số (text captions). '
    'Chứng minh video là phương tiện bổ trợ khả thi và hiệu quả để lôi NFRs ra khỏi điểm mù.'
)

ws.cell(row, 12).value = (
    'Nghiên cứu thực nghiệm giai đoạn đầu (early empirical investigation) với cỡ mẫu 5 video; '
    'video có nguy cơ mang tính quảng bá (marketing bias) và khó đo lường định lượng chi tiết hơn văn bản kỹ thuật.'
)

why_text = """Tại sao lại cần Video Prototyping cho NFRs? (Why?):
- Bối cảnh & Vấn đề: Bản vẽ giấy (Paper Mockups) và đặc tả văn bản chữ hoàn toàn "bó tay" khi mô tả NFRs (như tốc độ tải, độ trễ mạng, thao tác khi đang di chuyển ngoài đường). Khách hàng nhìn giấy chỉ thấy nút bấm mà quên sạch yêu cầu chất lượng (hiệu ứng Visual Bias).
- Cơ chế: Video Prototyping cung cấp bối cảnh đa giác quan (hình ảnh động + âm thanh hiện trường + phụ đề thông số). Khách hàng nhìn thấy biểu cảm của người dùng khi gặp trễ mạng, từ đó kích hoạt nhận thức về các yêu cầu phi chức năng."""

how_text = """Người ta áp dụng sao? (How?):
- Thiết kế thực nghiệm: Phân tích thực nghiệm trên 5 video tầm nhìn sản phẩm (Vision Videos) trong kỹ nghệ phần mềm để khám phá cách thức các thuộc tính chất lượng được biểu đạt.
- Phương pháp biểu đạt: Kết hợp 3 kỹ thuật: (1) Biểu cảm và hành vi của người dùng thực tế; (2) Giọng đọc thuyết minh (Voiceover); (3) Phụ đề và chỉ số đo lường hiển thị trực tiếp trên video."""

taxonomy_text = """Người ta chia thành mấy loại? (Taxonomy & RQ6.3):
- Phân loại NFRs truyền tải tốt nhất:
  + Hiệu năng & Thời gian đáp ứng (Time behavior / Performance).
  + Khả năng tương thích & Đồng bộ thiết bị (Interoperability).
  + Tính khả dụng trong bối cảnh vận hành thực tế (Usability in context).
- Loại phương tiện: Rich Multimedia / Video Prototyping (bổ khuyết vào khoảng trống mà Paper và Source Code Prototyping để lại)."""

ws.cell(row, 13).value = why_text
ws.cell(row, 14).value = how_text
ws.cell(row, 15).value = taxonomy_text
ws.cell(row, 16).value = 'https://doi.org/10.1109/REW57880.2023.00028'

wb.save('docs/Synthesis_Matrix_RP6.xlsx')
print('Successfully populated Row 9 for bano2023videos in docs/Synthesis_Matrix_RP6.xlsx!')
