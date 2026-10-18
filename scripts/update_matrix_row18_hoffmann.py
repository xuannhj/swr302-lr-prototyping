import openpyxl

wb = openpyxl.load_workbook('docs/Synthesis_Matrix_RP6.xlsx')
ws = wb.active

row = 18
ws.cell(row, 1).value = '=A17+1'
ws.cell(row, 2).value = 'hoffmann2011automotive'
ws.cell(row, 3).value = 'Towards automotive service engineering: a design framework and a process model for developing mobile services in automobiles'
ws.cell(row, 4).value = 'Holger Hoffmann and Jan Marco Leimeister (2011)'
ws.cell(row, 5).value = 'International Journal of Electronic Business (IJEB), Inderscience, Vol. 9, No. 4, pp. 320–349'
ws.cell(row, 6).value = 'Indexed (ref.bib)'
ws.cell(row, 7).value = 'https://doi.org/10.1504/IJEB.2011.043254'

ws.cell(row, 8).value = (
    'Đề xuất phương pháp In-situ Prototyping (Tạo mẫu tại hiện trường / trong bối cảnh thực) '
    'cho Hệ thống dịch vụ di động trên xe hơi (Automotive Services). '
    'Tích hợp nguyên mẫu phần mềm trực tiếp vào bảng điều khiển buồng lái xe Audi A6 '
    '(màn hình MMI, nút xoay trung tâm, phím bấm trên vô-lăng, hệ thống loa xe hơi) '
    'để tài xế vừa lái xe vừa trực tiếp trải nghiệm và tương tác với dịch vụ MACS MyNews.'
)

ws.cell(row, 9).value = (
    'Đặc tả văn bản (SRS) và phỏng vấn trong phòng họp khiến kỹ sư lầm tưởng menu duyệt tin tức văn bản 3 cấp là dễ dùng. '
    'Khi đưa vào buồng lái ô tô thực tế (In-situ), người dùng phát hiện ngay các Yêu cầu bị bỏ sót chí mạng (Missing Requirements): '
    '(1) Thiếu tính năng Chuyển văn bản thành giọng nói (Text-to-Speech / Audio Readout) vì tài xế không thể rời mắt khỏi đường lái '
    'để đọc chữ quá 1.5 giây mà không gặp nguy cơ tai nạn; '
    '(2) Thiếu luồng xử lý gián đoạn ưu tiên (Interruption Handling) khi có cảnh báo va chạm khẩn cấp hoặc cuộc gọi đến; '
    '(3) Cụ thể hóa yêu cầu mơ hồ: thao tác chọn kênh tin tức chỉ được tối đa 1-2 lần bấm từ vô-lăng.'
)

ws.cell(row, 10).value = (
    'Bẻ gãy điểm mù NFR Deficit trong Hệ thống đan xen vật lý - không gian mạng (Cyber-Physical Systems): '
    'Làm rõ xuất sắc các Yêu cầu Phi chức năng (NFRs) sống còn gồm: '
    'An toàn & Quản lý xao nhãng tài xế (Safety & Driver Attention Management), '
    'Hiệu năng & Độ trễ viễn thông (Telematics Performance & Latency), '
    'và Công thái học âm thanh (Acoustic Noise Constraints).'
)

ws.cell(row, 11).value = (
    'Thử nghiệm ứng dụng tin tức tương tác MACS MyNews trong khuôn khổ dự án MACS phối hợp với tập đoàn Audi AG. '
    'Đánh giá thực nghiệm trong buồng lái xe Audi A6, tuân thủ nghiêm ngặt Quy tắc an toàn 15 giây (15-second rule) '
    'của ngành giao thông vận tải và thiết lập cơ chế Tải trước & Lưu đệm ngoại tuyến (Prefetching & Offline Caching).'
)

ws.cell(row, 12).value = (
    'Chi phí chế tạo và lắp đặt buồng lái thử nghiệm (testbed) trên xe Audi A6 thực tế rất đắt đỏ; '
    'thử nghiệm in-situ đòi hỏi điều kiện an toàn nghiêm ngặt trên đường thử khép kín trước khi thử nghiệm ngoài đời thực.'
)

ws.cell(row, 13).value = """Bối cảnh công nghiệp & Đột phá In-situ Prototyping (Why?):
- Bối cảnh: Ngành ô tô chuyển dịch từ cơ khí phần cứng sang dịch vụ số di động (In-car Mobile Services).
- Hạn chế của RE truyền thống: Ngồi phòng máy lạnh viết SRS hoặc bấm chuột trên desktop không thể phản ánh được áp lực nhận thức của tài xế khi xe đang chạy ở tốc độ cao."""

ws.cell(row, 14).value = """Giao thức In-situ Prototyping trong xe Audi A6 (How?):
- Tích hợp nguyên mẫu phần mềm MACS MyNews vào hệ thống điều khiển MMI và nút bấm vô-lăng của xe Audi A6.
- Đánh giá khả năng tương tác của tài xế trong điều kiện vận hành thực tế (in-situ evaluation)."""

ws.cell(row, 15).value = """Bằng chứng đối trọng hóa giải NFR Deficit (What?):
- Đập tan luận điểm cho rằng "Prototyping chỉ thấy UI mà bỏ quên NFRs": Prototype trong phòng lab thì bỏ quên NFR, nhưng In-situ Prototyping lại là công cụ số 1 để khai quật NFRs sống còn (An toàn, Xao nhãng, Độ trễ viễn thông, và Âm thanh).
- Đóng góp vào Section III-C và Section V (Gap 3) của bài báo SLR."""

wb.save('docs/Synthesis_Matrix_RP6.xlsx')
print('Row 18 (hoffmann2011automotive) updated successfully in docs/Synthesis_Matrix_RP6.xlsx')
