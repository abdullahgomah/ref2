import uuid 
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Workspace(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name='اسم بيئة العمل')
    date_created = models.DateTimeField(auto_now_add=True) 
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        return self.name 
    

    def save(self, *args, **kwargs):
       if not self.slug: 
           self.slug = slugify(self.name, allow_unicode=True) 
       super(Workspace, self).save(*args, **kwargs) # Call the real save() method

    class Meta:
        verbose_name = 'بيئة عمل'
        verbose_name_plural = 'بيئات العمل'
    

class Website(models.Model):
    workspace = models.ForeignKey(Workspace, related_name='websites', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=250, verbose_name='اسم الموقع') 
    ui = models.FileField(upload_to='files/', verbose_name="ملفات واجهة المستخدم", blank=True, null=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'موقع'
        verbose_name_plural = 'المواقع'

class WebsitePage(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, verbose_name='الموقع', related_name='pages')
    name = models.CharField(max_length=250, verbose_name='اسم الصفحة') 
    code = models.TextField(verbose_name="الكود", blank=True, null=True) 

    def __str__(self):
        return self.name 

    class Meta: 
        verbose_name = 'صفحة موقع'
        verbose_name_plural = 'صفحات المواقع'



