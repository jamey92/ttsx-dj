from django.conf.urls import url

from app import views

urlpatterns = [
    # 首页
    url(r'^index/', views.index, name='index'),
    # 商品详情
    url(r'^detail/', views.detail, name='detail'),
    # 添加商品
    url(r'^add_card/', views.add_card, name='add_card'),
    # 减少商品
    url(r'^sub_card/', views.sub_card, name='sub_card'),
    # 计算总价
    url(r'^goods_count/', views.goods_count, name='goods_count'),
    # 刷新页面
    url(r'^goods_num/', views.goods_num, name='goods_num'),
    # 商品列表
    url(r'^product_list/', views.product_list, name='product_list'),
    # 用户中心
    url(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    # 购物车
    url(r'^cart/', views.cart, name='cart'),
    # 删除购物车商品
    url(r'^cart_del/', views.cart_del, name='cart_del'),
]
