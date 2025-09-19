from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm

def homePage(request):
   # data={
   #    'title':'Home',
   #    'bdata':'My name is Shailesh kumar',
   #    'clist':['PHP', 'Java', 'Django'],
   #    'numbers':[10,20,30,40,50],
   #    'student_details':[
   #       {'name':'pradeep', 'phone':9293843904},
   #       {'name':'testing', 'phone':7409033904},
   #    ]
   # }
   # return render(request, "index.html", data)
   return render(request, "index.html")

def about(request):
   # return HttpResponse("<b>Welcome to Django</b>")
   if request.method=="GET":
      output=request.GET.get('output')
   return render(request, "about.html",{'output':output})

# def course(request):
#    return HttpResponse("Welcome to Django Course")


# def courseDetails(request, courseid):
#    return HttpResponse(courseid)




def submitform(request):
   try:
      if request.method=="POST":
       # n1=int(request.GET['num1'])
       # n2=int(request.GET['num2'])
       n1=int(request.POST.get('num1'))
       n2=int(request.POST.get('num2'))
      # print(n1+n2)
       finalans=n1+n2
       data={
          'n1':n1,
          'n2':n2,
          'output':finalans
       }

      #  return HttpResponse(finalans)

       url="/about/?output={}".format(finalans)

       return redirect(url)
   except:
    pass      
   

# def userForm(request):
#    finalans =0
#    try:
#       # n1=int(request.GET['num1'])
#       # n2=int(request.GET['num2'])
#       n1=int(request.GET.get('num1'))
#       n2=int(request.GET.get('num2'))
#       # print(n1+n2)
#       finalans=n1+n2
#    except:
#       pass   
#    return render(request, "userform.html",{'output':finalans})



# def userForm(request):
#    finalans =0
#    try:
#       if request.method=="POST":
#        # n1=int(request.GET['num1'])
#        # n2=int(request.GET['num2'])
#        n1=int(request.POST.get('num1'))
#        n2=int(request.POST.get('num2'))
#       # print(n1+n2)
#        finalans=n1+n2
#    except:
#       pass   
#    return render(request, "userform.html",{'output':finalans})



def contact(request):
   return render(request, "contact.html") 
def calculator(request):
   c=''
   try:
       if request.method=="POST":
          n1=eval(request.POST.get('num1'))
          n2=eval(request.POST.get('num2'))
          opr=request.POST.get('opr')
          if opr=="+":
             c=n1+n2
          elif opr=="-":
             c=n1-n2 
          elif opr=="*":
             c=n1*n2
          elif opr=="/":
             c=n1/n2        
   except:
      c="Invalid opr......"
      print(c)   
   return render(request, "calculator.html",{'c':c})



def saveevenodd(request):
    c=''
    if request.method=="POST":
       n=eval(request.POST.get('num1'))
       if n%2==0:
          c="Even Number"
       else:
          c="Odd Number"   
    return render(request, "evenodd.html",{'c':c})



def marksheet(request):
   if request.method=="POST":
      s1=eval(request.POST.get('subject1'))
      s2=eval(request.POST.get('subject2'))
      s3=eval(request.POST.get('subject3'))
      s4=eval(request.POST.get('subject4'))
      s5=eval(request.POST.get('subject5'))
      t=s1+s2+s3+s4+s5
      p=t*100/500
      if p>=60:
         d="First Div"
      elif p>=48:
         d="Second Div"
      elif p>=35:
         d="Third Div"
      else:
         d="Fail"       
      data={
         'total':t,
         'per':p,
         'div':d,
      }
      return render(request, "marksheet.html",data)
   return render(request, "marksheet.html")




def userForm(request):
   finalans =0
   fn=usersForm()
   # data={}
   data={'form':fn}
   try:
      if request.method=="POST":
       # n1=int(request.GET['num1'])
       # n2=int(request.GET['num2'])
       n1=int(request.POST.get('num1'))
       n2=int(request.POST.get('num2'))
      # print(n1+n2)
       finalans=n1+n2
      #  data={
      #     'n1':n1,
      #     'n2':n2,
      #     'output':finalans
      #  }
       data={
         'form':fn,
         'output':finalans
       }

       url="/about/?output={}".format(finalans)

      #  return HttpResponseRedirect('/about/')
      #  return HttpResponseRedirect(url)
      return redirect(url)
   except:
      pass   
   return render(request, "userform.html",data)