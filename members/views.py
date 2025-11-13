from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values() # we use this to get all the data
    template = loader.get_template('all_members.html') #we then travel to this particular site
    context = { 
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    mymember = Member.objects.get(id=id) # to gain 1 specific member id
    template = loader.get_template('details.html') # this is where we would like to load our own html file.
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
    'firstname': 'Linus',
    }
    return HttpResponse(template.render(context,request))
