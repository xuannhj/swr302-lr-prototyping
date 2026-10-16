import openpyxl

wb = openpyxl.load_workbook('docs/Synthesis_Matrix_RP6.xlsx')
ws = wb.active

row = 12

ws.cell(row, 1).value = '=A11+1'
ws.cell(row, 2).value = 'cascon2025ambiguity'
ws.cell(row, 3).value = 'Multi-Label Ambiguity Detection in Software Requirements Using Language Models'
ws.cell(row, 4).value = 'P. Oghabi and N. Kahani (2025)'
ws.cell(row, 5).value = 'Proceedings of the 35th Annual International Conference on Computer Science and Software Engineering (CASCON), pp. 145–156'
ws.cell(row, 6).value = 'Downloaded (14_cascon2025ambiguity_Ambiguity_Taxonomy_LM.pdf)'
ws.cell(row, 7).value = 'https://doi.org/10.1145/cascon.2025.oghabi'

ws.cell(row, 8).value = (
    'Xây dựng và chuẩn hóa hệ thống phân loại 4 nhóm mơ hồ (Ambiguity Taxonomy: Structural, Scope, Anaphoric, và Vagueness) '
    'trong yêu cầu phần mềm viết bằng ngôn ngữ tự nhiên (NL SRS). Ứng dụng mô hình ngôn ngữ (RoBERTa, DistilBERT kết hợp Back-Translation) '
    'để phát hiện đa nhãn sự mơ hồ trên tập dữ liệu chuẩn PURE.'
)

ws.cell(row, 9).value = (
    'Yêu cầu phần mềm dạng văn bản tự nhiên có tỷ lệ chồng lấn đa mơ hồ (multi-label ambiguity) rất cao. Mô hình RoBERTa kết hợp '
    'Back-Translation đạt Macro F1-score 78.84% (tăng 12% ở Scope ambiguity và 7% ở Structural ambiguity). '
    'Cung cấp thước đo và phân loại chuẩn mực để định nghĩa và đánh giá "Unclear Requirements" trong các nghiên cứu RE.'
)

ws.cell(row, 10).value = (
    'Phân loại 4 chiều mơ hồ: (1) Mơ hồ cấu trúc ngữ pháp (Structural/Syntactic); (2) Mơ hồ phạm vi tác động (Scope); '
    '(3) Mơ hồ chỉ định đại từ (Anaphoric); (4) Mơ hồ do từ ngữ mơ hồ/ước chừng (Vagueness). '
    'Đây là cơ sở khoa học để chứng minh tại sao Prototype triệt tiêu được sự mơ hồ mà văn bản không làm được.'
)

ws.cell(row, 11).value = (
    'Thực nghiệm trên 1,266 yêu cầu thực tế từ tập dữ liệu công khai PURE (Public Requirements Dataset) từ nhiều miền ứng dụng. '
    'Đánh giá kiểm thử trên 255 yêu cầu gán nhãn thủ công (test set). Áp dụng độ đo thỏa thuận liên người đánh giá '
    '(Cohen\'s Kappa & Fleiss\' Kappa) và kỹ thuật tăng cường dữ liệu Back-Translation.'
)

ws.cell(row, 12).value = (
    'Nghiên cứu tập trung vào đặc tả văn bản tiếng Anh; độ chính xác ở nhóm mơ hồ chỉ định (Anaphoric) còn phụ thuộc ngữ cảnh dài; '
    'cần tích hợp vào các công cụ RE tương tác để hỗ trợ phát hiện tự động theo thời gian thực.'
)

why_text = """Tại sao cần Taxonomy chuẩn hóa về Ambiguity (Unclear Requirements)? (Why?):
- Bối cảnh & Vấn đề: Trong đề tài "Effect of Prototyping on Missing & Unclear Requirements", câu hỏi lớn nhất của hội đồng là: "Unclear (mơ hồ) là gì? Lấy thước đo nào để phân loại và đo lường?". Nếu không có taxonomy chuẩn mực, việc đánh giá tính "unclear" sẽ bị cảm tính và thiếu cơ sở khoa học.
- Ý nghĩa: Nghiên cứu của Oghabi & Kahani (2025) thiết lập một hệ thống phân loại 4 loại mơ hồ chuẩn mực quốc tế trên tập dữ liệu thực tế PURE, cung cấp cơ sở lý thuyết vững chắc cho bài SLR."""

how_text = """Phương pháp đo lường và phát hiện mơ hồ (How?):
- Dữ liệu thực nghiệm: 1,266 yêu cầu thực tế từ tập dữ liệu PURE, phân tách 255 mẫu kiểm thử được kiểm định chéo bởi chuyên gia bằng chỉ số Fleiss' Kappa.
- Mô hình phát hiện: Fine-tune các mô hình ngôn ngữ Transformer (RoBERTa, DistilBERT) cho bài toán phân loại đa nhãn (Multi-Label Classification) kết hợp Back-Translation để xử lý mất cân bằng dữ liệu, đạt Macro F1 = 78.84%."""

taxonomy_text = """Hệ thống 4 nhóm mơ hồ (Taxonomy & RQ6.3):
1. Structural Ambiguity (Mơ hồ cú pháp): Một câu có nhiều cây phân tích ngữ pháp (ví dụ: liên từ "và/hoặc" không rõ nhóm).
2. Scope Ambiguity (Mơ hồ phạm vi): Lượng từ (all, every, each) hoặc phủ định (not) không rõ bao quát đến đâu.
3. Anaphoric Ambiguity (Mơ hồ đại từ): Các đại từ (it, this, they) không rõ trỏ về danh từ nào đứng trước.
4. Vagueness (Tính mơ hồ/ước chừng): Dùng tính từ/phó từ không đo lường được (fast, user-friendly, appropriate).
-> Cơ chế Prototype giải quyết: Prototype trực quan hóa màn hình cụ thể, triệt tiêu đại từ (Anaphoric), gắn ràng buộc số liệu cụ thể triệt tiêu Vagueness, và phân nhánh IF-ELSE rõ ràng triệt tiêu Scope/Structural!"""

ws.cell(row, 13).value = why_text
ws.cell(row, 14).value = how_text
ws.cell(row, 15).value = taxonomy_text
ws.cell(row, 16).value = 'https://doi.org/10.1145/cascon.2025.oghabi'

wb.save('docs/Synthesis_Matrix_RP6.xlsx')
print('Successfully populated Row 12 for cascon2025ambiguity in docs/Synthesis_Matrix_RP6.xlsx!')
