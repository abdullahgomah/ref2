from django.contrib import admin
from .models import * 

# Register your models here.
class DatabaseAdmin(admin.ModelAdmin): 
    model = Database 
    list_filter = ('workspace', )
    

admin.site.register(Database, DatabaseAdmin) 


class DatabaseAttachmentAdmin(admin.ModelAdmin): 
    model = DatabaseAttachment 
    list_filter = ('db', )

admin.site.register(DatabaseAttachment, DatabaseAttachmentAdmin)

admin.site.register(DatabaseType)

class FieldTypeAdmin(admin.ModelAdmin): 
    model = FieldType 
    list_filter = ('db_type',) 

admin.site.register(FieldType, FieldTypeAdmin)


class PreBuiltFieldAdmin(admin.ModelAdmin): 
    model = PreBuiltField
    list_filter = ('department', 'db_type', 'field_type',)
admin.site.register(PreBuiltField, PreBuiltFieldAdmin)

admin.site.register(DatabaseField)

admin.site.register(PreBuiltFieldDepartment)