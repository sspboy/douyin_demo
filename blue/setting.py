import json

from flask import Blueprint, render_template,request
from model.DB_manage import Select_table,Operate_table


set_page = Blueprint('set_page', __name__)  # 创建蓝图
table_name = 'max.shop_setting'             # 数据表名称


# 设置页面路由
@set_page.route('/', methods=['GET'])
def setlist():
    return '设置列表'


# 添加
@set_page.route('/add', methods=['POST'])
def setadd():
    if request.method== 'POST':
        data_json = request.get_data()
        print(eval(data_json))
        print(type(data_json))
    return data_json


# 详情
@set_page.route('/select_detaile', methods=['POST'])
def select_detaile():
    if request.method == 'POST':
        data_json = request.get_data()
        print(data_json)
    return '编辑设置'


# 删除
@set_page.route('/del', methods=['POST'])
def setdel():
    if request.method == 'POST':
        data_json = str(request.get_data())
        print(data_json)
    return '删除设置'


# 更新
@set_page.route('/update', methods=['POST'])
def setupdate():
    if request.method == 'POST':
        data_json = request.get_data()
        print(eval(data_json))
    return '更新设置'