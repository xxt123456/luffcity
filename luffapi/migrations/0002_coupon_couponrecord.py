# Generated by Django 2.1.1 on 2019-07-18 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('luffapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='活动名称')),
                ('brief', models.TextField(blank=True, null=True, verbose_name='优惠券介绍')),
                ('coupon_type', models.SmallIntegerField(choices=[(0, '通用券'), (1, '满减券'), (2, '折扣券')], default=0, verbose_name='券类型')),
                ('money_equivalent_value', models.IntegerField(verbose_name='等值货币')),
                ('off_percent', models.PositiveSmallIntegerField(blank=True, help_text='只针对折扣券，例7.9折，写79', null=True, verbose_name='折扣百分比')),
                ('minimum_consume', models.PositiveIntegerField(default=0, help_text='仅在满减券时填写此字段', verbose_name='最低消费')),
                ('object_id', models.PositiveIntegerField(blank=True, help_text='可以把优惠券跟课程绑定', null=True, verbose_name='绑定课程')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='数量(张)')),
                ('open_date', models.DateField(verbose_name='优惠券领取开始时间')),
                ('close_date', models.DateField(verbose_name='优惠券领取结束时间')),
                ('valid_begin_date', models.DateField(blank=True, null=True, verbose_name='有效期开始时间')),
                ('valid_end_date', models.DateField(blank=True, null=True, verbose_name='有效结束时间')),
                ('coupon_valid_days', models.PositiveIntegerField(blank=True, help_text='自券被领时开始算起', null=True, verbose_name='优惠券有效期（天）')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': '31. 优惠券生成记录',
            },
        ),
        migrations.CreateModel(
            name='CouponRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=64, unique=True)),
                ('status', models.SmallIntegerField(choices=[(0, '未使用'), (1, '已使用'), (2, '已过期')], default=0)),
                ('get_time', models.DateTimeField(help_text='用户领取时间', verbose_name='领取时间')),
                ('used_time', models.DateTimeField(blank=True, null=True, verbose_name='使用时间')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luffapi.Account', verbose_name='拥有者')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luffapi.Coupon')),
            ],
            options={
                'verbose_name_plural': '32. 用户优惠券',
            },
        ),
    ]
