from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import user
from .quiz import fun_quiz
from service.models import service
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
    #this statment will change the contents of submit button after clicking in it
    # return render(r,'contact.html',{'ad':"thanks for contacing us",'ty':"text"}) 
    return redirect("/about/") #this will redirect to about page.
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
    print(list(table_data)[0])
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
