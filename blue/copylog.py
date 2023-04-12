import json

from flask import Blueprint, render_template,request
from model.DB_manage import Select_table,Operate_table


copy_log = Blueprint('copylog', __name__)  # 创建蓝图
table_name = 'item_detaile_res'             # 数据表名称


# 列表页面
@copy_log.route('/')
def copylog_list():
    if request.method == 'POST':
        data_json = request.get_data()         # 查询条件对象{}
        # res = Select_table(table_name).select_content_list()
    return render_template('copylog.html')


# 添加
@copy_log.route('/add', methods=['POST'])
def copylog_add():
    if request.method== 'POST':
        data_json = eval(request.get_data())
        res = Operate_table(table_name).Add(data_json)
    return str(res)


# 详情
@copy_log.route('/detaile', methods=['POST'])
def copylog_detaile():
    if request.method == 'POST':
        s_id = int(request.get_data())
        res = Operate_table(table_name).Detaile(s_id)
    return json.dumps(res)


# 删除
@copy_log.route('/del', methods=['POST'])
def copylog_del():
    if request.method == 'POST':
        s_id = int(request.get_data())
        res = Operate_table(table_name).Delete(s_id)
    return res


# 更新
@copy_log.route('/update', methods=['POST'])
def copylog_update():
    if request.method == 'POST':
        data_json = request.get_data()
        print(eval(data_json))
    return '更新复制日志'