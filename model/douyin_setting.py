from DB.DB import Data
# 商品上传配置
setting_data = {

    # 店铺id
    "shop_id": "123",

    # 配置名称
    "set_name": "配置文件数据格式",
    # id
    # create_time
    # updata_time

    "title":"", # 标题配置
    "pic":"",   # 图片配置
    "desc":"",  #详情配置
    "price":"", # 价格配置
    "pro_class"
    # pro_format
    # pro_type
    # mobile
    # freight_id
    # reduce_type
    # commit
    # recommend_remark
    # pay_type
    # start_sale_type
    # standard_brand_id
    # supply_7day_return
    # size_info_template_id
    # purchase
    # delay_rule
    # presell_config_level

    # 标题配置

    # 价格配置

    # 详情配置

    # 商品类型
    "product_type": "1",

    # 客服电话
    "mobile": "",

    # 运费模板
    "freight_id": "",

    # 减库存方式
    "reduce_type": "",

    # 上传方式
    "commit": "",

    # 推荐语
    "recommend_remark": "",

    # 支付方式
    "pay_type": "",

    # 上架方式
    "start_sale_type": "",

    # 品牌id
    "standard_brand_id": "",

    # 商品类目



    # 七天无理由
    "supply_7day_return": "",

    # 尺码模板
    "size_info_template_id": "",

    # 限购
    "purchase": {"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},

    # 特殊时间延迟发货

    # 商品属性

    # 商品发货模式

}


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
