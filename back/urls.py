from django.conf.urls import url

from back import views

urlpatterns = [
    # 登录
    url(r'^login/', views.login, name='login'),
    # 商品列表
    url(r'^product_list/', views.product_list, name='product_list'),
    # 修改商品
    url(r'^charge_list/', views.charge_list, name='charge_list'),
    # 删除商品
    url(r'^del_list/', views.del_list, name='del_list'),
    # 添加商品
    url(r'^product_detail/', views.product_detail, name='product_detail'),
    # 商品分类
    url(r'^product_category/', views.product_category, name='product_category'),
    # 回收站
    url(r'^recycle_bin/', views.recycle_bin, name='recycle_bin'),
    # 回收站恢复
    url(r'^cancel_del/', views.cancel_del, name='cancel_del'),
    # 彻底删除
    url(r'^thorough_del/', views.thorough_del, name='thorough_del'),
    # 订单列表
    url(r'^order_list/', views.order_list, name='order_list'),
    # 订单详情
    url(r'^order_detail/', views.order_detail, name='order_detail'),
]
