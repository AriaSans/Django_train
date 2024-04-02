import json
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from memberapp import models
from memberapp.utils.pagination import Pagination
from memberapp.utils.BootstrapModelForm import BootstrapModelForm


class CityModelForm(BootstrapModelForm):
    class Meta:
        model = models.City
        fields = '__all__'


def city_list(request):
    if request.method == 'GET':
        queryset = models.City.objects.all()
        form = CityModelForm()
        page_obj = Pagination(request, queryset, page_size=5)
        context = {
            'form': form,
            'city_list': page_obj.queryset_list,
            'page_code': page_obj.html(),
        }
        return render(request, 'city_list.html', context)
