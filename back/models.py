from django.db import models


# 创建商品种类模型
class ArticleCategory(models.Model):
    kind = models.CharField(max_length=30)            # 分类
    isDelete = models.BooleanField(default=False)     # 是否删除

    class Meta:
        db_table = "sx_kind"


class BackUser(models.Model):
    username = models.CharField(max_length=32, unique=True)  # 名称
    password = models.CharField(max_length=256)  # 密码

    class Meta:
        db_table = 'back_users'


class BackUserTicket(models.Model):
    back_user = models.ForeignKey(BackUser)  # 关联管理用户
    ticket = models.CharField(max_length=256)  # 密码
    out_time = models.DateTimeField()  # 过期时间

    class Meta:
        db_table = 'back_users_ticket'


# 商品详情
class BackProductList(models.Model):
    icons = models.ImageField(upload_to='icons')  # 图片
    list_name = models.CharField(max_length=50)  # 产品名称
    list_num = models.CharField(max_length=20)   # 货号
    list_price = models.FloatField(default=0)    # 单价
    list_unit = models.IntegerField(default=1)   # 单位
    list_stock = models.IntegerField(default=1)  # 库存
    is_del = models.BooleanField(default=True)  # 是否删除
    # 关联商品种类
    list_sort = models.ForeignKey(ArticleCategory)

    class Meta:
        db_table = 'back_product_list'
