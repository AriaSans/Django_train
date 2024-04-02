from django.shortcuts import render, redirect

from memberapp import models
from memberapp.utils.pagination import Pagination
from memberapp.utils.form import MemberForm, PrettyForm, PrettyEditForm


def echarts_edit(request):
    return render(request, 'echarts_list.html')