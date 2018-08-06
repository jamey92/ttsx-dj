from datetime import datetime

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponseRedirect, render

from user.models import UserTicketModel


class UserMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 需要登录验证
        need_login = ['/app/cart/', '/app/user_center_info/', '/app/detail/',
                      '/app/add_card/', '/app/sub_card/',
                      '/app/goods_count/', '/app/goods_num/', '/app/cart_del/']
        if request.path in need_login:
            # 获取cookies中的ticket参数
            ticket = request.COOKIES.get('ticket')
            # 如果没有ticket, 跳转到登录
            if not ticket:
                return HttpResponseRedirect(reverse('user:login'))

            user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
            if not user_ticket:
                return HttpResponseRedirect(reverse('user:login'))

            if user_ticket.out_time.replace(tzinfo=None) < datetime.now():
                # 获取认证，验证认证是否过期
                user_ticket.delete()
                return HttpResponseRedirect(reverse('user:login'))

            request.user = user_ticket.user
