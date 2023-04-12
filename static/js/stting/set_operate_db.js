// 数据库操作

var Set_operate_db = {

    /** set add**/
    add:(data_json)=>{
        /* url,data,callback */
        let url = 'http://127.0.0.1:5000/setpage/add'
        function sayhello(data){
            console.log(data)
        }

        XHR.PostMsg(url,JSON.stringify(data_json),sayhello,true)

    },
    /* set del */
    del:(set_id)=>{
        let url = 'http://127.0.0.1:5000/setpage/del'
        function sayhello(data){
            console.log(data)
        }

        XHR.PostMsg(url,set_id,sayhello,true)

    },
    /* set update */
    update:()=>{
        let url = 'http://127.0.0.1:5000/setpage/update'
        let data_json = "{'a':'更新设置'}"
        function sayhello(data){
            console.log(data)
        }
        XHR.PostMsg(url,data_json,sayhello,true)

    },
    /* set select_detaile */
    detaile:(set_id)=>{
        let url = 'http://127.0.0.1:5000/setpage/detaile'
        function sayhello(data){
            console.log(JSON.parse(data).delay_rule)
        }

        XHR.PostMsg(url,set_id,sayhello,true)

    },
    /* set select_list */
    list:()=>{
        let url = 'http://127.0.0.1:5000/setpage/'
        var json_data = {'shop_id':'3432342'}
        function sayhello(data){
            console.log(data)
        }

        XHR.PostMsg(url,JSON.stringify(json_data),sayhello,true)

    },
}
// 商品上传配置
setting_data = {

    // 店铺id
    "shop_id": "123123",

    // 配置名称
    "set_name": "配置文件数据格式",
    // 标题配置
    "title":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    // 图片配置
    "pic":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    // 详情配置
    "desc_url":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    // 价格配置
    "price":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    // 商品类目
    "pro_class":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    "pro_format":"0",    // 属性
    "pro_type":"1",      // 类型
    "mobile":"13888888812",    // 客服电话
    "freight_id":"0",    // 运费模板
    "reduce_type":"0",    // 减库存方式
    "commit_msg":"1",        // 上传方式

    "recommend_remark":"发递四方速递",      // 推荐语
    "pay_type":"1",              // 支付方式
    "start_sale_type":"1",       // 上架方式
    "standard_brand_id":"57864",    // 品牌id
    "supply_7day_return":"1",    // 七天无理由
    "size_info_template_id":"0",    // 尺码模板
    // 限购
    "purchase": {"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    // 特殊时间延迟发货
    "delay_rule":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""},
    // 商品发货模式
    "presell_config_level":{"maximum_per_order": "",
                 "limit_per_buyer": "",
                 "minimum_per_order": ""}

}
// Set_operate_db.add(setting_data)         // 新增
// Set_operate_db.del(8)                    //删除
// Set_operate_db.update()                  // 更新
Set_operate_db.detaile(11)            // 详情 d_id
// Set_operate_db.list()                    // 列表 shop_id


