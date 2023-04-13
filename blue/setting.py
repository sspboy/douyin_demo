import json

from flask import Blueprint, render_template,request
from model.DB_manage import Select_table,Operate_table


set_page = Blueprint('setpage', __name__)  # 创建蓝图
table_name = 'shop_setting'                 # 数据表名称


# 设置页面路由
@set_page.route('/', methods=['POST'])
def setlist():
    if request.method == 'POST':
        data_json = request.get_data()
    return '设置列表'


# 添加
@set_page.route('/add', methods=['POST'])
def setadd():
    if request.method== 'POST':
        data_json = request.get_data()
        res = Operate_table(table_name).Add(eval(data_json))
    return str(res)


# 详情
@set_page.route('/detaile', methods=['POST'])
def setdetaile():
    if request.method == 'POST':
        s_id = int(request.get_data())
        res = Operate_table(table_name).Detaile(s_id)
    return res


# 删除
@set_page.route('/del', methods=['POST'])
def setdel():
    if request.method == 'POST':
        s_id = int(request.get_data())
        res = Operate_table(table_name).Delete(s_id)
    return res


# 更新
@set_page.route('/update', methods=['POST'])
def setupdate():
    if request.method == 'POST':
        data_json = request.get_data()
        print(eval(data_json))
    return '更新设置'