from django.db import models


# Create your models here.

class Admin(models.Model):
    name = models.CharField(verbose_name="账号", max_length=32)
    pwd = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(verbose_name="部门名", max_length=16)

    def __str__(self):
        return self.name


class Member(models.Model):
    gender_list = (
        (1, "男"),
        (2, "女")
    )

    name = models.CharField(verbose_name="名字", max_length=16)
    phone = models.CharField(verbose_name="手机号", max_length=32)
    pwd = models.CharField(verbose_name="密码", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间", null=True, blank=True)

    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", null=True, blank=True,
                               on_delete=models.SET_NULL)
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_list)


class PrettyNum(models.Model):
    """ 靓号表 """
    level_choices = (
        (1, "一级"),
        (2, "二级"),
        (3, "三级"),
        (4, "四级"),
    )

    status_choices = {
        (1, "已占用"),
        (2, "未使用"),
    }

    mobile = models.CharField(verbose_name="号码", max_length=11)
    price = models.IntegerField(verbose_name="价格", default=0)
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=2)


class Task(models.Model):
    level_choices = (
        (1, '紧急'),
        (2, '重要'),
        (3, '临时'),
    )

    level = models.SmallIntegerField(verbose_name="等级", choices=level_choices, default=3)
    title = models.CharField(verbose_name="标题", max_length=64)
    details = models.TextField(verbose_name="详细信息")
    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)


class Order(models.Model):
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=64)
    price = models.IntegerField(verbose_name="价格", default=0)

    status_choices = (
        (1, '待支付'),
        (2, '已支付'),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    admin = models.ForeignKey(verbose_name="管理员", to="Admin", on_delete=models.CASCADE)


class Userdata(models.Model):
    name = models.CharField(verbose_name="昵称", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    avatar = models.CharField(verbose_name="头像", max_length=128)


class City(models.Model):
    name = models.CharField(verbose_name="名称", max_length=32)
    count = models.IntegerField(verbose_name="人口")

    # 本质上数据库上也是CharField，自动保存数据。
    img = models.FileField(verbose_name="logo", max_length=128, upload_to='city/')
    # upload_to='city/' : 文件保存到 'media/city/' 目录下
