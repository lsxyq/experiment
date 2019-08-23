from django.db import models


# Create your models here.

class Customer(models.Model):
    CHOICE = (
        (1, '普通'),
        (2, '批发'),
        (3, 'VIP')
    )
    name = models.CharField('客户姓名', max_length=50)
    phone = models.CharField('客户电话', max_length=12)
    type = models.PositiveSmallIntegerField(default=1, choices=CHOICE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    company_code = models.CharField('公司码', max_length=20, blank=True, null=True)

    def __str__(self):
        return '%s-%s' % (self.name, self.phone)

    class Meta:
        permissions = (
            ("simulate_import_customer", "允许模拟导入客户"),
            ("import_customer", "允许导入客户至商家系统"),
        )
        verbose_name = "客户"
        verbose_name_plural = verbose_name


class CompanyUser(models.Model):
    is_taixiang_admin = models.BooleanField('是否运营人员', default=False)
    company_code = models.CharField('公司码', max_length=20, blank=True, default='')

    def __unicode__(self):
        return '%s' % self.company_code

    class Meta:
        verbose_name = '导入账号'
        verbose_name_plural = verbose_name
