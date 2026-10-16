import openpyxl

wb = openpyxl.load_workbook('docs/Synthesis_Matrix_RP6.xlsx')
ws = wb.active

row = 10

ws.cell(row, 1).value = '=A9+1'
ws.cell(row, 2).value = 'gupta2022strategic'
ws.cell(row, 3).value = 'Strategic prototyping technology adoption in startups: framework, challenges, and opportunities'
ws.cell(row, 4).value = 'V. Gupta, E. Bjarnason, and C. Gupta (2022)'
ws.cell(row, 5).value = 'IT Professional (IEEE Computer Society), Vol. 24, No. 5, pp. 36–43'
ws.cell(row, 6).value = 'Published (IEEE Xplore Paywalled / DOI: 10.1109/MITP.2022.3188562)'
ws.cell(row, 7).value = 'https://doi.org/10.1109/MITP.2022.3188562'

ws.cell(row, 8).value = (
    'Mở rộng mô hình PAM (Prototyping Anchor Model) vào bối cảnh các công ty khởi nghiệp công nghệ (startups). '
    'Xây dựng khung định hướng việc lựa chọn và tiếp nhận công nghệ tạo mẫu (prototyping technologies) mang tính chiến lược, '
    'giúp startup đối phó với sự biến động yêu cầu liên tục (requirements volatility) và nguy cơ pivot.'
)

ws.cell(row, 9).value = (
    'Startups vận hành dưới áp lực thị trường mơ hồ và nguồn lực hạn hẹp; prototyping đóng vai trò hạt nhân để kiểm chứng nhanh '
    'các giả định nghiệp vụ (business assumptions) và hạn chế làm lại (rework). Tuy nhiên, nếu thiếu chiến lược chọn công cụ, '
    'startup dễ rơi vào bẫy đóng băng ý tưởng quá sớm (premature idea cementing) hoặc gánh nặng nợ kỹ thuật mẫu (prototype debt).'
)

ws.cell(row, 10).value = (
    'Làm rõ xuất sắc: Tính khả thi của mô hình kinh doanh (Business Model Viability), Luồng thao tác của khách hàng (Customer Flows/Tasks) '
    'và Bằng chứng khả thi kỹ thuật (PoC). Thường bị bỏ qua nghiêm trọng: Toàn bộ nhóm Yêu cầu Phi chức năng (NFRs như Scalability, Bảo mật, Kiến trúc dài hạn) '
    'do áp lực tốc độ ra mắt sản phẩm (speed-to-market).'
)

ws.cell(row, 11).value = (
    'Nghiên cứu khung khái niệm (conceptual framework) kết hợp đối sánh dữ liệu thực tiễn từ các trường hợp startup áp dụng mô hình PAM. '
    'Phân tích 4 trụ cột tiếp nhận công nghệ: chi phí đầu tư, tốc độ học hỏi (learning curve), dải độ trung thực (fidelity range) '
    'và khả năng tích hợp công nghệ.'
)

ws.cell(row, 12).value = (
    'Khung nghiên cứu mang tính định tính và định hướng chiến lược; cần mở rộng kiểm chứng thực nghiệm định lượng về tỷ lệ thành công/sống sót '
    'và ROI của các startup công nghệ áp dụng khung này.'
)

why_text = """Tại sao Startup cần Prototyping chiến lược? (Why?):
- Bối cảnh & Vấn đề: Startups đối mặt với sự bất định tột độ về thị trường và rủi ro thất bại cao. Yêu cầu phần mềm không cố định mà thay đổi liên tục theo từng lần "chuyển hướng" (pivoting). Nguồn lực tài chính và thời gian cực kỳ hạn hẹp, không thể viết tài liệu đặc tả dày cộp.
- Thách thức & Cơ chế: Nếu chọn công cụ tạo mẫu tùy tiện (chỉ theo trào lưu hoặc công cụ miễn phí nhưng kém linh hoạt), startup sẽ bị kẹt giữa hai rủi ro: vẽ giấy quá sơ sài thì không kiểm chứng được với nhà đầu tư, còn code bằng mã nguồn thật quá sớm thì bị "đóng băng ý tưởng" (Premature Idea Cementing) và gánh nợ kỹ thuật (Prototype Debt) khi phải đập đi xây lại."""

how_text = """Startups áp dụng Prototyping như thế nào? (How?):
- Tích hợp khung PAM: Định vị công nghệ tạo mẫu theo 5 chiều của PAM (Mục đích, Phạm vi, Phương tiện, Thói quen dùng, và Chiến lược thăm dò) gắn chặt với từng giai đoạn phát triển của startup (khám phá ý tưởng -> kiểm chứng thị trường -> mở rộng quy mô).
- Quy trình tiếp nhận 3 bước: (1) Nhận diện các yếu tố tác động (chi phí, đường cong học hỏi, tính cộng tác, dải độ trung thực); (2) Thu thập thông tin và đánh giá công cụ tạo mẫu đối chiếu giữa nhu cầu kiểm chứng ngắn hạn và khả năng mở rộng dài hạn; (3) Ra quyết định chiến lược chuẩn hóa bộ công cụ tạo mẫu thay vì tiếp cận chắp vá theo cảm tính."""

taxonomy_text = """Người ta chia thành mấy loại? (Taxonomy & RQ6.3):
- Phân loại yêu cầu được làm rõ tốt nhất:
  + Giả định kinh doanh & Giá trị cốt lõi (Core Business Assumptions & Value Proposition).
  + Luồng thao tác tối thiểu của khách hàng (Customer Minimum Viable Flows).
  + Tính khả thi kỹ thuật sơ bộ (Proof-of-Concept / Technical Feasibility).
- Điểm mù NFRs trong Startups: Do áp lực sống còn "speed-to-market", các startup hầu như bỏ qua NFRs (bảo mật, hiệu năng tải lớn, khả năng bảo trì). Khi mẫu prototype nhanh được chuyển hóa thẳng thành sản phẩm thương mại, toàn bộ NFRs bị thiếu hụt sẽ gây đổ vỡ hệ thống."""

ws.cell(row, 13).value = why_text
ws.cell(row, 14).value = how_text
ws.cell(row, 15).value = taxonomy_text
ws.cell(row, 16).value = 'https://doi.org/10.1109/MITP.2022.3188562'

wb.save('docs/Synthesis_Matrix_RP6.xlsx')
print('Successfully populated Row 10 for gupta2022strategic in docs/Synthesis_Matrix_RP6.xlsx!')
