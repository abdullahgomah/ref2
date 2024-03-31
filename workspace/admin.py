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