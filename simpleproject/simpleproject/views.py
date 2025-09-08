from django.http import HttpResponse
from django.shortcuts import render

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
   return render(request, "about.html")

# def course(request):
#    return HttpResponse("Welcome to Django Course")


# def courseDetails(request, courseid):
#    return HttpResponse(courseid)


def contact(request):
   return render(request, "contact.html")  