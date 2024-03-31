from django.urls import path 
from .views import * 
app_name = 'workspace' 

urlpatterns = [
    path('', all, name='all'),
    path('<uuid:id>/', workspace_details, name='workspace-details'), 
    path('<uuid:workspace_id>/<int:website_id>/', website_details, name='website-details'), 
    path('pages/<int:website_id>/<int:page_id>/', page_details, name='page-details'), 
    path('workspace/delete/<uuid:workspace_id>/', delete_workspace, name='delete_workspace'),
    path('website/delete/<int:website_id>/', delete_website, name='delete_website'),
    path('websitepage/delete/<int:page_id>/', delete_website_page, name='delete_website_page'), 

    path('workspace/databases/create/<uuid:workspace_id>/', create_database, name='create-database')
]
