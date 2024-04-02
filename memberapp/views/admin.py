from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django import forms

from memberapp import models
from memberapp.utils.pagination import Pagination
from memberapp.utils.BootstrapModelForm import BootstrapModelForm
from memberapp.utils.encrypt import md5
from memberapp.utils.form import MemberForm, PrettyForm, PrettyEditForm


def admin_list(request):
    search_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        search_dict['name__contains'] = search_data

    queryset = models.Admin.objects.filter(**search_dict)
    page_obj = Pagination(request, queryset)
    context = {
        'admin_list': page_obj.queryset_list,
        'page_code': page_obj.html(),
        'search_data': search_data,
    }
    return render(request, 'admin_list.html', context)


class AdminForm(BootstrapModelForm):
    confirm_pwd = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta:
        model = models.Admin
        fields = ['name', 'pwd', 'confirm_pwd']
        widgets = {
            'pwd': forms.PasswordInput(render_value=True)
        }

    def clean_pwd(self):
        pwd = self.cleaned_data['pwd']
        return md5(pwd)

    def clean_confirm_pwd(self):
        confirm_pwd = md5(self.cleaned_data['confirm_pwd'])
        pwd = self.cleaned_data['pwd']
        if confirm_pwd != pwd:
            raise ValidationError("两次密码不一致")
        return confirm_pwd

def admin_add(request):
    if request.method == 'GET':
        form = AdminForm()
        context = {
            'title_name': "新增管理员",
            'form': form,
        }
        return render(request, 'changes.html', context)

    form = AdminForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    context = {
        'title_name': "新增管理员",
        'form': form,
    }
    return render(request, 'changes.html', context)
