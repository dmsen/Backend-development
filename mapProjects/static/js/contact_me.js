 <!--开始实现我们的数据库ajax-->
    $("#submit").click(function () {
        $.ajax({
            //跨域访问
            //url:'http:192.168.0.103:8000/check_name/'
            //本地访问

            url: 'check_form',
            type: 'POST',
            async: true,

            data: {username: $("#username").val(),
            email :$("input#email").val()},
            timeout: 500000,//超时时间
            dataType: 'json',//返回的数据格式：json/xml/html/script/jsonp/text
//            dataType:'jsonp',//如果是跨域请求数据
//            json:'callback',

            //callback:'jsonp',
            beforeSend: function (xhr) {
                console.log(xhr);
                console.log('发送前')
            },
            success: function (data,textStatus,jqXHR) {
                console.log(data);


                //$("#userinfo").val("yonghu")
                console.log(textStatus);
                console.log(jqXHR);
            },
            error: function (xhr, textStatus) {
                console.log('错误');
                console.log(xhr);
                console.log(textStatus)
            },
            complete: function () {
                console.log('结束');

            }
        })
    })