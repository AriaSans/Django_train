from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django import forms

from memberapp import models
from memberapp.utils.pagination import Pagination
from memberapp.utils.BootstrapModelForm import BootstrapModelForm, BootstrapForm
from memberapp.utils.encrypt import md5
from memberapp.utils.form import MemberForm, PrettyForm, PrettyEditForm


class LoginForm(BootstrapForm):
    name = forms.CharField(label='账号', widget=forms.TextInput())
    pwd = forms.CharField(label='账号', widget=forms.PasswordInput())

    def clean_pwd(self):
        return md5(self.cleaned_data['pwd'])


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(request.POST)
    if form.is_valid():
        user_obj = models.Admin.objects.filter(**form.cleaned_data).first()
        if user_obj:
            print("查找成功")
            request.session['info'] = {'id': user_obj.id, 'name': user_obj.name}
            return redirect('/admin/list')
        print("查找失败")
        form.add_error('name', '用户名或密码错误')
    return render(request, 'login.html', {'form': form})


def logout(request):
    request.session.clear()
    return redirect('/login/')
