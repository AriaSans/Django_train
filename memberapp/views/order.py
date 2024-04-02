import random
from datetime import datetime

from django import forms
from django.http import JsonResponse
from django.shortcuts import render, redirect

from memberapp import models
from memberapp.utils.pagination import Pagination
from memberapp.utils.form import MemberForm, PrettyForm, PrettyEditForm
from memberapp.utils.BootstrapModelForm import BootstrapModelForm
from django.views.decorators.csrf import csrf_exempt


class OrderForm(BootstrapModelForm):
    class Meta:
        model = models.Order
        exclude = ['oid', 'admin']


def order_list(request):
    form = OrderForm()

    orders = models.Order.objects.all().order_by('-id')
    page_obj = Pagination(request, orders)
    context = {
        'order_list': page_obj.queryset_list,
        'page_code': page_obj.html(),
        'form': form
    }
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    form = OrderForm(request.POST)
    form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
    if form.is_valid():
        form.instance.admin_id = request.session['info']['id']
        form.save()
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'errors': form.errors})


def order_delete(request):
    print(request.GET)
    models.Order.objects.filter(id=int(request.GET.get('q'))).delete()
    return JsonResponse({})


def order_detail(request):
    uid = request.GET.get('uid')
    data_dict = models.Order.objects.filter(id=uid).values('oid', 'title', 'price', 'status').first()
    return JsonResponse({'status': True, 'data': data_dict})


@csrf_exempt
def order_edit(request):
    uid = request.GET.get('uid')
    row_obj = models.Order.objects.filter(id=uid).first()
    if row_obj is None:
        print('no rowobj')
        return JsonResponse({'status': False})
    form = OrderForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'errors': form.errors})
