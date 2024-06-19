from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import loader  

# Create your views here.
def hello(request):
    #return HttpResponse("hello world")
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    return HttpResponse(html)    # rendering the template in HttpResponse  

def index(request):
    template = loader.get_template('index.html') # getting our template  

    # return HttpResponse(template.render())       # rendering the template in HttpResponse 
    
    name = {  
        'student':'prachi'  
    }  
    return HttpResponse(template.render(name))   

def members(request):
    mymembers = {'name':'prachi','id':'1'}
    template = loader.get_template('members.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'], 
  }
  return HttpResponse(template.render(context, request))  


from myapp.form import studentForm 
  
def studentindex(request):  
    stu = studentForm()  
    return render(request,"studentindex.html",{'form':stu})  