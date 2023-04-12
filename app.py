from flask import Flask,render_template
from blue.setting import set_page
from blue.copylog import copy_log


app = Flask(__name__)

# 设置蓝图注册
app.register_blueprint(set_page, url_prefix='/setpage')
app.register_blueprint(copy_log, url_prefix='/copylog')


@app.route('/')
def hello_world():
    return render_template('set.html')


if __name__ == '__main__':
    app.run(debug=True)
