from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# class Menu(models.Model):
class Menu(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    # parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    # def __str__(self):
    #     return self.title

    def __str__(self):  # __str__ method elaborated later in
        full_path = [self.title]  # post. use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Content(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    TYPE = (
        ('News', 'Haber'),
        ('Announce', 'Duyuru'),
        ('Decision', 'Karar'),
        ('Survey', 'Anket')
    )

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)  # relation with Menu table
    # detail = models.TextField()
    detail = RichTextUploadingField()
    type = models.CharField(max_length=10, choices=TYPE)
    # file ve videolink field eklenecek...
    slug = models.SlugField()
    # user field eklenecek...
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Imagen(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)  # relation with Content table
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
