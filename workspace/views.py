from django.shortcuts import render, redirect, get_object_or_404
from .models import * 
from .forms import * 
from django.http import HttpResponseRedirect 

# Create your views here.

def all(request): 
    workspaces = Workspace.objects.all() 
    form = CreateWorkspaceForm() 

    if request.POST: 
        form = CreateWorkspaceForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('workspace:all')
    
    context= {
        'form': form, 
        'workspaces': workspaces
    } 

    return render(request, 'workspace/all.html', context)



def workspace_details(request, id): 
    workspcae = get_object_or_404(Workspace, id=id)

    create_db_form = CreateDatabaseForm()  

    form = CreateWebsiteForm() 

    if request.POST:
        form = CreateWebsiteForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.instance.workspace = workspcae 
            form.save() 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    
    context = {
        'workspace': workspcae,
        'form': form, 
        'create_db_form': create_db_form
    } 
    return render(request, 'workspace/workspace-details.html', context)


def website_details(request, workspace_id, website_id): 
    website = Workspace.objects.get(id=workspace_id).websites.get(id=website_id) 

    form = CreateWebsitePageForm() 

    if request.POST: 
        form = CreateWebsitePageForm(request.POST) 
        if form.is_valid(): 
            form.instance.website = website 
            form.save()  
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


    context = {
        'website': website, 
        'form': form, 
    }

    return render(request, 'workspace/website_details.html', context)


def page_details(request, website_id, page_id): 

    page = Website.objects.get(id=website_id).pages.get(id=page_id) 
    

    context ={
        'page': page, 
    }
    return render(request, 'workspace/page-details.html', context)



def delete_workspace(request, workspace_id):
    workspace = get_object_or_404(Workspace, pk=workspace_id)
    workspace.delete()
    return redirect('workspace:all') 

def delete_website(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    workspace_id = website.workspace.id 
    website.delete()
    return redirect('workspace:workspace-details', id=workspace_id)  

def delete_website_page(request, page_id):
    page = get_object_or_404(WebsitePage, id=page_id)
    website_id = page.website.id 
    workspace_id = page.website.workspace.id 
    page.delete()
    return redirect('workspace:website-details', website_id=website_id, workspace_id=workspace_id)  


def create_database(request, workspace_id): 
    workspace = get_object_or_404(Workspace, id=workspace_id)

    if request.POST: 
        form = CreateDatabaseForm(request.POST) 
        if form.is_valid(): 
            form.instance.workspace = workspace 
            form.save() 
            return redirect('workspace:workspace-details', id=workspace_id)


def database_details(request, db_id): 
    db = get_object_or_404(Database, id=db_id) 

    context = {
        'db': db,
    }

    return render(request, 'workspace/database-details.html', context)