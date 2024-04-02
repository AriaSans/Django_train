from django.shortcuts import render, redirect

from memberapp import models
from memberapp.utils.pagination import Pagination
from memberapp.utils.form import MemberForm, PrettyForm, PrettyEditForm


def memberlist(request):
    member_list = models.Member.objects.all()
    pagination_obj = Pagination(request, member_list)

    context = {
        'member_list': pagination_obj.queryset_list,
        'page_code': pagination_obj.html(),
    }

    return render(request, 'memberlist.html', context)


def memberadd(request):
    if request.method == 'GET':
        form = MemberForm()
        return render(request, 'memberadd.html', {"form": form})

    form = MemberForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/member/list/')

    return render(request, 'memberadd.html', {"form": form})


def memberedit(request, nid):
    row_obj = models.Member.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = MemberForm(instance=row_obj)
        return render(request, 'memberedit.html', {'form': form})

    form = MemberForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/member/list/')

    return render(request, 'memberedit.html', {"form": form})


def memberdelete(request, nid):
    models.Member.objects.filter(id=nid).delete()
    return redirect('/member/list/')