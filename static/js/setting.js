var Set = {

    /** set add**/
    add:()=>{
        /* url,data,callback */
        let url = 'http://127.0.0.1:5000/set_page/add'

        let data_json = "{'a':'添加设置'}"

        function sayhello(data){
            console.log(data)
        }

        XHR.PostMsg(url,data_json,sayhello,true)

    },
    /* set del */
    del:(set_id)=>{
        let url = 'http://127.0.0.1:5000/set_page/del'
        function sayhello(data){
            console.log(data)
        }

        XHR.PostMsg(url,set_id,sayhello,true)

    },
    /* set update */
    update:()=>{
        let url = 'http://127.0.0.1:5000/set_page/update'
        let data_json = "{'a':'更新设置'}"
        function sayhello(data){
            console.log(data)
        }

        XHR.PostMsg(url,data_json,sayhello,true)

    },
    /* set select_detaile */
    select_detaile:(set_id)=>{
        let url = 'http://127.0.0.1:5000/set_page/detaile'
        function sayhello(data){
            console.log(data)
        }

        XHR.PostMsg(url,set_id,sayhello,true)

    },
    /* set select_list */
    select_list:()=>{
        let url = 'http://127.0.0.1:5000/set_page/'
        function sayhello(data){
            console.log(data)
        }

        XHR.GetMsg(url,sayhello,true)

    },
}
// Set.update()
// Set.select_detaile(5)
Set.select_list()




