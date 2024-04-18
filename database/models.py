from django.db import models
from workspace.models import * 

## قاعدة بيانات فيها نوع الحقل والكود الخاص بيه 

class DatabaseType(models.Model):

    name = models.CharField(verbose_name="الاسم", max_length=200)

    class Meta:
        verbose_name = "نوع قاعدة بيانات"
        verbose_name_plural = "أنواع قواعد البيانات"

    def __str__(self):
        return self.name


class FieldType(models.Model): 
    db_type = models.ForeignKey(DatabaseType, verbose_name="نوع قاعدة البيانات", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="نوع الحقل", max_length=150)
    code = models.TextField(verbose_name="الكود")

    class Meta: 
        verbose_name = "نوع حقل مسبق"
        verbose_name_plural = "أنواع الحقول المسبقة"

    def __str__(self):
        return self.name 

class Database(models.Model):
    workspace = models.ForeignKey(Workspace, verbose_name="بيئة العمل", on_delete=models.CASCADE, related_name='databases')
    name = models.CharField(verbose_name="اسم قاعدة البيانات", max_length=150)
    db_type = models.ForeignKey(DatabaseType, on_delete=models.SET_NULL, null=True, blank=True) 
    
    class Meta:
        verbose_name = "قاعدة بيانات"
        verbose_name_plural = "قواعد البيانات"

    def __str__(self):
        return self.name


class DatabaseAttachment(models.Model):
    db = models.ForeignKey("Database", verbose_name="قاعدة البيانات", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="اسم المرفق ", max_length=150)
    description= models.TextField(verbose_name='وصف المرفق', null=True, blank=True)
    file = models.FileField(verbose_name="المرفق", upload_to="media/db/attachments/")


    class Meta:
        verbose_name = "مرفق"
        verbose_name_plural = "مرفقات قواعد البيانات"

    def __str__(self):
        return self.name




# pre built database fields 

class PreBuiltField(models.Model):
    department= models.ForeignKey("PreBuiltFieldDepartment", verbose_name="القسم", on_delete=models.SET_NULL, null=True, blank=True)
    db_type = models.ForeignKey(DatabaseType, on_delete=models.SET_NULL, null=True, blank=True) 
    field_type = models.ForeignKey(FieldType, on_delete=models.SET_NULL, null=True,blank=True) 
    
    name = models.CharField(verbose_name="اسم الحقل", max_length=255)
    description = models.TextField(verbose_name="وصف الحقل", null=True, blank=True)
    

    class Meta:
        verbose_name_plural = "معجم الحقول"
        verbose_name = "حقل مسبق"

    def __str__(self):
        return self.name


class PreBuiltFieldDepartment(models.Model):
    name =models.CharField(verbose_name="اسم القسم", max_length=250)
    

    class Meta:
        verbose_name = "قسم"
        verbose_name_plural = "اقسام الحقول المسبقة"

    def __str__(self):
        return self.name


class DatabaseField(models.Model):
    db = models.ForeignKey(Database, verbose_name="قاعدة البيانات", on_delete=models.CASCADE, related_name='fields')
    field_type = models.ForeignKey(FieldType, on_delete=models.SET_NULL, null=True,blank=True) 
    
    name = models.CharField(verbose_name="اسم الحقل", max_length=255)
    description = models.TextField(verbose_name="وصف الحقل", null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "حقول قواعد البيانات "
        verbose_name = "حقل"

    def __str__(self):
        return self.name


