from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import user
from .quiz import fun_quiz
from service.models import service
from abcon.models import about_fun
def about(r):
    data_obj=about_fun.objects.all().order_by('title')#this create a object of all file and sorted by title fied
    if r.method=="GET":
        st=r.GET.get('search')
        if st!=None:
            data_obj=about_fun.objects.filter(title__icontains=st)
    data={
        'data':data_obj
    }
    return render(r,'about.html',data)
def aboutus(r,id):
    return HttpResponse(id)
def contact(r):
   
  
    try:
        if r.method=="POST":
            name=r.POST.get('name')
            email=r.POST.get('email')
            message=r.POST.get('message')
            en=service(name=name,email=email,message=message)
            en.save()
            return render(r,'contact.html',{'ad':"thanks for contacing us",'ty':"text"}) 
           
    except:
        pass

    return render(r,'contact.html',{'ad':"send message",'ty':"submit"})
    #this statment will change the contents of submit button after clicking in it
    # return redirect("/about/") #this will redirect to about page.
def index(r):
    table_data=service.objects.all()
    
    data={
        'title':'Home page',
        'list':['python','c++','java'],
        'dic':[
        {'name':'rav','phone':'4554'},
        {'name':'anuj','phone':'7854'},
        ],
        'tdata':table_data,
    }
  
    return render(r,'index.html',data)
# def calculator(r):
#     c=0
#     cl=user()
#     data={
#         'form':cl
#     }
#     return render(r,'calculator.html',data)
def calculator(request):
    try:
        if request.method == 'POST':
            form = user(request.POST)
            if form.is_valid():
                n1 = form.cleaned_data['n1']
                o=form.cleaned_data['opt']
                n2 = form.cleaned_data['n2']
            
                d=n1+str(o)+n2
                total=eval(d)
            
                return render(request, 'calculator.html', {'total': total,'title':'Output'})
        else:
            form = user()
    except:
        pass
    return render(request, 'calculator.html', {'form': form,'total':'calculate','title':'Calculator'})

def quiz(request):
    try:
        m=fun_quiz().out[0]
        
        if request.method == 'POST':
            form = fun_quiz(request.POST)
            if form.is_valid() :
                o=request.POST['opt']

            
                
                if o ==fun_quiz().out[1]:
                    return render(request, 'quiz.html', {'total': 'correct','title':'your ans is','q':''})
                   

                else:
                    return render(request, 'quiz.html', {'total':'wrong' ,'title':'your ans is','q':''})
           
                    
        else:
            
            form = fun_quiz()
            
    except:
       pass
    return render(request, 'quiz.html', {'form': form,'total':'submit','title':'Quiz','q':m})
