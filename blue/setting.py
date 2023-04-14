from flask import Blueprint, render_template,request
from model.DB_manage import Operate_table,Select_table

set_page = Blueprint('setpage', __name__)
table_name = 'shop_setting'             # 数据表名称


# 列表
@set_page.route('/', methods=['POST'])
def setlist():
    if request.method == 'GET':
        shop_id = request.get_data()
    return '设置列表'


# 添加
@set_page.route('/add', methods=['POST'])
def setadd():
    if request.method == 'POST':
        data_json = request.get_data()
        res = Operate_table(table_name).Add(eval(data_json))
    return str(res)


# 详情
@set_page.route('/detaile', methods=['POST'])
def setdetaile():
    if request.method == 'POST':
        s_id = request.get_data()
        res = Operate_table(table_name).Detaile(s_id)
    return res


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
        res = Operate_table(table_name).Delete(int(s_id))
    return res
