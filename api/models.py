from django.db import models
import django.utils.timezone as timezone


ATTR_CHOICES = (
    (0, '收入'),
    (1, '支出'),
)

TYPE_CHOICE = (
    ('Y', '年度预算'),
    ('M', '月度预算'),
)


class User(models.Model):
    """
    用户表
    """
    nickname = models.CharField(verbose_name='昵称', max_length=50, default='')
    level = models.IntegerField(verbose_name='会员等级', default=0)
    mobile = models.CharField(verbose_name='手机', max_length=16, unique=True)
    email = models.EmailField(verbose_name='邮箱', max_length=50, unique=True)
    integral = models.IntegerField(verbose_name='积分', default=0)
    keep_date = models.IntegerField(verbose_name='记账天数', default=0)
    username = models.CharField(verbose_name='账号', max_length=50, unique=True)
    password = models.CharField(verbose_name='密码', max_length=100)
    last_date = models.DateTimeField(verbose_name='最后登录时间', auto_now=True)
    token = models.CharField(verbose_name='登录凭证', max_length=100, default='')
    icon = models.ImageField(verbose_name='头像', upload_to='image/%Y/%m', height_field='icon_height',
                             width_field='icon_width', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Category1(models.Model):
    """
    一级分类
    """

    name = models.CharField(verbose_name='分类名称', max_length=100, unique=True)
    attr = models.IntegerField(verbose_name='分类属性', choices=ATTR_CHOICES, default=1)
    fast_code = models.CharField(verbose_name='快速代码', max_length=10, default='', blank=True)
    icon = models.ImageField(verbose_name='图标', upload_to='image/%Y/%m', blank=True, null=True)
    # icon = models.ImageField(verbose_name='图标', upload_to='image/%Y/%m', blank=True)
    ordering = models.IntegerField(verbose_name='排序', default=0, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '一级分类'
        verbose_name_plural = '一级分类'
        ordering = ['-ordering', 'name']


class Category2(models.Model):
    """
    二级分类
    """
    name = models.CharField(verbose_name='分类名称', max_length=100, unique=True)
    # attr = models.IntegerField(verbose_name='分类属性', choices=ATTR_CHOICES, default=1)
    fast_code = models.CharField(verbose_name='快速代码', max_length=10, default='', blank=True)
    parent = models.ForeignKey('Category1', verbose_name='上级分类', on_delete=models.CASCADE, related_name='c2')
    icon = models.ImageField(verbose_name='图标', upload_to='image/%Y/%m', blank=True, null=True)
    # icon = models.ImageField(verbose_name='图标', upload_to='image/%Y/%m', blank=True)
    ordering = models.IntegerField(verbose_name='排序', default=0, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '二级分类'
        verbose_name_plural = '二级分类'
        ordering = ['-ordering', 'name']


class WasteBook(models.Model):
    """
    记账流水
    """
    account_date = models.DateTimeField(verbose_name='记账日期', default=timezone.now)
    # user = models.ForeignKey('User', verbose_name='用户id', on_delete=models.CASCADE)
    category1 = models.ForeignKey('Category1', verbose_name='一级分类', on_delete=models.CASCADE)
    category2 = models.ForeignKey('Category2', verbose_name='二级分类', on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name='金额', max_digits=10, decimal_places=2)
    remark = models.CharField(verbose_name='备注', max_length=500, default='', blank=True)

    def __str__(self):
        return '{0}.{1}.{2}'.format(self.account_date, self.category1, self.category2)

    class Meta:
        verbose_name = '流水'
        verbose_name_plural = '流水'
        # ordering = ['-account_date', 'user']
        ordering = ['-account_date']


class Budget(models.Model):
    """
    预算
    """
    # user = models.ForeignKey('User', verbose_name='用户id', related_name='budgets', on_delete=models.CASCADE)
    budget_type = models.CharField(verbose_name='预算类型', max_length=2, choices=TYPE_CHOICE, default='Y')
    amount = models.DecimalField(verbose_name='金额', max_digits=10, decimal_places=2)
    remark = models.CharField(verbose_name='备注', max_length=500, default=0, blank=True)

    def __str__(self):
        return self.budget_type

    class Meta:
        verbose_name = '预算'
        verbose_name_plural = '预算'
        # ordering = ['user', 'budget_type']
        ordering = ['budget_type']


class Config(models.Model):
    """
    用户设置
    """
    user = models.ForeignKey('auth.User', verbose_name='用户', on_delete=models.CASCADE)
    key = models.CharField(verbose_name='配置项', max_length=20)
    value = models.CharField(verbose_name='配置值', max_length=100)
    remark = models.CharField(verbose_name='备注', max_length=500, default='', blank=True)

    def __str__(self):
        return '{0}.{1}'.format(self.user, self.key)

    class Meta:
        verbose_name = '用户设置'
        verbose_name_plural = '用户设置'
        ordering = ['user', 'key']
