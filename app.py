from flask import Flask
from blue.setting import set_page


app = Flask(__name__)

# 设置蓝图注册
app.register_blueprint(set_page, url_prefix='/set_page')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
