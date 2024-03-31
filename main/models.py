from django.db import models
from django.http import JsonResponse

from django.contrib.auth.models import AbstractUser



class Users(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    is_client = models.BooleanField(default=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='users')


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Categories(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True,)


    def __str__(self):
        return self.name

class Salesproduct(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    discount = models.CharField(max_length=20)
    Holat = models.CharField(max_length=30)
    total_weight = models.CharField(max_length=40)
    photo1 = models.ImageField(null=True, blank=True, upload_to='sales')
    photo2 = models.ImageField(null=True, blank=True,  upload_to='sales')
    photo3 = models.ImageField(null=True, blank=True, upload_to='sales')
    photo4 = models.ImageField(null=True, blank=True, upload_to='sales')

    def __str__(self):
        return self.name

class Blogs(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='blogs')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.author



class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    foiz = models.CharField(max_length=23, null=True, blank=True, default=' ')
    stasus = models.CharField(max_length=22,null=True, blank=True)
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    photo1 = models.ImageField(null=True, blank=True, upload_to='products')
    photo2 = models.ImageField(null=True, blank=True, upload_to='products')
    photo3 = models.ImageField(null=True, blank=True, upload_to='products')
    photo4 = models.ImageField(null=True, blank=True, upload_to='products')
    aksiya = models.BooleanField(default=False, null=True, blank=True)
    aksiy_price = models.DecimalField(max_digits=10, decimal_places=0,default='0',verbose_name=' Aksiya Narxni belgilang')
    def __str__(self):
        return self.name


class Banners(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='banners')

    def __str__(self):
        return self.title


class Shop(models.Model):
    client = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class ShopItem(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)


class Favourite(models.Model):
    client = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Favouriteitem(models.Model):
    fav = models.ForeignKey(Favourite, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


def CountSavatcha(request):
    count = ShopItem.objects.filter(shop__client=request.user, shop__status=0)
    s = 0
    for c in count:
        s += c.total

    data = {
        'count': count.count(),
        'total': s
    }

    return JsonResponse(data)


class UserPhone(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.user.first_name
