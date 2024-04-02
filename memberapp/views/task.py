import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from memberapp import models
from memberapp.utils.pagination import Pagination
from memberapp.utils.BootstrapModelForm import BootstrapModelForm


class TaskForm(BootstrapModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'


def task_list(request):
    form = TaskForm()
    if request.method == 'GET':
        return render(request, 'task_list.html', {"form": form})


@csrf_exempt
def task_ajax(request):
    print(request.POST)
    data_dict = {'status': True, 'data': [1, 1, 2, 2]}
    return HttpResponse(json.dumps(request.POST))
    # 或者return JsonResponse(dict)


@csrf_exempt
def task_add(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        data_dict = {'status': True}
    else:
        data_dict = {'status': False, 'error': form.errors}

    return HttpResponse(json.dumps(data_dict))
