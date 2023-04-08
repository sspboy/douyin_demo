from DB.DB import Data
import datetime, json, math


# 数据表-组件+翻页+跳转指定页面
class Select_table():

    # 参数 数据表名称\查询条件where、排序条件order by desc asc、翻页数量、翻页条数、第几页
    config = {
        'table_name': '',
        'condition': [

        ],
        # where 多条件、排序 order by name asc desc、like %关键字% 模糊匹配
        # 模糊匹配 WHERE name LIKE ‘%孙%'；
        # 文本条件 where id='1231231'
        # 时间范围 where start_time > '2020-08-24 00:00:00' and end_time < '2020-08-24 00:00:00'
        # 排序条件 order by name asc desc

        'page_size': '',
        'page': ''}

    def __init__(self, table_name, page=1, page_size=10, condition=None):
        self.table_name = table_name
        self.page = page
        self.page_size = page_size
        self.condition = condition

    # 转译条件语句
    def translation_condition(self):

        if self.condition != None:  # 条件不为空
            where_text = ''
            o_text = ''
            for i in self.condition:
                type = i.get('type')
                if type == 'where':  # 筛选 where语句
                    w_text = ''
                    condition = i.get('condition')
                    for w in condition:
                        w_text = w_text + ' and ' + w.get('column_name') + ' ' + w.get('operator') + ' ' + "'" + w.get(
                            'value') + "'"
                    where_text = 'where' + w_text[4:]

                if type == 'orderby':  # 排序 orderby
                    condition = i.get('condition')[0]

                    o_text = ' order by ' + condition.get('column_name') + ' ' + condition.get('value')
            condition_text = where_text + o_text

            return condition_text
        else:  # 条件为空
            return None

    # 获取表的列名称
    def select_column(self):
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s';" % self.table_name
        res = Data().select(sql)
        column_list = []
        for i in res:
            column_list.append(i[0])
        return column_list

    def page_num(self):  # limit(page_num, page_size)
        page = self.page
        if page <= 1:
            page_num = 0
        elif page > 1:
            page_num = (page - 1) * self.page_size
        return page_num

    def get_total_page_num(self):  # 获取内容总页数-可见

        # 需要where 条件计算出内容总页数
        sql = "select count(*) from %s %s;" % (self.table_name, self.translation_condition())
        # print(sql)

        res = Data().select(sql)
        total_page = int(math.ceil(int(res[0][0]) / (self.page_size + 0.0)))
        return total_page

    def select_content_list(self):  # 查询内容列表

        name_list = self.select_column()  # 表头

        # 需要where条件+排序条件
        sql = "select * from %s %s limit %s,%s;" % (
        self.table_name, self.translation_condition(), self.page_num(), self.page_size)
        # print(sql)
        res = Data().select(sql)
        res_list = []
        for i in res:
            list_one = list(i)
            res_one = dict(list(zip(name_list, list_one)))
            res_list.append(res_one)
        return res_list

    def get_page_list(self, total_page):  # 翻页列表11页
        total_list = []

        for i in range(1, total_page + 1):
            total_list.append(i)

        if self.page <= 6:
            # 截取总列表前11位
            page_list = total_list[:11]
        elif self.page > 6 and self.page < total_page - 6:
            # 截取 当前左侧5位
            page_list_left = total_list[self.page - 6:self.page]
            # 截取 当前右侧5位
            page_list_right = total_list[self.page:self.page + 5]
            # 拼接为一个list
            page_list = page_list_left + page_list_right
        elif self.page > total_page - 6:
            page_list = total_list[total_page - 11:]
        return page_list

    def page_message(self):  # 翻页信息=当前页，上一页，下一页，页面列表

        page_message = dict()

        page_message['now_page'] = self.page  # 当前页

        total_page = self.get_total_page_num()

        page_message['total_page'] = total_page  # 总页数

        page_message['page_list'] = self.get_page_list(total_page)  # 总页数

        previous_page = self.page - 1  # 上一页int(page_num) - 1

        if previous_page <= 0:
            previous_page = 1

        page_message['previous_page'] = previous_page  # 上一页

        next_page = self.page + 1  # 下一页int(page_num) + 1

        if next_page > total_page:
            next_page = total_page

        page_message['next_page'] = next_page  # 下一页

        page_message['data'] = self.select_content_list()  # 数据列表

        return page_message


# 商品上传配置
setting_data = {

    # 店铺id
    "shop_id": "123123",

    # 配置名称
    "set_name": "配置文件数据格式",
    # 标题配置
    "title":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    # 图片配置
    "pic":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    # 详情配置
    "desc_url":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    # 价格配置
    "price":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    # 商品类目
    "pro_class":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    "pro_format":"0",    # 属性
    "pro_type":"1",      # 类型
    "mobile":"13888888812",    # 客服电话
    "freight_id":"0",    # 运费模板
    "reduce_type":"0",    # 减库存方式
    "commit_msg":"1",        # 上传方式

    "recommend_remark":"发递四方速递",      # 推荐语
    "pay_type":"1",              # 支付方式
    "start_sale_type":"1",       # 上架方式
    "standard_brand_id":"57864",    # 品牌id
    "supply_7day_return":"1",    # 七天无理由
    "size_info_template_id":"0",    # 尺码模板
    # 限购
    "purchase": {"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    # 特殊时间延迟发货
    "delay_rule":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    # 商品发货模式
    "presell_config_level":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""}

}

# 数据表-增、删、改、查(id详情)
class Operate_table():

    def __init__(self, table_name):
        # 数据库名称
        self.table_name = table_name

    # 获取表的列名称
    def select_column(self):
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s';" % self.table_name
        res = Data().select(sql)
        column_list = []
        for i in res:
            column_list.append(i[0])
        return column_list

    # 插入设置数据
    def Add(self, setting_data):

        db_name = ''
        db_value = ''
        for x, y in setting_data.items():
            if y != '':
                db_name = db_name + x + ','
                if type(y) == dict:     # json 字段处理
                    db_value = db_value + "'" + json.dumps(y) + "'" + ','
                elif type(y) == int:    # 整数字段处理
                    db_value = db_value + y + ','
                else:                   # 文本字段处理
                    db_value = db_value + "'" + str(y) + "'" + ','

        sql="insert into %s (%s) value (%s)" % (self.table_name, db_name[:-1],db_value[:-1])
        # print (sql)
        res = Data().inset(sql)
        return res

    # 查询设置数据
    def Select_id(self, set_id):
        name_list = self.select_column()  # 表头
        sql = "select * from %s where id='%s'" % (self.table_name, set_id)
        res = Data().select(sql)
        res_one = dict(list(zip(name_list, res[0])))
        return res_one

    # 更新指定id的设置信息
    def Update(self, setting_data, set_id):
        db_text = ''
        for x, y in setting_data.items():
            if y != '':
                if type(y) == dict:     # json 字段处理
                    db_text = db_text + x + '=' + "'" + json.dumps(y) + "'" + ','
                elif type(y) == int:    # 整数字段处理
                    db_text = db_text + x + '=' + y + ','
                else:                   # 文本字段处理
                    db_text = db_text + x + '=' + "'" + str(y) + "'" + ','
        sql = "UPDATE %s SET %s WHERE id=%s" % (self.table_name, db_text[:-1], set_id)
        # print (sql)
        res = Data().updata(sql)
        return res

    # 删除指定的设置信息
    def Delete(self,set_id):
        sql = "delete from %s where id='%s'" % (self.table_name, set_id)
        res = Data().delete(sql)
        return res


if __name__ == '__main__':
    # table:列表、翻页、多条件查询：：：：条件配置说明
    condition = [
        {'type': 'where',
         'condition': [
            #{'column_name': 'create_time', 'value': '2020-11-16 16:10:10', 'operator': '>'},
            #{'column_name': 'create_time', 'value': '2023-11-16 16:12:10', 'operator': '<'},
            {'column_name':'shop_id','value':'123123','operator':'='}]},                                  # 查询条件语句
        # {'type':'where','condition':[{'column_name':'shop_id','value':'%1312830%','operator':'like'}]}, # 模糊查询语句
        {'type': 'orderby', 'condition': [{'column_name': 'id', 'value': 'asc', }]}                       # 排序条件语句
    ]
    Select_table = Select_table('shop_setting', 1, 10, condition)  # 示例化查询用例
    res_msg = Select_table.page_message()  # 获取结果json
    # print(json.dumps(res_msg, indent=4, ensure_ascii=False))  # 打印json格式
    for i in res_msg.get('data'):
        i['create_time'] = str(i.get('create_time'))
        i['updata_time'] = str(i.get('updata_time'))
        print(i)  # 打印json格式


    ####### table的增、删、改、查(id详情)

    # 新增
    # Operate_table('shop_setting').Add(setting_data)


    # 删除
    # Operate_table('shop_setting').Delete(5)


    # 查询详情
    # res = Operate_table('shop_setting').Select_id(2)
    # print (res)


    # 更新
    # Operate_table('shop_setting').Update(setting_data,3)