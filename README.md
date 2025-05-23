cd chatboxAI
python -m venv venv
venv\Scripts\activate 

//libary nesscessary
pip install flask chatterbot==1.0.5 chatterbot_corpus pyyaml spacy
python -m spacy download en_core_web_sm