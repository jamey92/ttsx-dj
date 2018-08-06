from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from back.models import BackUser, BackProductList, ArticleCategory


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'backstage/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = {}
        if BackUser.objects.filter(username=username).exists():
            user = BackUser.objects.get(username=username)
            # 密码验证
            if check_password(password, user.password):
                return HttpResponseRedirect(reverse('back:product_list'))
            else:
                data['msg'] = '账号或密码错误'
                return HttpResponseRedirect(reverse('back:login'))
        else:
            data['msg'] = '账号或密码错误'
            return HttpResponseRedirect(reverse('back:login'))


# 商品列表
def product_list(request):
    if request.method == 'GET':
        products = BackProductList.objects.filter(is_del=1)
        return render(request, 'backstage/product_list.html',
                      {'products': products})


# 修改商品
def charge_list(request):
    if request.method == 'GET':
        pro_id = request.GET.get('pro_id')
        pro = BackProductList.objects.filter(id=pro_id).first()
        ctx = {'pro': pro}
        return render(request, 'backstage/product_detail.html', ctx)

    if request.method == 'POST':
        pro_id = request.GET.get('pro_id')
        list_name = request.POST.get('list_name')
        list_price = request.POST.get('list_price')  # 价格
        list_stock = request.POST.get('list_stock')  # 库存
        list_num = request.POST.get('list_num')  # 货号
        list_sort = request.POST.get('list_sort')  # 分类
        icons = request.FILES.get('icons')
        if not icons:
            a = ArticleCategory.objects.get(kind=list_sort)
            b = BackProductList.objects.filter(id=pro_id).first()
            b.list_name = list_name
            b.list_price = list_price
            b.list_stock = list_stock
            b.list_num = list_num
            b.list_sort_id = a.id
            b.save()
            return HttpResponseRedirect(reverse('back:product_list'))
        else:
            a = ArticleCategory.objects.get(kind=list_sort)
            b = BackProductList.objects.filter(id=pro_id).first()
            b.list_name = list_name
            b.list_price = list_price
            b.list_stock_id = list_stock
            b.list_num = list_num
            b.list_sort_id = a.id
            b.icons = icons
            b.save()
            return HttpResponseRedirect(reverse('back:product_list'))


# 删除商品
def del_list(request):
    if request.method == 'GET':
        pro_id = request.GET.get('pro_id')
        pro = BackProductList.objects.filter(id=pro_id).first()
        pro.is_del = 0
        pro.save()
        return HttpResponseRedirect(reverse('back:product_list'))


# 添加商品
def product_detail(request):
    if request.method == 'GET':
        return render(request, 'backstage/product_detail.html')

    if request.method == 'POST':
        list_name = request.POST.get('list_name')
        list_price = request.POST.get('list_price')  # 价格
        list_stock = request.POST.get('list_stock')  # 库存
        list_num = request.POST.get('list_num')  # 货号
        list_sort = request.POST.get('list_sort')  # 分类
        icons = request.FILES.get('icons')
        data = {}
        if not all([list_name, list_price, list_stock, list_num, icons]):
            data['msg'] = '请填写完整信息'
            return render(request, 'backstage/product_detail.html', data)
        else:
            a = ArticleCategory.objects.get(kind=list_sort)
            BackProductList.objects.create(list_name=list_name,
                                           list_price=list_price,
                                           list_stock=list_stock,
                                           list_num=list_num,
                                           list_sort_id=a.id,
                                           icons=icons)
            return HttpResponseRedirect(reverse('back:product_list'))


# 商品分类
def product_category(request):
    if request.method == 'GET':
        list_sort = request.GET.get('list_sort')  # 分类
        a = ArticleCategory.objects.get(kind=list_sort)
        if a.id == 7:
            BackProductList.objects.all()
            return HttpResponseRedirect(reverse('back:product_list'))
        else:
            BackProductList.objects.filter(list_sort_id=a.id).first()
            return HttpResponseRedirect(reverse('back:product_list'))


# 回收站
def recycle_bin(request):
    if request.method == 'GET':
        product = BackProductList.objects.filter(is_del=0)
        return render(request, 'backstage/recycle_bin.html', {'products': product})


# 撤销删除
def cancel_del(request):
    if request.method == 'GET':
        pro_id = request.GET.get('pro_id')
        pro = BackProductList.objects.filter(id=pro_id).first()
        pro.is_del = 1
        pro.save()
        return HttpResponseRedirect(reverse('back:recycle_bin'))


# 彻底删除
def thorough_del(request):
    if request.method == 'GET':
        pro_id = request.GET.get('pro_id')
        BackProductList.objects.filter(id=pro_id).delete()
        return HttpResponseRedirect(reverse('back:recycle_bin'))


# 订单列表
def order_list(request):
    if request.method == 'GET':
        return render(request, 'backstage/order_list.html')


# 订单详情
def order_detail(request):
    if request.method == 'GET':
        return render(request, 'backstage/order_detail.html')
