from flask import Blueprint, render_template,request

set_page = Blueprint('set_page', __name__)


# 设置页面路由
@set_page.route('/', methods=['POST'])
def setlist():
    if request.method == 'GET':
        shop_id = request.get_data()
    return '设置列表'


# 添加设置
@set_page.route('/add', methods=['POST'])
def setadd():
    if request.method == 'POST':
        shop_id = request.get_data()
    return '添加设置'


# 编辑设置
@set_page.route('/edit', methods=['POST'])
def setedit():
    if request.method == 'POST':
        shop_id = request.get_data()
    return '编辑设置'


# 删除设置
@set_page.route('/del', methods=['POST'])
def setdel():
    if request.method == 'POST':
        s_id = request.get_data()
    return '删除设置'
