/** 异步 网络请求方法 XHR */
var XHR = {

    /** 正则替换json 19位数字精度问题
     * var res = JSON.parse(res.replace(/\"product_id\":(\d+)/g,'"product_id":"$1"'));    // 返回商品id的数字精度转换*/

    /** promise Get 请求接口方法*/
    PromiseGet:function (url) {

        return new Promise(function (resolve, reject){

            var xhr = new XMLHttpRequest();// 实例化异步请求方法

            xhr.open('GET', url, false);// 执行get传参

            xhr.onreadystatechange = function () {

                if (xhr.readyState == 4){

                    resolve(xhr.responseText);      // 回调

                }; // 回调函数执行方法

            };

            xhr.send();// 发送请求

        });
    },
    GetMsg:function (url,callback,way=true) {

        var httpRequest = new XMLHttpRequest();
        httpRequest.open('GET', url, way);
        httpRequest.send();

        /** *获取数据后回调函数方法 */
        httpRequest.onreadystatechange = function () {                              //请求后的回调接口，可将请求成功后要执行的程序写在其中

            if (httpRequest.readyState == 4 && httpRequest.status == 200) {         //验证请求是否发送成功

                callback(httpRequest.responseText)

            };
        };

    },

    PostMsg:function (url,data,callback,way=true) {
        var httpRequest = new XMLHttpRequest();
        httpRequest.open('POST', url, way);                            // 接收信息的URL
        httpRequest.setRequestHeader("Content-type","application/json;charset=UTF-8");    // 发送信息格式为json
        /** *获取数据后回调函数方法 */
        httpRequest.onreadystatechange = function () {                              //请求后的回调接口，可将请求成功后要执行的程序写在其中

            if (httpRequest.readyState == 4 && httpRequest.status == 200) {         //验证请求是否发送成功
                callback(httpRequest.responseText)
            };
        };

        httpRequest.send(data);
    }



};


/**-图片异步加载- 开始**/
var Delay_load_img = {

    action:function(start_pic_num){     // 第几张开始

        var imgs = document.querySelectorAll('img');

        for(var i = start_pic_num;i<imgs.length;i++) {

            var url = imgs[i].dataset.src;

            this.loadImage(imgs[i],url,this.showImage);

        }
    },

    loadImage:function (obj,url,callback) {

        var img = new Image();

        img.src = url;
        // 判断图片是否在缓存中
        if(img.complete){
            callback.call(img,obj);
            return;
        }

        // 图片加载到浏览器的缓存中回调函数
        img.onload = function(){
            callback.call(img,obj);
        }

    },

    showImage:function (obj) {
        obj.src = this.src;
    }


};
/**-图片异步加载- 结束**/


/** 新建弹窗方法 开始**/
var Create_windows = {

    // 新建弹出层
    model:function (id='myModal', title='标题', size='', button='true') {

        // id
        // title：标题
        // size：弹框大小
        // button：是否显示按钮
        // id+content：内容
        // id+closed：关闭按钮
        // id+affirm确认按钮

        if(button == 'true'){

            var title_closed = '<h7 class="modal-title">' + title + '</h7>';


            var modal_foot = '<div class="modal-footer" name="'+ id+'footer' + '" style="height: 64px;">' +
           '<button type="button" class="btn btn-secondary font-size-12" data-dismiss="modal" name="'+ id+'closed' +'">关闭</button>' +
           '<button type="button" class="btn btn-primary font-size-12" name="'+ id + 'affirm' +'">确认</button>\n' +
           '</div>'

        }else if(button == 'false'){

            var title_closed = '<h7 class="modal-title">' + title + '</h7>' +
            '<button type="button" class="close" data-dismiss="modal" aria-label="Close" name="'+ id+'closed' +'">\n' +
                '<span aria-hidden="true">&times;</span>\n' +
                '</button>';

            var modal_foot = '<div class="modal-footer" name="'+ id+'footer' +'" style="height: 64px;"></div>'

        }else if(button == 'closed'){
            var title_closed = '<h7 class="modal-title">' + title + '</h7>';

            var modal_foot = '<div class="modal-footer" name="'+ id+'footer' +'" style="height: 64px;">' +
           '<button type="button" class="btn btn-secondary font-size-12 m-auto" data-dismiss="modal" name="'+ id+'closed' +'">关闭</button>' +
           '</div>'

        }

        var model_html = '<div class="modal" tabindex="-1" id="' + id + '" data-backdrop="static">' +
            '<div class="modal-dialog '+ size +'">' +
           '<div class="modal-content">' +
           '<div class="modal-header">' +
           title_closed +
           '</div>' +
           '<div class="modal-body" name="'+ id + 'content' +'">' +
           '<p></p>' +
           '</div>' +
            modal_foot +
           '</div>' +
           '</div>' +
           '</div>';

        if(document.getElementById('model_div') == null){   // 判断弹窗容器是否存在

            var model_div=document.createElement('div');
            model_div.setAttribute('id','model_div');
            document.body.appendChild(model_div);

            var model_div = document.getElementById('model_div');
            model_div.innerHTML = model_html;

            // 关闭-清除html代码
            var closed_id = id+'closed';
            document.getElementsByName(closed_id)[0].onclick = function () {
                Create_windows.clear_model_div()
            }
        };

    },
    // 清除弹窗html
    clear_model_div:function() {document.getElementById('model_div').remove();}

};
/** 新建弹窗方法 结束**/

/** 添加列表、翻页、跳转方法、全选、反选 开始*/




/** 添加列表、翻页、跳转方法、全选、反选 结束*/


// ************-----------------------获取当前url参数方法
function getQueryVariable(variable)
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
}


//随机生成 min 到 max 之间的整数
function random(min,max){
    return Math.floor((max-min+1)*Math.random())+min;
}

// 数组去重复方法:::去重，把提交的重复商品链接去除；
function for_repeat(value, array) {
    for(var i=0;i<array.length;i++){
        if (value == array[i]){
            return true
        };
    };
};




// 获取当前时间戳
function get_time_par() {
    var d = new Date();
    var t = d.getTime();
    return t
};


// 时间戳
function time() {

    var dt = new Date();
    var y = dt.getFullYear();//获取四位数年
    var m = dt.getMonth() + 1;//获取月份
    m = m < 10 ? ('0' + m) : m;  //判断月是否大于10
    var d = dt.getDate();//获取日期
    d = d < 10 ? ('0' + d) : d;  //判断日期是否大10
    var h = dt.getHours();//获取时
    h = h < 10 ? ('0' + h) : h;  //判断时是否大10
    var i = dt.getMinutes();//获取分
    i = i < 10 ? ('0' + i) : i;  //判断时是否大10
    var s = dt.getSeconds();//获取秒
    s = s < 10 ? ('0' + s) : s;  //判断时是否大10

    return  y+"-"+m+"-"+d+" "+h+":"+i+":"+s;//进行组合
};

var time_stamp = {

    // 获取当前时间格式：2020-09-12 12:21:12
    get_time_now:function() {

        var dt = new Date();
        var y = dt.getFullYear();//获取四位数年
        var m = dt.getMonth() + 1;//获取月份
        m = m < 10 ? ('0' + m) : m;  //判断月是否大于10
        var d = dt.getDate();//获取日期
        d = d < 10 ? ('0' + d) : d;  //判断日期是否大10
        var h = dt.getHours();//获取时
        h = h < 10 ? ('0' + h) : h;  //判断时是否大10
        var i = dt.getMinutes();//获取分
        i = i < 10 ? ('0' + i) : i;  //判断时是否大10
        var s = dt.getSeconds();//获取秒
        s = s < 10 ? ('0' + s) : s;  //判断时是否大10

        return  y+"-"+m+"-"+d+" "+h+":"+i+":"+s;//进行组合
    },
    // 时间错转时间格式
    filterTime(time_num) {

        const date = new Date(time_num);
        const Y = date.getFullYear();   // 年
        const M = date.getMonth() + 1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1;// 月
        const D = date.getDate();   // 日
        const H = date.getHours(); // 小时
        const I = date.getMinutes(); // 分钟
        const S = date.getSeconds(); // 秒

      return `${Y}-${M}-${this.isAddZero(D)} ${this.isAddZero(H)}:${this.isAddZero(I)}:${this.isAddZero(S)}`
    },
    // 下边这个方法是判断时间是否小于10，小于10 前边加0，更加规范一些，看自己需求
    isAddZero:function (time) {

        let str = time < 10 ? '0' + time : time.toString();

        return str
    }
};


// JSON 按键值排序方法
function Sort_JSON(Json_obj) {

    var arry_list = [];

    for(var key in Json_obj){
        arry_list.push(key)
    }
    arry_list.sort();   // 排序key
    let str = '';
    for(var i of arry_list){

        str = str + '"' + i + '"' +  ':' + '"' + Json_obj[i] + '",'

    }

    return '{' + str.substr(0,str.length-1) + '}'

}


// JavaScript 笛卡尔积算法，可用于商品 SKU 计算
function calcDescartes (array) {
    if (array.length < 2) return array[0] || [];
    return [].reduce.call(array, function (col, set) {
        var res = [];
        col.forEach(function (c) {
            set.forEach(function (s) {
                var t = [].concat(Array.isArray(c) ? c : [c]);
                t.push(s);
                res.push(t);
            })
        });
        return res;
    });
}


// 判断是否数字方法::
function isNumber(val) {
    var regPos = /^\d+(\.\d+)?$/; //非负浮点数
    var regNeg = /^(-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)))$/; //负浮点数
    if(regPos.test(val) || regNeg.test(val)) {
        return true;
        } else {
        return false;
        }
    };



// Bootstrap中模态框多层嵌套时滚动条问题
var modal_list = document.getElementsByName('Bootstrap_modal');

for(var i=0;i<modal_list.length;i++){

    modal_list[i].addEventListener('click',function () {
        Bootstrap_modal_open()
    });
    function Bootstrap_modal_open(){
        setTimeout("document.getElementsByTagName('body')[0].setAttribute('class','modal-open')",500);
    };
};

