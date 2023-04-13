<<<<<<<<< Temporary merge branch 1
from flask import Blueprint, render_template
=========
from flask import Blueprint, render_template,request
>>>>>>>>> Temporary merge branch 2

set_page = Blueprint('set_page', __name__)


# 设置页面路由
<<<<<<<<< Temporary merge branch 1
@set_page.route('/')
=========
@set_page.route('/', methods=['POST'])
>>>>>>>>> Temporary merge branch 2
def setlist():
    if request.method == 'GET':
        shop_id = request.get_data()
    return '设置列表'


# 添加设置
<<<<<<<<< Temporary merge branch 1
@set_page.route('/add')
def setadd():
=========
@set_page.route('/add', methods=['POST'])
def setadd():
    if request.method == 'POST':
        shop_id = request.get_data()
>>>>>>>>> Temporary merge branch 2
    return '添加设置'


# 编辑设置
<<<<<<<<< Temporary merge branch 1
@set_page.route('/edit')
def setedit():
=========
@set_page.route('/edit', methods=['POST'])
def setedit():
    if request.method == 'POST':
        shop_id = request.get_data()
>>>>>>>>> Temporary merge branch 2
    return '编辑设置'


# 删除设置
<<<<<<<<< Temporary merge branch 1
@set_page.route('/del')
def setdel():
=========
@set_page.route('/del', methods=['POST'])
def setdel():
    if request.method == 'POST':
        s_id = request.get_data()
>>>>>>>>> Temporary merge branch 2
    return '删除设置'
