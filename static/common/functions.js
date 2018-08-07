function addgoods(id) {

    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/app/add_card/',
        type: 'POST',
        data: {'goods_id': id},
        dataType: 'json',
        headers:{'X-CSRFToken': csrf},
        success: function (data) {
            if (data.code == '200') {
                $('.num_show_'+ id).val(data.c_num)
                $('#cart_price_'+ id).html(data.count)
                console.log(data)
                get_count_price()
            }
        },
        error: function (data) {
            alert('请求失败')
        }
    })
}


function subgoods(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/app/sub_card/',
        data:{'goods_id':id},
        dataType:'json',
        type:'POST',
        headers:{'X-CSRFToken': csrf},
        success:function(data){
            if(data.code == '200'){
                $('.num_show_'+ id).val(data.c_num)
                $('#cart_price_'+ id).html(data.count)
                console.log(data)
                get_count_price()
            }
        },
        error:function(data){
            alert('删除商品失败')
        }
    });
}


$.get('/app/goods_num/', function (data) {
    if (data.code == '200') {
        for (var i=0;i<data.carts.length;i++) {
            alert('123')
            $('#goods_'+ data.carts[i].goods_id).val(data.carts[i].c_num)
            // $('num_show_'+ data.carts[i].goods_id).val(data.carts[i].c_num)
        }
    }
});

// 总计
function get_count_price(){

    $.get('/app/goods_count/', function(data){
        if(data.code == '200'){
            $('#all_price').html(data.count)
            $('#all_num').html(data.num)
        }
    });
}

get_count_price()

