from django.db import models
from django.urls import reverse


class Menu(models.Model):
    menu_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('menu', kwargs={'menu_slug': self.slug})

    def __str__(self):
        return self.menu_name

    class Meta:
        verbose_name_plural = "Menu"


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='categories',
                             null=True, blank=True, verbose_name="Category by menu")
    subcategory = models.ForeignKey("self", on_delete=models.CASCADE, null=True,
                                    related_name='subcategories', blank=True, verbose_name="Subcategory by category")
    which_cat = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='which_menu_cat',
                             null=True, blank=True, verbose_name="In which menu")

    def __str__(self):
        return f"{self.category_name}"

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug, 'menu_slug': self.which_cat.slug})

    class Meta:
        verbose_name_plural = "Categories"


