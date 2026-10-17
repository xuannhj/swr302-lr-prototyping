import openpyxl

wb = openpyxl.load_workbook('docs/Synthesis_Matrix_RP6.xlsx')
ws = wb.active

# ==============================================================================
# ROW 14: ferrari2016ambiguity
# ==============================================================================
row = 14
ws.cell(row, 1).value = '=A13+1'
ws.cell(row, 2).value = 'ferrari2016ambiguity'
ws.cell(row, 3).value = 'Ambiguity and tacit knowledge in requirements elicitation interviews'
ws.cell(row, 4).value = 'Alessio Ferrari, Paola Spoletini, and Stefania Gnesi (2016)'
ws.cell(row, 5).value = 'Requirements Engineering Journal (Springer), Vol. 21, Issue 3, pp. 333–355'
ws.cell(row, 6).value = 'Indexed & Cited (ref.bib)'
ws.cell(row, 7).value = 'https://doi.org/10.1007/s00766-016-0249-3'

ws.cell(row, 8).value = (
    'Nghiên cứu thực nghiệm trên 34 cuộc phỏng vấn khách hàng - phân tích viên (customer-analyst interviews). '
    'Xây dựng khung phân loại 4 hiện tượng mơ hồ nhận thức: Unclarity, Multiple Understanding, Incorrect Disambiguation, '
    'và Correct Disambiguation; chứng minh sự mơ hồ là dấu hiệu kích hoạt (cue/trigger) để khơi gợi Tri thức ẩn (Tacit Knowledge).'
)

ws.cell(row, 9).value = (
    'Trong đặc tả văn bản và phỏng vấn chay, hiện tượng "Giải mã sai lệch" (Incorrect Disambiguation) cực kỳ nguy hiểm vì '
    'phân tích viên tự cho rằng mình đã hiểu đúng và âm thầm đặt ra giả định sai, tạo nên "ảo giác đồng thuận" (illusion of shared understanding). '
    'Prototyping biến các giả định ngầm thành các giao diện trực quan cụ thể, vạch trần tức thì các hiểu lầm tiềm ẩn trước khi lập trình.'
)

ws.cell(row, 10).value = (
    'Làm rõ xuất sắc Tri thức ẩn (Tacit Knowledge) và Ngữ cảnh thực dụng (Pragmatic Context) của Yêu cầu Chức năng (FRs) '
    'và Quy tắc nghiệp vụ (Business Rules) vốn thường bị khách hàng bỏ qua vì coi là điều hiển nhiên.'
)

ws.cell(row, 11).value = (
    'Khảo sát chi tiết 34 phiên phỏng vấn RE thực tế. Phát hiện phần lớn các hiểu lầm xuất phát từ ngữ cảnh thực dụng (pragmatic context) '
    'và việc giải mã sai (incorrect disambiguation) hơn là lỗi ngữ pháp thuần túy.'
)

ws.cell(row, 12).value = (
    'Nghiên cứu tập trung vào phiên phỏng vấn đối thoại bằng lời; chưa tích hợp công cụ đo lường mức độ giảm mơ hồ khi '
    'có sự hiện diện đồng thời của mẫu thử tương tác (interactive prototypes).'
)

ws.cell(row, 13).value = """Vai trò của Mơ hồ và Tri thức ẩn trong RE (Why?):
- Bối cảnh & Vấn đề: Trong giao tiếp yêu cầu truyền thống, mơ hồ thường bị coi là lỗi (defect). Tuy nhiên, nghiên cứu này chứng minh sự mơ hồ thực chất là "mỏ vàng" để khai thác tri thức ẩn (tacit knowledge) - những quy tắc nghiệp vụ mà khách hàng nắm rõ nhưng không nói ra vì tưởng phân tích viên đã biết.
- Ảo giác đồng thuận: Khi hai bên dùng ngôn từ trừu tượng, họ tưởng mình hiểu nhau nhưng thực tế đang hình dung về hai hệ thống hoàn toàn khác biệt."""

ws.cell(row, 14).value = """Khung phân loại 4 chiều mơ hồ nhận thức (How?):
- Phương pháp: Phân tích định tính và định lượng trên 34 cuộc phỏng vấn thu thập yêu cầu.
- 4 hiện tượng nhận thức:
  1. Unclarity: Câu nói mập mờ, thiếu dữ kiện.
  2. Multiple Understanding: Câu nói gợi mở nhiều hướng diễn giải logic khác nhau.
  3. Incorrect Disambiguation: Phân tích viên tự ý suy đoán và hiểu sai ý khách hàng mà không hỏi lại (cội nguồn của lỗi phần mềm).
  4. Correct Disambiguation: Phân tích viên giải mã chính xác thông qua câu hỏi đào sâu."""

ws.cell(row, 15).value = """Cơ chế Prototype hóa giải Incorrect Disambiguation (Taxonomy & RQ6.3):
- Prototype như một bài kiểm tra thực tế (Reality Check):
  + Khi nhìn vào màn hình prototype, khách hàng lập tức nhận ra các điểm phân tích viên hiểu sai: "Khoan đã, tôi không hề muốn nút bấm này hoạt động như thế!".
  + Prototype biến tri thức ẩn (tacit) thành tri thức tường minh (explicit), triệt tiêu hoàn toàn rủi ro Incorrect Disambiguation."""

ws.cell(row, 16).value = 'https://doi.org/10.1007/s00766-016-0249-3'


# ==============================================================================
# ROW 15: spoletini2018interview
# ==============================================================================
row = 15
ws.cell(row, 1).value = '=A14+1'
ws.cell(row, 2).value = 'spoletini2018interview'
ws.cell(row, 3).value = 'Interview Review: An Empirical Study on Detecting Ambiguities in Requirements Elicitation Interviews'
ws.cell(row, 4).value = 'Paola Spoletini, Alessio Ferrari, and Stefania Gnesi (2018)'
ws.cell(row, 5).value = 'REFSQ 2018, LNCS vol. 10753, Springer, pp. 243–259'
ws.cell(row, 6).value = 'Indexed & Cited (ref.bib)'
ws.cell(row, 7).value = 'https://doi.org/10.1007/978-3-319-77243-1_15'

ws.cell(row, 8).value = (
    'Quy trình kiểm duyệt phỏng vấn có cấu trúc (Interview Review Protocol): Ghi âm và cho phân tích viên gốc cùng '
    'người kiểm duyệt độc lập (independent secondary reviewer) nghe lại để phát hiện các mơ hồ tiềm ẩn (latent ambiguities) '
    'mà phiên phỏng vấn trực tiếp đã bỏ sót.'
)

ws.cell(row, 9).value = (
    'Do phỏng vấn trực tiếp gây quá tải nhận thức, các bên bỏ sót phần lớn mơ hồ trong thời gian thực. '
    'Đặc biệt, mơ hồ mà phân tích viên gốc và người kiểm duyệt độc lập phát hiện có sự KHÁC BIỆT CÓ Ý NGHĨA THỐNG KÊ, '
    'chứng minh mỗi cá nhân luôn có điểm mù nhận thức riêng. Prototyping cung cấp một mỏ neo nhận thức độc lập để chuẩn hóa diễn giải.'
)

ws.cell(row, 10).value = (
    'Làm rõ các Mơ hồ Tiềm ẩn về Luồng quy trình (Process Flows), Ràng buộc hệ thống (Constraints) '
    'và Thuật ngữ chuyên ngành (Domain Terminology).'
)

ws.cell(row, 11).value = (
    'Thực nghiệm trên các nhóm sinh viên RE tại Kennesaw State University và UTS. '
    'Chứng minh kiểm duyệt hồi cứu phát hiện số lượng mơ hồ vượt trội so với phỏng vấn trực tiếp và '
    'hai người kiểm duyệt mang lại hai góc nhìn nhận thức hoàn toàn bổ trợ nhau.'
)

ws.cell(row, 12).value = (
    'Quy trình nghe lại băng ghi âm tốn nhiều thời gian và công sức; '
    'cần kết hợp các công cụ hỗ trợ trực quan hóa hoặc tạo mẫu để tăng tốc độ đồng thuận giữa các bên.'
)

ws.cell(row, 13).value = """Khắc phục điểm mù nhận thức trong phỏng vấn RE (Why?):
- Bối cảnh & Vấn đề: Phỏng vấn trực tiếp đòi hỏi người hỏi phải vừa lắng nghe, vừa suy nghĩ câu hỏi tiếp theo, vừa ghi chép. Tình trạng quá tải nhận thức này khiến phân tích viên bỏ sót vô số điểm mơ hồ quan trọng.
- Ý nghĩa: Nghiên cứu khẳng định tài liệu yêu cầu và biên bản phỏng vấn cần được kiểm duyệt hồi cứu bởi nhiều góc nhìn độc lập."""

ws.cell(row, 14).value = """Giao thức kiểm duyệt phỏng vấn hai lớp (How?):
- Thiết kế thực nghiệm: Các cuộc phỏng vấn RE được ghi âm đầy đủ. Sau đó được kiểm duyệt độc lập bởi:
  1. Primary Analyst (người trực tiếp phỏng vấn).
  2. Secondary Independent Reviewer (người ngoài cuộc nghe lại).
- Kết quả đối sánh: Hai bên phát hiện các tập hợp mơ hồ khác biệt rõ rệt, chứng minh tính bù trừ nhận thức và sự cần thiết của góc nhìn thứ ba."""

ws.cell(row, 15).value = """Sai lệch diễn giải và Mỏ neo Prototyping (Taxonomy & RQ6.3):
- Độ lệch diễn giải (Interpretation Discrepancy - Δ_interp):
  + Khi chỉ có văn bản và lời nói, mức độ bất đồng diễn giải giữa các bên rất cao.
  + Prototype đóng vai trò "mỏ neo nhận thức khách quan", chuẩn hóa thuật ngữ chuyên môn và các ràng buộc hệ thống, giúp triệt tiêu độ lệch diễn giải giữa các bên tham gia."""

ws.cell(row, 16).value = 'https://doi.org/10.1007/978-3-319-77243-1_15'


# ==============================================================================
# ROW 16: brill2010videos
# ==============================================================================
row = 16
ws.cell(row, 1).value = '=A15+1'
ws.cell(row, 2).value = 'brill2010videos'
ws.cell(row, 3).value = 'Videos vs. Use Cases: Can Videos Capture More Requirements Under Time Pressure?'
ws.cell(row, 4).value = 'Oliver Brill, Kurt Schneider, and Eric Knauss (2010)'
ws.cell(row, 5).value = 'REFSQ 2010, LNCS vol. 6182, Springer, pp. 30–44'
ws.cell(row, 6).value = 'Indexed & Cited (ref.bib)'
ws.cell(row, 7).value = 'https://doi.org/10.1007/978-3-642-14192-8_5'

ws.cell(row, 8).value = (
    'Nghiên cứu thực nghiệm đối đầu giữa Video-based Requirements (Tạo mẫu kịch bản video / Video Prototyping) '
    'và Ca sử dụng dạng văn bản truyền thống (Textual Use Cases) dưới áp lực thời gian (Time Pressure).'
)

ws.cell(row, 9).value = (
    'Dưới cùng áp lực thời gian gắt gao, nhóm sử dụng Video Prototyping ghi nhận và làm rõ được SỐ LƯỢNG YÊU CẦU NHIỀU HƠN '
    'ĐÁNG KỂ so với nhóm đọc Use Case dạng văn bản. Video đóng vai trò prototype động, trực quan hóa bối cảnh, '
    'giảm tải mệt mỏi nhận thức và loại bỏ các hiểu lầm từ ngữ.'
)

ws.cell(row, 10).value = (
    'Làm rõ vượt trội Bối cảnh tương tác người dùng (User Interaction Context), Luồng thao tác tác nghiệp (Operational Flows) '
    'và Trải nghiệm người dùng thực tế (Usability in Practice).'
)

ws.cell(row, 11).value = (
    'Thực nghiệm có đối chứng đánh giá năng suất và độ chính xác yêu cầu. Chứng minh ngay cả người không chuyên '
    'chỉ mất khoảng 30 phút để tạo ra một video mô phỏng yêu cầu hiệu quả, vượt trội hơn viết văn bản đặc tả phức tạp.'
)

ws.cell(row, 12).value = (
    'Video có thể thiếu các thông số định lượng chính xác (như dung lượng RAM, mili-giây xử lý); '
    'cần kết hợp với bảng đặc tả bổ sung đối với các ràng buộc kỹ thuật sâu.'
)

ws.cell(row, 13).value = """Video Prototyping ứng phó áp lực thời gian (Why?):
- Bối cảnh & Vấn đề: Trong các dự án phát triển nhanh, viết Use Cases chi tiết bằng văn bản tốn rất nhiều thời gian và khiến người đọc mệt mỏi, dễ bỏ sót yêu cầu quan trọng.
- Giải pháp: Video đóng vai trò một prototype động, truyền tải trọn vẹn bối cảnh sử dụng chỉ trong vài phút."""

ws.cell(row, 14).value = """Thiết kế thực nghiệm đối đầu có kiểm soát (How?):
- Thiết kế: So sánh hai nhóm đối tượng thực hiện cùng một bài toán RE dưới áp lực thời gian nghiêm ngặt: Nhóm A sử dụng Video Prototyping, Nhóm B sử dụng Textual Use Cases.
- Đo lường: Đếm tổng số yêu cầu thu thập được (gross requirements), độ chính xác và mức độ hiểu đúng của các bên liên quan."""

ws.cell(row, 15).value = """Ưu thế của Mẫu động so với Đặc tả tĩnh (Taxonomy & RQ6.3):
- Bắt trọn yêu cầu bị bỏ sót:
  + Văn bản Use Case dễ bỏ quên bối cảnh thực tế (môi trường sử dụng, thao tác cử chỉ).
  + Video prototype làm nổi bật tính khả dụng và luồng thao tác thực tế, kích thích người xem phát hiện các bước thiếu trong kịch bản."""

ws.cell(row, 16).value = 'https://doi.org/10.1007/978-3-642-14192-8_5'


# ==============================================================================
# ROW 17: hickey1998prototyping
# ==============================================================================
row = 17
ws.cell(row, 1).value = '=A16+1'
ws.cell(row, 2).value = 'hickey1998prototyping'
ws.cell(row, 3).value = 'Prototyping for Requirements Elicitation and Validation: A Participative Prototype Evaluation Methodology'
ws.cell(row, 4).value = 'Ann M. Hickey and Douglas L. Dean (1998)'
ws.cell(row, 5).value = 'Proceedings of the Americas Conference on Information Systems (AMCIS 1998), pp. 112–114'
ws.cell(row, 6).value = 'Indexed & Cited (ref.bib)'
ws.cell(row, 7).value = 'https://aisel.aisnet.org/amcis1998/41'

ws.cell(row, 8).value = (
    'Đề xuất Phương pháp luận Đánh giá Prototype có sự tham gia (Participative Prototype Evaluation Methodology) '
    'kết hợp Hệ thống Hỗ trợ Nhóm (Group Support Systems - GSS / GroupSystems) để thu thập phản hồi có cấu trúc '
    'từ các nhóm người dùng lớn và đa dạng (large, heterogeneous groups).'
)

ws.cell(row, 9).value = (
    'Giải quyết khiếm khuyết kinh điển của Prototyping: đưa bản mẫu cho người dùng một cách tùy tiện không có kịch bản '
    'dẫn đến việc bị cuốn vào chi tiết bề mặt nông cạn (superficial UI aesthetics) hoặc bị chi phối bởi các thành viên "to mồm" (loud voices). '
    'Quy trình có cấu trúc giúp giữ vững trọng tâm vào Yêu cầu Chức năng cốt lõi và phát hiện toàn diện các yêu cầu bị thiếu.'
)

ws.cell(row, 10).value = (
    'Cân bằng và làm rõ hoàn hảo giữa Yêu cầu Chức năng nghiệp vụ (Core Functional Requirements) '
    'và Trải nghiệm tương tác (Interaction Experience), ngăn ngừa rủi ro tranh cãi cảm tính.'
)

ws.cell(row, 11).value = (
    'Nghiên cứu nền tảng thiết lập cấu trúc quy trình đánh giá mẫu thử theo pha; ứng dụng công nghệ GSS '
    'cho phép người dùng nhập phản hồi ẩn danh và song song, loại bỏ hiện tượng thiên lệch nhóm (groupthink).'
)

ws.cell(row, 12).value = (
    'Công nghệ GSS thời kỳ 1998 còn sơ khai trên máy tính để bàn mạng nội bộ; '
    'ngày nay đã được chuyển hóa thành các công cụ cộng tác trực tuyến hiện đại (như Miro, Figma, FigJam).'
)

ws.cell(row, 13).value = """Nền móng phương pháp luận đánh giá Prototype (Why?):
- Bối cảnh & Vấn đề: Các kỹ sư thường than phiền: "Đưa prototype cho khách hàng xem thì họ chỉ toàn cãi nhau về màu sắc nút bấm mà không chịu kiểm tra logic nghiệp vụ!".
- Ý nghĩa: Hickey & Dean là những người đầu tiên đặt nền móng giải quyết vấn đề này bằng một quy trình đánh giá mẫu thử có cấu trúc khoa học."""

ws.cell(row, 14).value = """Phương pháp đánh giá có sự tham gia kết hợp GSS (How?):
- Thiết kế quy trình:
  + Phân đoạn các phiên đánh giá theo từng nhiệm vụ cụ thể (task-based evaluation).
  + Áp dụng hệ thống Group Support Systems (GSS) cho phép toàn bộ stakeholder nhập phản hồi đồng thời và ẩn danh.
  + Triệt tiêu hiện tượng người có chức vụ cao hoặc to mồm át vía ý kiến của người khác."""

ws.cell(row, 15).value = """Định hướng vào Chức năng và Phát hiện Thiếu sót (Taxonomy & RQ6.3):
- Chống sa đà bề mặt: Quy trình dẫn dắt người dùng tập trung vào: "Hệ thống có đáp ứng đúng quy trình nghiệp vụ không?" trước khi bàn về giao diện.
- Phát hiện Missing Requirements: Nhờ việc tương tác song song, các nhóm người dùng từ các phòng ban khác nhau nhanh chóng chỉ ra các luồng nghiệp vụ liên phòng ban bị bỏ sót."""

ws.cell(row, 16).value = 'https://aisel.aisnet.org/amcis1998/41'

wb.save('docs/Synthesis_Matrix_RP6.xlsx')
print('Successfully populated Rows 14, 15, 16, 17 in docs/Synthesis_Matrix_RP6.xlsx!')
