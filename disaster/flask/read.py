from flask import Flask

app=Flask(__name__)


topics=[
    {'id':1, 'title':'html','body': 'html is ...'},
    {'id':2, 'title':'css','body': 'css is ...'},
    {'id':3, 'title':'javascript','body': 'javascript is ...'},
]


def template(contents, content):   # 중복된 코드 하나로 묶기
     return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}           
        </body>
    </html>
    '''


def getContents():   # 중복된 코드 하나로 묶기
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags



@app.route('/')
def indenx():
    return template(getContents(), '<h2>Welcome</h2>Hello, Web')


@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(), f'<h2>{title}</h2>{body}')

app.run(debug=True)
