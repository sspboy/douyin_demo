from flask import Blueprint, render_template

set_page = Blueprint('set_page', __name__)


# 设置页面路由
@set_page.route('/')
def setlist():
    return '设置列表'


# 添加设置
@set_page.route('/add')
def setadd():
    return '添加设置'


# 编辑设置
@set_page.route('/edit')
def setedit():
    return '编辑设置'


# 删除设置
@set_page.route('/del')
def setdel():
    return '删除设置'
