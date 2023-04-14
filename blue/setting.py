from flask import Blueprint, render_template,request
from model.DB_manage import Operate_table,Select_table

set_page = Blueprint('setpage', __name__)   # 注册蓝图
table_name = 'shop_setting'             # 数据表名称


# 列表
@set_page.route('/', methods=['POST'])
def setlist():
    if request.method == 'POST':
        shop_id = request.get_data()
        res = Select_table(table_name).select_content_list()
    return res


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
        res = Operate_table(table_name).Detaile(int(s_id))
    return res


# 更新设置
@set_page.route('/update', methods=['POST'])
def setupdate():
    if request.method == 'POST':
        json_data = request.get_data()
        res = Operate_table(table_name).Update(json_data)
    return res


# 删除设置
@set_page.route('/del', methods=['POST'])
def setdel():
    if request.method == 'POST':
        s_id = request.get_data()
        res = Operate_table(table_name).Delete(int(s_id))
    return res
