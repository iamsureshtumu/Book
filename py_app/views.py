from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pyspiders(request):
    return HttpResponse("<marquee><h1>Welcome to Pyspiders Library........!!</h1></marquee>")
def title(request):
    return HttpResponse("<center><h1>Python Full-Stack Development</h1></center>")
def index(request):
    return HttpResponse("<center><h1>python, Django, Html5, Css3, JS, SQL</h1></center>")
def python(request):
    return render(request,'python.html')
def django(request):
    return render(request,'django.html')
def html(request):
    return render(request,'html.html')
def css(request):
    return render(request,'css.html')
def js(request):
    return render(request,'js.html')
def sql(request):
    return render(request,'sql.html')

