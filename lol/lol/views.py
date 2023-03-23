from django.http import HttpResponse
from django.shortcuts import render

def about(r):
    return render(r,'about.html')
def aboutus(r,id):
    return HttpResponse(id)
def contact(r):
   
  
    try:
        if r.method=="post":
            name=r.POST['name']
            email=r.POST['email']
            message=r.POST['message']
           
    except:
        pass
    if r.method=="GET":
        return render(r,'contact.html',{'ad':"send message",'ty':"submit"})
    return render(r,'contact.html',{'ad':"thanks for contacing us",'ty':"text"})
def index(r):
    data={
        'title':'Home page',
        'list':['python','c++','java'],
        'dic':[
        {'name':'rav','phone':'4554'},
        {'name':'anuj','phone':'7854'},

        ]
    }
    return render(r,'index.html',data)