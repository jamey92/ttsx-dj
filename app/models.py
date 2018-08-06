from django.db import models

from back.models import BackProductList
from user.models import UserModel


# 购物车
class CartModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    goods = models.ForeignKey(BackProductList)  # 关联商品
    c_num = models.IntegerField(default=1)  # 商品的个数
    is_select = models.BooleanField(default=True)  # 是否选择

    class Meta:
        db_table = 'sx_carts'


# 订单
class OrderModel(models.Model):
    goods = models.ForeignKey(BackProductList)
    o_user = models.ForeignKey(UserModel)  # 关联用户
    o_date = models.DateTimeField(auto_now=True)  # 购买日期
    o_pay = models.BooleanField(default=False)  # 付款属性
    o_total = models.DecimalField(max_digits=6, decimal_places=2)  # 总价
    o_address = models.CharField(max_length=150)  # 收货地址
    o_peisong = models.CharField(max_length=50)  # 配送方式

    class Meta:
        db_table = 'sx_orders'
