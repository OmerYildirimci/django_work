from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name='Kategori ismi')
    slug = models.SlugField(max_length=20)
    def __str__(self):
        return self.name
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="article")
    category = models.ForeignKey(Category,models.DO_NOTHING)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.title