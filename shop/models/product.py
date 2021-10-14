from django.db import models
from shop.models.category import Category
 
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    descripton = models.CharField(max_length=255, default='', blank=True, null=True)
    image = models.ImageField(upload_to = 'upload/product')

    def __str__(self):
        return self.name


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all__products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by__category(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all__products()