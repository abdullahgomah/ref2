from django.shortcuts import render
from .forms import CreateDatabaseFieldForm
from .models import * 
from django.http import HttpResponseRedirect 
from django.contrib import messages


# Create your views here.
def create_db_field(request, db_id):
    try: 
        db = Database.objects.get(id=db_id)
    except: 
        return render('workspace:all') 
    form = CreateDatabaseFieldForm() 
    if request.POST: 
        form = CreateDatabaseFieldForm(request.POST)
        if form.is_valid(): 
            form.instance.db = db 
            form.save() 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



"""
must be a check if the user owns the db or not
"""
def delete_db_field(request, field_id):
    field = DatabaseField.objects.get(id=field_id) 
    field.delete() 
    messages.add_message(request, messages.SUCCESS, message="تم الحذف بنجاح")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

