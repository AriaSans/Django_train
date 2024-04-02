from django.shortcuts import render, redirect

from memberapp import models
from memberapp.utils.pagination import Pagination
from memberapp.utils.form import MemberForm, PrettyForm, PrettyEditForm


# Create your views here.
def departList(request):
    if request.method == 'GET':
        departs_list = models.Department.objects.all()
        return render(request, 'departlist.html', {'departs_list': departs_list})


def departAdd(request):
    if request.method == 'GET':
        return render(request, 'departadd.html')

    name = request.POST.get('name')
    models.Department.objects.create(name=name)
    return redirect('/depart/list/')


def departDelete(request):
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()

    return redirect('/depart/list/')


def departEdit(request, nid):
    if request.method == 'GET':
        depart = models.Department.objects.filter(id=nid).first()
        return render(request, 'departedit.html', {"depart": depart})

    name = request.POST.get('name')
    models.Department.objects.filter(id=nid).update(name=name)
    return redirect('/depart/list/')
