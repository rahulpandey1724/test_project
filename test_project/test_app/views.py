from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import table
from .forms import tableform

projectList = [
    {'id' : '1',
     'title' : 'Ecommerce Website',
     'Description': 'A functioning website'},

     {'id' : '2',
     'title' : 'Social Website',
     'Description': 'A functioning website'},

     {'id' : '3',
     'title' : 'Food Website',
     'Description': 'A functioning website'},
]

def home(request):
    projects = table.objects.all()
    content = {'work' : projects}
    return render(request, "test_app/templates1.html", content)

def user(request, pk):
    projectobj = table.objects.get(id = pk)
    tags = projectobj.tags.all()
    
    return render(request, 'test_app/templates2.html', {'project' : projectobj, 'tags' : tags})

def createproject(request):
    form = tableform()

    if request.method == 'POST':
        form = tableform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('first')
    content = {'page' : form}
    return render(request, "test_app/form.html", content)