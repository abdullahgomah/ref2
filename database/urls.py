from django.urls import path 
from .views import * 

app_name = 'database' 

urlpatterns = [
    path('create_db_field/<int:db_id>/', create_db_field, name='create-db-field'), 
    path('del_field/<int:field_id>/', delete_db_field, name='del-db-field'),
]
