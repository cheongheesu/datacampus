from flask import Flask

# 라우팅 (포트 연결)
app=Flask(__name__)

@app.route('/')
def indenx():
    return 'Welcome Back'


@app.route('/create/')
def create():
    return 'Create'


@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read'+ id


app.run(debug=True)