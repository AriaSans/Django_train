"""django_train_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings

from memberapp.views import depart, member, pretty, admin, accout, task, order, echarts, upload, city

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    path('login/', accout.login),
    path('logout/', accout.logout),

    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),

    path('depart/list/', depart.departList),
    path('depart/add/', depart.departAdd),
    path('depart/delete/', depart.departDelete),
    path('depart/<int:nid>/edit', depart.departEdit),

    path('member/list/', member.memberlist),
    path('member/add/', member.memberadd),
    path('member/<int:nid>/edit/', member.memberedit),
    path('member/<int:nid>/delete/', member.memberdelete),

    path('pretty/list/', pretty.pretty_list),
    path('pretty/add/', pretty.pretty_add),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),

    path('task/list/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('task/add/', task.task_add),

    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),
    path('order/edit/', order.order_edit),

    path('echarts/list/', echarts.echarts_edit),

    path('upload/list/', upload.upload_edit),
    path('upload/form/', upload.upload_form),
    path('upload/modelform/', upload.upload_modelform),

    path('city/list', city.city_list),
]
