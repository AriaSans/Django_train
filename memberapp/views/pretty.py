from django.shortcuts import render, redirect

from memberapp import models
from memberapp.utils.pagination import Pagination
from memberapp.utils.form import MemberForm, PrettyForm, PrettyEditForm


def pretty_list(request):
    # for i in range(300):
    #     models.PrettyNum.objects.create(mobile="18838828898")

    search_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        search_dict['mobile__contains'] = search_data

    # 分页功能
    queryset = models.PrettyNum.objects.filter(**search_dict).order_by('-level')
    paginator_object = Pagination(request, queryset)

    prtty_list = paginator_object.queryset_list
    page_code = paginator_object.html()

    context = {
        "pretty_list": prtty_list,
        "search_data": search_data,
        "page_code": page_code
    }
    return render(request, 'prtty_list.html', context)


def pretty_add(request):
    if request.method == 'GET':
        pretty_form = PrettyForm()
        return render(request, 'pretty_add.html', {"form": pretty_form})

    form_get = PrettyForm(data=request.POST)
    if form_get.is_valid():
        form_get.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_add.html', {"form": form_get})


def pretty_edit(request, nid):
    row_object = models.PrettyNum.objects.get(id=nid)
    form = PrettyEditForm(instance=row_object)
    if request.method == 'GET':
        return render(request, 'pretty_edit.html', {"form": form})

    form_get = PrettyEditForm(data=request.POST, instance=row_object)
    if form_get.is_valid():
        form_get.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_edit.html', {"form": form_get})


def pretty_delete(request, nid):
    models.PrettyNum.objects.get(id=nid).delete()
    return redirect('/pretty/list/')