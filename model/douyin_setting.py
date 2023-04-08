import json
from DB.DB import Data


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


class Operate_table():

    def __init__(self, table_name):
        # 数据库名称
        self.table_name = table_name

    def select_column(self):  # 获取表的列名称
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s';" % self.table_name
        res = Data().select(sql)
        column_list = []
        for i in res:
            column_list.append(i[0])
        return column_list

    def Add(self, setting_data):        # 插入设置数据

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

    def Select_id(self, set_id):    # 查询设置数据
        name_list = self.select_column()  # 表头
        sql = "select * from %s where id='%s'" % (self.table_name, set_id)
        res = Data().select(sql)
        res_one = dict(list(zip(name_list, res[0])))
        return res_one

    def Update(self, setting_data, set_id):     # 更新指定id的设置信息
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

    def Delete(self,set_id):        # 删除指定的设置信息
        sql = "delete from %s where id='%s'" % (self.table_name, set_id)
        res = Data().delete(sql)
        return res

# 新增
# Operate_table('shop_setting').Add(setting_data)


# 删除
# Operate_table('shop_setting').Delete(5)


# 查询详情
# res = Operate_table('shop_setting').Select_id(2)
# print (res)


# 更新
# Operate_table('shop_setting').Update(setting_data,3)