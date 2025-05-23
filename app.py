import yaml
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random, string

app = Flask(__name__)

# Khởi tạo chatbot
chatbot = ChatBot('MyBot')
trainer = ListTrainer(chatbot)

# Nạp dữ liệu hội thoại từ file YAML
with open("customer_care.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

for conv in data["conversations"]:
    trainer.train(conv)

# Dữ liệu sản phẩm
products = [
    {"name": "Áo thun cotton", "price": "150,000 VNĐ", "image": "/static/images/aothun.jpg"},
    {"name": "Quần jean nam", "price": "350,000 VNĐ", "image": "/static/images/jean.jpg"},
    {"name": "Giày thể thao", "price": "500,000 VNĐ", "image": "/static/images/giay.jpg"}
]

def generate_discount_code(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg').lower()

    if "mã giảm giá" in userText:
        code = generate_discount_code()
        return f"Mã giảm giá của bạn là: <strong>{code}</strong>"

    elif "menu" in userText:
        html_products = ""
        for p in products:
            html_products += f'''
            <div style="margin-bottom: 15px;">
                <img src="{p['image']}" alt="{p['name']}" style="width:120px; height:auto; vertical-align:middle; margin-right:10px;">
                <strong>{p['name']}</strong><br>
                Giá: {p['price']}
            </div>
            '''
        return html_products

    elif "chăm sóc khách hàng" in userText:
        names = ["Anh Tuấn", "Chị Lan", "Bạn Minh", "Anh Long"]
        staff = random.choice(names)
        return f"Đây là bộ phận chăm sóc khách hàng: <strong>{staff}</strong>. Bạn cần hỗ trợ gì ạ?"

    
    else:
        response = chatbot.get_response(userText)
        return str(response)


if __name__ == "__main__":
    app.run(debug=True)
