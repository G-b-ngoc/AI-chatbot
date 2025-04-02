from transformers import pipeline

# Tải mô hình chatbot đã được huấn luyện sẵn
print("Đang tải Ngọc Bot, vui lòng chờ...")
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

# Giới thiệu Ngọc Bot
print("Xin chào! Tôi là Ngọc Bot, được tạo ra để trò chuyện với bạn. Bạn khỏe không?")

# Vòng lặp để trò chuyện
while True:
    user_input = input("Bạn: ")  # Nhập câu hỏi hoặc lời nói của bạn
    if user_input.lower() in ["thoát", "exit", "bye"]:  # Thoát khỏi chương trình
        print("Ngọc Bot: Tạm biệt nhé! Hẹn gặp lại!")
        break
    response = chatbot(user_input)  # AI trả lời
    print("Ngọc Bot:", response[0]["generated_text"])  # In câu trả lời