# The 8 Ascending Steps of the Proposed Agile Requirements Engineering Process

Based on Section 5 of the paper, the proposed hybrid process consists of eight ascending steps designed to tackle agile requirements engineering challenges [1]:

### 1. Step 1: Gathering High-Level Requirements and Building a Business Process Model (BPM)
* **English**: High-level requirements are collected, recorded, and reviewed to ensure completeness, providing a comprehensive view of the project's size, modules, and features [1]. Business process modeling is represented as a flowchart showing the precise sequence of business activities and data flows [1]. This step is critical because it provides a reliable project roadmap for the Product Owner (PO) and a stable architecture blueprint for the solution architect, preventing future reworks caused by overlooked feature dependencies [1].
* **Vietnamese**: Các yêu cầu cấp cao được thu thập, ghi lại và xem xét để đảm bảo tính đầy đủ, cung cấp một cái nhìn toàn diện về quy mô, các phân hệ và tính năng của dự án [1]. Việc mô hình hóa quy trình nghiệp vụ được thể hiện dưới dạng lưu đồ chỉ ra trình tự chính xác của các hoạt động nghiệp vụ và luồng dữ liệu [1]. Bước này rất quan trọng vì nó cung cấp một lộ trình dự án đáng tin cậy cho Product Owner (PO) và bản thiết kế kiến trúc ổn định cho kiến trúc sư giải pháp, ngăn ngừa việc phải làm lại (rework) trong tương lai do bỏ sót các mối phụ thuộc giữa các tính năng [1].

### 2. Step 2: Selecting a Feature to Implement
* **English**: Based on client priority, the PO selects a feature that has no dependencies on other unfinished features to elicit detailed functional, non-functional, and design requirements [2] [3]. The UI/UX designer actively participates in these sessions to capture design requirements early, which minimizes subsequent UI rework [3].
* **Vietnamese**: Dựa trên mức độ ưu tiên của khách hàng, PO chọn một tính năng không có sự phụ thuộc vào các tính năng chưa hoàn thành khác để khai thác các yêu cầu chi tiết về chức năng, phi chức năng và thiết kế [2] [3]. Nhà thiết kế UI/UX tham gia tích cực vào các buổi họp này để nắm bắt các yêu cầu thiết kế ngay từ sớm, giúp giảm thiểu việc phải sửa đổi giao diện (UI rework) sau này [3].

### 3. Step 3: Building a Prototype
* **English**: Prototyping is used to efficiently gather and share requirements with the development team [4]. The paper proposes three specific practices: using high-fidelity mockups (which is faster and more flexible than code), utilizing professional prototyping tools to boost productivity, and generating an evolutionary prototype that can be reused in the final product rather than starting from scratch [4].
* **Vietnamese**: Việc tạo mẫu thử (prototyping) được sử dụng để thu thập và chia sẻ các yêu cầu với nhóm phát triển một cách hiệu quả [4]. Bài báo đề xuất ba thực hành cụ thể: sử dụng các bản mockup có độ trung thực cao (nhanh và linh hoạt hơn so với viết mã), sử dụng các công cụ thiết kế chuyên nghiệp để tăng năng suất, và tạo ra một mẫu thử tiến hóa có thể tái sử dụng trong sản phẩm cuối cùng thay vì phải bắt đầu lại từ đầu [4].

### 4. Step 4: Validating and Verifying Prototypes with Stakeholders
* **English**: This step involves validating the prototype with stakeholders to avoid missing requirements, expose conflicting requirements, and ensure that the PO, UI/UX designers, and stakeholders share a common understanding [5].
* **Vietnamese**: Bước này bao gồm việc xác thực mẫu thử với các bên liên quan để tránh bỏ sót yêu cầu, phát hiện các yêu cầu xung đột, và đảm bảo rằng PO, nhà thiết kế UI/UX cùng các bên liên quan có chung một cách hiểu [5].

### 5. Step 5: Validating Prototypes with the Technical Team
* **English**: The prototype is validated with the technical team to identify and avoid potential future technical issues, reduce rework, and confirm the technical feasibility of the design [6].
* **Vietnamese**: Mẫu thử được xác thực với nhóm kỹ thuật để nhận diện và tránh các vấn đề kỹ thuật tiềm ẩn trong tương lai, giảm thiểu việc làm lại, và xác nhận tính khả thi về mặt kỹ thuật của thiết kế [6].

### 6. Step 6: Writing an Enriched User Story
* **English**: After validation, the PO writes a detailed user story using an enhanced template [7]. This template includes the user story statement, actors, priority, preconditions, post-conditions, scenarios, output, a data dictionary, the prototype itself, and enhanced acceptance criteria (covering both business rules and constraints like non-functional and validation rules) [7]. This addresses documentation gaps and ensures non-functional requirements are not overlooked [7].
* **Vietnamese**: Sau khi xác thực, PO viết một câu chuyện người dùng (user story) chi tiết bằng cách sử dụng một biểu mẫu cải tiến [7]. Biểu mẫu này bao gồm phát biểu câu chuyện người dùng, các tác nhân, độ ưu tiên, tiền điều kiện, hậu điều kiện, các kịch bản, đầu ra, từ điển dữ liệu, chính mẫu thử đó, và các tiêu chí chấp nhận cải tiến (bao gồm cả quy tắc nghiệp vụ lẫn các ràng buộc như phi chức năng và xác thực) [7]. Điều này giải quyết việc thiếu hụt tài liệu và đảm bảo các yêu cầu phi chức năng không bị bỏ qua [7].

### 7. Step 7: User Story Review
* **English**: The client reviews the detailed user story alongside the prototype to provide final approval [8]. This serves as a second evaluation of the prototype, double-checking that all client requirements are met and none are missing [8].
* **Vietnamese**: Khách hàng xem xét chi tiết câu chuyện người dùng cùng với mẫu thử để đưa ra phê duyệt cuối cùng [8]. Bước này đóng vai trò như một lần đánh giá thứ hai đối với mẫu thử, kiểm tra kỹ lưỡng để đảm bảo tất cả các yêu cầu của khách hàng đều được đáp ứng và không có yêu cầu nào bị bỏ sót [8].

### 8. Step 8: Backlog Update
* **English**: The PO adds the finalized, approved user story to the product backlog, and the cycle (Steps 2 to 8) is repeated until all requirements are completed [9].
* **Vietnamese**: PO thêm câu chuyện người dùng đã hoàn thành và được phê duyệt vào danh sách yêu cầu sản phẩm (backlog), và chu trình (từ Bước 2 đến Bước 8) được lặp lại cho đến khi hoàn thành tất cả các yêu cầu [9].

---

## Backlog-Grooming Mechanism: Working Ahead of the Development Team

* **English**: To ensure smooth execution, the development team only starts a sprint when the backlog contains a sufficient number of fully completed and validated user stories [10]. To achieve this, the PO and the UI/UX designer work in parallel with the development team but must operate at least one sprint ahead of them [10]. This acts as an advanced backlog-grooming mechanism, ensuring that requirements are fully detailed, prototyped, and validated before the developers begin implementation [10].
* **Vietnamese**: Để đảm bảo việc thực hiện diễn ra suôn sẻ, nhóm phát triển chỉ bắt đầu một sprint khi backlog đã có đủ số lượng câu chuyện người dùng đã hoàn thành và được xác thực đầy đủ [10]. Để đạt được điều này, PO và nhà thiết kế UI/UX làm việc song song với nhóm phát triển nhưng phải đi trước họ ít nhất một sprint [10]. Điều này hoạt động như một cơ chế chuẩn bị backlog nâng cao, đảm bảo các yêu cầu được chi tiết hóa, tạo mẫu thử và xác thực đầy đủ trước khi các lập trình viên bắt đầu triển khai [10].

## References

[1] Keshk, El-Ramly, Salah. “A Proposal for Enhancing Agile Requirements Engineering with Prototyping and Enriched User Stories,” ACM FAMECSE, 2022.
