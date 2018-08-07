from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.models import CartModel
from back.models import BackProductList


def index(request):
    # 首页
    if request.method == 'GET':
        # 分类
        product = BackProductList.objects.filter(is_del=1)[:4]

        data = {
            'product': product,
        }
        return render(request, 'index.html', data)


# 商品列表
def product_list(request):
    if request.method == 'GET':
        return render(request, 'list.html')


# 商品详情
def detail(request):
    if request.method == 'GET':
        det_id = request.GET.get('pro_id')
        # 筛选id，只拿到一个id的所有数据
        details = BackProductList.objects.filter(id=det_id)
        return render(request, 'detail.html', {'detail': details})


# 增加商品数量
def add_card(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        data['code'] = '1001'
        if user.id:
            goods_id = request.POST.get('goods_id')
            # 验证当前登录用户是否对同一商品进行添加操作
            cart = CartModel.objects.filter(user=user, goods_id=goods_id)
            cat = cart.first()
            if cart:
                cat.c_num += 1
                cat.save()
                data['c_num'] = cat.c_num
                count_price = cat.goods.list_price * cat.c_num
                data['count'] = count_price
            else:
                # 登录的当前用户没有添加商品到购物车中，则创建
                CartModel.objects.create(user=user, goods_id=goods_id)
                data['c_num'] = 1
                cat = CartModel.objects.filter(user=user, goods_id=goods_id).first()
                count_price = cat.goods.list_price
                data['count'] = count_price
            data['code'] = '200'
            data['msg'] = '请求成功'
            return JsonResponse(data)
        return JsonResponse(data)


# 减少商品数量
def sub_card(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        data['code'] = '1002'
        if user.id:
            goods_id = request.POST.get('goods_id')
            cart = CartModel.objects.filter(user=user, goods_id=goods_id)
            if cart:
                cat = cart.first()
                if cat.c_num == 1:
                    cat.delete()
                    data['c_num'] = 0
                else:
                    cat.c_num -= 1
                    cat.save()
                    data['c_num'] = cat.c_num
                    count_price = cat.goods.list_price * cat.c_num
                    data['count'] = count_price
                data['c_num'] = cat.c_num
                data['code'] = '200'
                return JsonResponse(data)
            else:
                data['msg'] = '请添加商品'
                return JsonResponse(data)
        else:
            data['msg'] = '请先登录'
            return JsonResponse(data)


# 刷新页面
def goods_num(request):
    if request.method == 'GET':
        user = request.user
        cart_list = []
        if user.id:
            carts = CartModel.objects.filter(user=user)
            for cart in carts:
                data = {
                    'id': cart.id,
                    'goods_id': cart.goods.id,
                    'c_num': cart.c_num,
                    'user_id': cart.user.id
                }
                cart_list.append(data)
                return JsonResponse({'carts': cart_list, 'code': '200'})
        else:
            JsonResponse({'carts': '', 'code': '1002'})


# 计算总价
def goods_count(request):
    if request.method == 'GET':
        user = request.user

        carts = CartModel.objects.filter(user=user, is_select=True)
        count_price = 0
        num = 0
        for cart in carts:
            count_price += cart.goods.list_price * cart.c_num
            num += 1

        return JsonResponse({'count': count_price, 'code': 200, 'num': num})


# 购物车
def cart(request):
    if request.method == 'GET':
        user = request.user
        carts = CartModel.objects.filter(user=user)
        return render(request, 'cart.html', {'carts': carts})


# 删除购物车
def cart_del(request):
    if request.method == 'GET':
        user = request.user
        cart_id = request.GET.get('cart_id')
        cart = CartModel.objects.filter(user=user, id=cart_id)
        cart.delete()
        return HttpResponseRedirect(reverse('app:cart'))


# 用户中心
def user_center_info(request):

    if request.method == 'GET':
        user = request.user
        return render(request, 'user_center_info.html')

