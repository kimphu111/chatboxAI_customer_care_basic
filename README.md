
step1 (mở terminal ở file explorer): git clone https://github.com/kimphu111/chatboxAI_customer_care_basic.git

step2: open in vs code
step3: open terminal
step4:cd chatboxAI
step5 (thấy folder venv rồi thì bỏ qua bước này):python -m venv venv
step6: venv\Scripts\activate 

//libary nesscessary
step7:pip install flask chatterbot==1.0.5 chatterbot_corpus pyyaml spacy
step8:python -m spacy download en_core_web_sm
step9: python app.py
step10: click the url mở giao diện lên  