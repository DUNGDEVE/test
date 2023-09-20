import nltk
from nltk.chat.util import Chat, reflections

# Định nghĩa các quy tắc cho chatbot
bongda_rules = [
    (r'(.*)(bóng đá)(.*)',
     ['Bóng đá là môn thể thao vua, bạn muốn biết gì về bóng đá?']),
    (r'(.*)(Cristiano Ronaldo)(.*)',
     ['Cristiano Ronaldo là một cầu thủ bóng đá nổi tiếng, người đến từ Bồ Đào Nha.']),
    (r'(.*)(Messi)(.*)',
     ['Messi là một cầu thủ bóng đá xuất sắc, người đến từ Argentina.']),
    (r'(.*)(World Cup)(.*)',
     ['World Cup là giải đấu bóng đá lớn nhất trên thế giới, diễn ra mỗi 4 năm một lần.']),
    (r'(.*)(Premier League)(.*)',
     ['Premier League là giải đấu bóng đá nổi tiếng ở Anh.']),
    (r'(.*)(Champions League)(.*)',
     ['Champions League là giải đấu câu lạc bộ hàng đầu ở châu Âu.'])
    (r'(.*)(Manchester United)(.*)',
     ['Manchester United là  câu lạc bộ hàng đầu ở the gioi.'])
]

# Tạo chatbot sử dụng các quy tắc
bongda_chatbot = Chat(bongda_rules, reflections)

# Hàm chính để tương tác với chatbot
def chat_with_bongda_bot():
    print("Chào bạn! Tôi là chatbot về bóng đá. Hãy nhập câu hỏi hoặc chủ đề bạn muốn biết.")
    print("Để thoát, hãy gõ 'quit'.")
    
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Chúc bạn một ngày tốt lành!")
            break
        else:
            response = bongda_chatbot.respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    chat_with_bongda_bot()
