from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def introduction(request):
    return HttpResponse("<marquee><h1>A Beautiful lovestory!!..............</h1></marquee>")
def coverpage(request):
    return HttpResponse("<center><h1>Romeo and Juliet</h1></center>")
def index(request):
    return HttpResponse("<center><h1>Welcome to great lovestory of Romeo and Juliet</h1></center>")
def page(request):
    return render(request,'book.html')
def page1(request):
    return render(request,'sample1.html')
def page2(request):
    return render(request,'sample2.html')
def page3(request):
    return render(request,'sample3.html')

