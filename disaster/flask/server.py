from flask import Flask
import random

# 기본적인 flask 문법
app=Flask(__name__)

@app.route('/')
def index():
    return 'random: <strong>'+ str(random.random()) + '</strong>' # 문자열로 인식하게 해줘야 함. html 문법 넣어서 사용 가능.

app.run(debug=True) # debug: 자연적으로 flask 가 실행되고 종료되게끔 만듬. return에 오는 문자 바꿀 수 있음.
