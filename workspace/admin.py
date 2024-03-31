from django.contrib import admin

from .models import * 
# Register your models here.


class WorkspaceAdmin(admin.ModelAdmin): 
    model = Workspace 
    search_fields = ('name',) 
    list_filter = ('date_created', )

admin.site.register(Workspace, WorkspaceAdmin)

admin.site.register(Website)


class WebsitePageAdmin(admin.ModelAdmin): 
    model = WebsitePage 
    list_filter = ('website', )

admin.site.register(WebsitePage, WebsitePageAdmin)


class DatabaseAdmin(admin.ModelAdmin): 
    model = Database 
    list_filter = ('workspace', )
    

admin.site.register(Database, DatabaseAdmin) 


class DatabaseAttachmentAdmin(admin.ModelAdmin): 
    model = DatabaseAttachment 
    list_filter = ('db', )

admin.site.register(DatabaseAttachment, DatabaseAttachmentAdmin)

class WebsiteAdmin(admin.AdminSite): 
    site_title = "بالإشارة"
    index_title = "بالإشارة"

admin.AdminSite.site_title = "بالإشارة"
admin.AdminSite.index_title = "لوحة الإدارة"
admin.AdminSite.site_header = "بالإشارة"