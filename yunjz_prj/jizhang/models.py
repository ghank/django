#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
# 分类
class Category(models.Model):
    INCOME_CHOICES = (
        (True, u'收入'),
        (False, u'支出'),
    )
    #related_name：The name to use for the relation from the related object back to this one.
    #p_category相当于models.Model的子类
    p_category = models.ForeignKey('self', null=True, blank=True, verbose_name=u"父类名称", related_name='childs')
    name = models.CharField(max_length=20, verbose_name=u"类别名称")
    isIncome = models.BooleanField(choices=INCOME_CHOICES, verbose_name=u"是否收入")
    # User的外键
    user = models.ForeignKey(User, verbose_name=u"所属用户")

    def __unicode__(self):
        return self.level()+self.name

    def get_absolute_url(self):
        return '%s' % (reverse('jizhang:edit_category', args=(self.id,)))

    def get_items_url(self):
        return '%s' % (reverse('jizhang:show_category', args=(self.id, )))

    def level(self):
        if self.p_category:
            return "+"+self.p_category.level()
        else:
            return ""

    #save()函数，django会根据模型的主键，更新或插入数据到数据库里
    def save(self, *args, **kwargs):
        #form保证了子类不能修改isIncome，只能修改顶级父类的isIncome
        #遍历一遍childs，统一设置isIncome
        for child in self.childs.all():
            if child.isIncome != self.isIncome:
                child.isIncome = self.isIncome
                child.save()

        super(self.__class__, self).save(*args, **kwargs)

# 收支
class Item(models.Model):
    #价格
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name=u'金额')
    #备注
    comment = models.CharField(max_length=200, blank = True, verbose_name=u'注释')
    #日期
    pub_date = models.DateField(verbose_name=u'日期')
    #分类 收支的外键
    category = models.ForeignKey(Category,verbose_name=u'分类', related_name='items')

    #排序
    class Meta:
        ordering = ["-pub_date"]

    def __unicode__(self):
        return str(self.price)

    def get_absolute_url(self):
        return '%s' % (reverse('jizhang:edit_item', args=(self.id,)))

    def get_price(self):
        if self.category.isIncome:
            return self.price
        else:
            return -1*self.price

    #录入数据库
    def save(self, *args, **kwargs):
        if self.price<0:
            self.price = -1*self.price
        super(self.__class__, self).save(*args, **kwargs)
