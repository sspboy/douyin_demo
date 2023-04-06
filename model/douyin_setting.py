from DB.DB import Data
# 商品上传配置
setting_data = {

    # 店铺id
    "shop_id": "123",

    # 配置名称
    "set_name": "配置文件数据格式",

    "title":"", # 标题配置
    "pic":"",   # 图片配置
    "desc":"",  #详情配置
    "price":"", # 价格配置
    "pro_class":"", # 商品类目
    "pro_format":"",    # 属性
    "pro_type":"",      # 类型
    "mobile":"",    # 客服电话
    "freight_id":"",    # 运费模板
    "reduce_type":"",    # 减库存方式
    "commit":"",        # 上传方式
    "recommend_remark":"",      # 推荐语
    "pay_type":"",              # 支付方式
    "start_sale_type":"",       # 上架方式
    "standard_brand_id":"",    # 品牌id
    "supply_7day_return":"",    # 七天无理由
    "size_info_template_id":"",    # 尺码模板
    # 限购
    "purchase": {"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    "delay_rule":"",                # 特殊时间延迟发货
    "presell_config_level":"",      # 商品发货模式

}
def myprint(**can):
    print (can)

class Setting():

    def __init__(self):
        pass

    def Add(self, res_json):        # 插入设置数据
        sql="insert max.shop_setting set shop_id=''"
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
