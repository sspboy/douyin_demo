from DB.DB import Data
# 商品上传配置
setting_data = {

    # 店铺id
    "shop_id": "123",

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
    "desc":{"maximum_per_order": "",
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
    "mobile":"138888888",    # 客服电话
    "freight_id":"0",    # 运费模板
    "reduce_type":"0",    # 减库存方式
    "commit":"1",        # 上传方式

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
db_name = ''
db_value = ''
for x,y in setting_data.items():
    if y != '':
        db_name = db_name + x + ','
        db_value = db_value + str(y) + ','
print (db_name)
print (db_value)

class Setting():

    def __init__(self):
        pass

    def Add(self, x, y):        # 插入设置数据
        sql="insert into max.shop_setting(%s) value (%s)" % (x[:-1],y[:-1])
        print (sql)
        res = Data().inset(sql)
        return res

    def select_id(self, set_id):    # 查询设置数据
        pass

    def select_list(self):          # 查询设置信息列表、翻页、状态筛选
        pass

    def update(self, new_json):     # 更新指定id的设置信息
        pass

    def delete(self,set_id):        # 删除指定的设置信息
        pass


Setting().Add(db_name,db_value)
