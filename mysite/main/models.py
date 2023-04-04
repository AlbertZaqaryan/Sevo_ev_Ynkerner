from django.db import models

# Create your models here.


class SliderActive(models.Model):

    name1 = models.CharField('SliderActive name1', max_length=60)
    name2 = models.CharField('SliderActive name2', max_length=60)
    text = models.TextField('SliderActive text')
    img = models.ImageField('SliderActive image', upload_to='images')
    logo = models.ImageField('SliderActive logo', upload_to='images')

    def __str__(self):
        return self.name1
    
class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categ')
    name = models.CharField('SubCategory name', max_length=60)
    price = models.PositiveIntegerField('SubCategory price')
    img = models.ImageField('SubCategory image', upload_to='images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
