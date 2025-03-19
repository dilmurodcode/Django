from django.db import models

# Create your models here.
class Customers(models.Model):
    full_name = models.CharField("to'liq ismi", max_length=255)
    position = models.CharField("lavozimi", max_length=255)
    image = models.ImageField("rasmi", upload_to='customers/')
    deascription = models.TextField("tafsif")

    class Meta:
        verbose_name = "mijozlar"
        verbose_name_plural = "mijozlar"


    def __str__(self):
        return self.full_name


class Partner(models.Model):
    image = models.ImageField("rasmi")
    url = models.CharField("urli", max_length=255)
    order = models.IntegerField("tartibi", default=0)

    class Meta:
        verbose_name = "hamkorlar"
        verbose_name_plural = "hamkorlar"


class Application(models.Model):
    class StatusChoice(models.TextChoices):
         MAIN_PAGE= 'main_page', 'MAIN_PAGE'
         SERVICE= 'service', 'SERVICE'
         GET_TT= 'get_tt', 'GET_TT'
         PARTNER = 'partner', 'PARTNER'
         ORDER = 'order', 'ORDER'

    class Meta:
        verbose_name = "hamkorlar"
        verbose_name_plural = "hamkorlar"

    full_name = models.CharField("to'liq ismi", max_length=255)
    phone = models.CharField("nomeri", max_length=255)
    description = models.TextField("tafsif", max_length=255, null=True, blank=True)
    product = models.CharField("product nomi",max_length=255, null=True, blank=True)
    status = models.CharField("holati", max_length=255, choices=StatusChoice.choices,default=StatusChoice.MAIN_PAGE)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    title = models.CharField("sarlavha", max_length=255)
    status = models.CharField("holat", max_length=255)
    order = models.IntegerField("tartibi",default=0)
    image = models.ImageField("rasmi")
    description = models.TextField("tafsif", max_length=255, null=True, blank=True)
    brand = models.CharField('brendi', max_length=255)
    country = models.CharField("mamlakati", max_length=255)
    guarantee = models.CharField("kafaloti", max_length=255)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products',
        null=True
    )
    is_main_page = models.BooleanField("bosh sahifa", max_length=255)


class ProductImage(models.Model):
    image = models.ImageField("rasmi",)
    product = models.ForeignKey(
        Product, related_name='product', on_delete=models.CASCADE
    )


class ProductCharacteristic(models.Model):
    key = models.CharField("kalit", max_length=255)
    value = models.CharField("valeusi",max_length=255)
    order = models.IntegerField("tartibi",default=0)
    product = models.ForeignKey(
        Product, related_name='product_characteristic', on_delete=models.CASCADE
    )

class Category(models.Model):
    name = models.CharField("ismi",max_length=255)
    icon = models.ImageField('iconi',)
    order = models.IntegerField('tartibi',default=0)

class News(models.Model):
    title = models.CharField("sarlavha", max_length=255)
    description = models.TextField("tafsif", max_length=255, null=True, blank=True)
    image = models.ImageField("rasmi")
    date = models.DateField("vaqti",)
    body = models.TextField("yomonliklari", max_length=255)