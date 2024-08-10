from django.db import models

class Listofproducts(models.Model):
    name_product = models.CharField(max_length=50, blank=False, verbose_name='продукт')
    calories = models.FloatField(default=0, verbose_name='калории')
    fats = models.FloatField(default=0, verbose_name='жиры')
    protein = models.FloatField(default=0, verbose_name='белок')
    carbohydrates = models.FloatField(default=0, verbose_name='углеводы')
    cholesterol = models.FloatField(default=0, verbose_name='холестирин')
    rubric = models.ForeignKey('ViewProduct', null=True, on_delete=models.PROTECT, verbose_name='Вид продукта')

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name_product']



class ViewProduct(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='продукт')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'вид продукта'
        verbose_name_plural = 'виды продуктов'
        ordering = ['name']