from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

#
# class Category(MPTTModel):
#     title = models.CharField(max_length=50, unique=True, verbose_name='Название')
#     parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
#                             db_index=True, verbose_name='Родительская категория')
#     slug = models.SlugField()
#
#     class MPTTMeta:
#         order_insertion_by = ['title']
#
#     class Meta:
#         unique_together = [['parent', 'slug']]
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def get_absolute_url(self):
#         return reverse('post-by-category', args=[str(self.slug)])
#
#     def __str__(self):
#         return self.title
