from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from user.models import UserModel, UserTicketModel
from utils.functions import get_ticket


def register(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        password1 = request.POST.get('cpwd')
        email = request.POST.get('email')
        # 验证的参数不为空
        if not all([username, password, email]):
            msg = '参数不能为空'
            return render(request, 'register.html', {'msg': msg})
        # 判断两次输入的密码是否一致
        if password == password1:
            # 加密
            password = make_password(password)
            # 创建账号密码
            UserModel.objects.create(username=username,
                                     password=password,
                                     email=email)
            return HttpResponseRedirect(reverse('user:login'))
        else:
            return render(request, 'register.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        data = {}
        # 判断用户名是否存在
        if UserModel.objects.filter(username=username).exists():
            user = UserModel.objects.get(username=username)
            # 密码验证
            if check_password(password, user.password):
                # 存ticket在cookie中
                ticket = get_ticket()
                res = HttpResponseRedirect(reverse('app:user_center_info'))
                # 过期时间
                out_time = datetime.now() + timedelta(days=2)
                res.set_cookie('ticket', ticket, expires=out_time)
                # 创建
                UserTicketModel.objects.create(user=user,
                                               ticket=ticket,
                                               out_time=out_time)
                return res
            else:
                data['msg'] = '密码错误'
                return render(request, 'login.html')
        else:
            data['msg'] = '账号错误'
            return render(request, 'login.html')
