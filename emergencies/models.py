from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


# class EmergencyImage(models.Model):
#     emergency = models.ForeignKey(Emergency, blank=True, null=True, default=None)
#     image = models.ImageField(upload_to='emergency_images')
#     is_active = models.BooleanField(default=True)
#     is_main = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#          return "%s" % self.id
#
#     class Meta:
#         verbose_name = 'Фотография'
#         verbose_name_plural = 'Фотографии'

class Emergency(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.ForeignKey(Status, blank=True, null=True, default=None)
    person_name=models.TextField(blank=True, null=True, default=None)
    phone=models.TextField(blank=True, null=True, default=None)
    # image = models.FileField(upload_to='', null=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Происшествие'
        verbose_name_plural = 'Происшествия'


class EmergencyImage(models.Model):
    emergency = models.ForeignKey(Emergency, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='emergency_images')
    is_active = models.BooleanField(default=False)
    is_main = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

