# Generated by Django 4.1 on 2024-03-27 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberapp', '0003_member_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='号码')),
                ('price', models.IntegerField(default=0, verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[(1, '一级'), (2, '二级'), (3, '三级'), (4, '四级')], default=1, verbose_name='级别')),
                ('status', models.SmallIntegerField(choices=[(2, '未使用'), (1, '已占用')], default=2, verbose_name='状态')),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别'),
        ),
    ]