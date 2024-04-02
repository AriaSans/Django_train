import os

from django import forms
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings

from memberapp import models
from memberapp.utils.pagination import Pagination
from memberapp.utils.BootstrapModelForm import BootstrapForm, BootstrapModelForm
from django.views.decorators.csrf import csrf_exempt


class UploadForm(BootstrapForm):
    bootstrap_exclude_fields = ['avatar']

    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='age')
    avatar = forms.FileField(label='avatar')


class UploadModelForm(BootstrapModelForm):
    class Meta:
        model = models.City
        fields = '__all__'


def upload_edit(request):
    if request.method == 'GET':
        return render(request, 'upload_list.html')

    print(request.POST)
    print(request.FILES)

    file_obj = request.FILES.get('avatar')
    f = open(file_obj.name, mode='wb')
    for chunk in file_obj.chunks():
        f.write(chunk)
    f.close()

    return HttpResponse('ggg')


def upload_form(request):
    form = UploadForm()
    if request.method == 'GET':
        return render(request, 'upload_form.html', {'form': form})

    form = UploadForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        avatar_obj = form.cleaned_data.get('avatar')
        name = form.cleaned_data.get('name')
        age = form.cleaned_data.get('age')

        media_path = os.path.join('media', avatar_obj.name)

        # 文件存放
        f = open(media_path, mode='wb')
        for chunk in avatar_obj.chunks():
            f.write(chunk)
        f.close()

        # 数据库操作
        models.Userdata.objects.create(name=name, age=age, avatar=media_path)

        return HttpResponse('上传成功')

    return render(request, 'upload_form.html', {'form': form, 'errors': form.errors})


@csrf_exempt
def upload_modelform(request):
    print(request.FILES)
    print(request.POST)
    form = UploadModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'errors': form.errors})
