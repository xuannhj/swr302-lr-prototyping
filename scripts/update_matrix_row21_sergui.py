import openpyxl

wb = openpyxl.load_workbook('docs/Synthesis_Matrix_RP6.xlsx')
ws = wb.active

row = 21
ws.cell(row, 1).value = '=A20+1'
ws.cell(row, 2).value = 'kolthoff2024selfelicitation'
ws.cell(row, 3).value = 'Self-Elicitation of Requirements with Automated GUI Prototyping'
ws.cell(row, 4).value = 'Kristian Kolthoff, Christian Bartelt, Simone Paolo Ponzetto, and Kurt Schneider (2024)'
ws.cell(row, 5).value = 'Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE)'
ws.cell(row, 6).value = 'PDF Downloaded (papers_pdf/)'
ws.cell(row, 7).value = 'https://doi.org/10.1145/3691620.3695350'

ws.cell(row, 8).value = (
    'Đề xuất hệ thống SERGUI cho phép khách hàng Tự khơi gợi yêu cầu (Self-Elicitation of Requirements - SER) '
    'thông qua trợ lý AI đối thoại và kho dữ liệu 48.402 màn hình di động (Rico). '
    'Quy trình gồm 4 pha: Lọc và xếp hạng màn hình Top-k bằng Sentence-BERT/S2W, khám phá tính năng con, '
    'LLM (GPT-4) chủ động dự đoán và gợi ý Top-30 tính năng liên quan, và tự động tái xếp hạng màn hình theo phản hồi.'
)

ws.cell(row, 9).value = (
    'Giải quyết căn bệnh khách hàng không biết diễn đạt yêu cầu trong phỏng vấn văn bản truyền thống. '
    'Prototype trực quan đóng vai trò "Chất xúc tác kích hoạt trí nhớ" (Cognitive Stimulator). '
    'Đánh giá qua 72 phiên tạo mẫu: AI gợi ý tính năng bị bỏ quên đạt MAP = 0.741 (xấp xỉ 3 trong 4 tính năng '
    'được xác nhận là yêu cầu bị bỏ sót), MRR = 0.816 (tính năng đúng ở hạng 1.22). '
    'Tái xếp hạng giúp cải thiện +61.89 bậc trong 68.05% trường hợp.'
)

ws.cell(row, 10).value = (
    'Làm rõ và khơi gợi xuất sắc các Yêu cầu Chức năng (Functional Requirements) và Tính năng trải nghiệm (UX Features). '
    'Biến tri thức ẩn (Tacit Knowledge) và nhu cầu tiềm ẩn thành các yêu cầu hiển ngôn (explicit). '
    'Hạn chế: Chưa bao quát các yêu cầu phi chức năng sâu (NFRs như bảo mật, chịu tải máy chủ).'
)

ws.cell(row, 11).value = (
    'Thực nghiệm trên 72 phiên tạo mẫu với 12 chuyên gia kỹ thuật trên 3 miền ứng dụng (Shopping, News, Social). '
    'Feature Recommendation: MAP = 0.741, MRR = 0.816, P@1 = 0.691, P@10 = 0.638. '
    'GUI Feature Ranking: MRR = 0.390, HITS@1 = 0.270, HITS@15 = 0.691. '
    'GUI Reranking: Tăng trung bình +61.89 ranks (SD: 79.82).'
)

ws.cell(row, 12).value = (
    'Tập dữ liệu dựa trên ứng dụng di động Android; đánh giá sơ bộ trên 12 người tham gia; '
    'hệ thống tập trung vào các chức năng tương tác trực quan, cần kết hợp kỹ sư cho các NFRs backend.'
)

ws.cell(row, 13).value = """Nỗi khổ khách hàng không biết mình muốn gì (Why?):
- Thách thức: Khách hàng không có nền tảng IT nên chỉ nói được 1-2 câu sơ sài, bỏ quên hàng loạt yêu cầu nghiệp vụ ngầm.
- Phỏng vấn truyền thống tốn kém nhiều buổi họp lặp lại giữa analyst và khách hàng."""

ws.cell(row, 14).value = """Cơ chế SERGUI kích hoạt Self-Elicitation (How?):
- Khách hàng gõ câu yêu cầu sơ khởi -> SERGUI lôi màn hình mẫu từ kho 48.000 GUI ra cho xem.
- GPT-4 chủ động gợi ý Top-30 tính năng liên quan kèm hình ảnh minh họa -> Khách hàng tự nhận ra và bấm chọn bổ sung."""

ws.cell(row, 15).value = """Đột phá học thuật ACM/IEEE ASE 2024 của GS. Kurt Schneider (What?):
- Chứng minh Prototype trực quan đóng vai trò chất xúc tác nhận thức giúp khách hàng tự khơi gợi yêu cầu bị thiếu (Missing/Tacit).
- Đóng góp vào Section I (Introduction) và Section III-A (Elicitation Mechanisms) của bài báo SLR."""

wb.save('docs/Synthesis_Matrix_RP6.xlsx')
print('Row 21 (kolthoff2024selfelicitation) updated successfully in docs/Synthesis_Matrix_RP6.xlsx')
