from django import forms

from memberapp import models

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class MemberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = ['name', 'phone', 'pwd', 'age', 'account', 'create_time', 'depart', 'gender']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "depart" or name == "gender":
                field.widget.attrs = {"class": "form-select"}
                continue
            if name == "create_time":
                field.widget.attrs = {"class": "form-control", "autocomplete": "off"}
                continue
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class PrettyForm(forms.ModelForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号格式错误", "错误信息2")],
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "level" or name == "status":
                field.widget.attrs = {"class": "form-select"}
                continue
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()

        if exists:
            # 验证不通过
            raise ValidationError("号码已存在")

        # 验证通过
        return txt_mobile


class PrettyEditForm(forms.ModelForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号格式错误", "错误信息2")],
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == "level" or name == "status":
                field.widget.attrs = {"class": "form-select"}
                continue
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        txt_id = self.instance.pk

        exists = models.PrettyNum.objects.exclude(id=txt_id).filter(mobile=txt_mobile).exists()

        if exists:
            # 验证不通过
            raise ValidationError("号码已存在")

        # 验证通过
        return txt_mobile
