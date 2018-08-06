from django.db import models


# 创建用户信息模型
class UserModel(models.Model):
    username = models.CharField(max_length=32, unique=True)  # 名称
    password = models.CharField(max_length=256)  # 密码
    email = models.CharField(max_length=64, unique=True)  # 邮箱
    recipients = models.CharField(max_length=10, default='')  # 收件人姓名
    uaddress = models.CharField(max_length=100)  # 收件人地址
    postcode = models.CharField(max_length=6)  # 收件人邮编
    uphone = models.CharField(max_length=11)  # 收件人电话

    class Meta:
        db_table = 'sx_users'


# 创建用户Ticket模型
class UserTicketModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    ticket = models.CharField(max_length=256)  # 密码
    out_time = models.DateTimeField()  # 过期时间

    class Meta:
        db_table = 'sx_users_ticket'
