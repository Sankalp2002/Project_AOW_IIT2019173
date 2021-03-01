from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def title(request):
    return HttpResponse("Home Page")

def Overview(request):
    my_de = {'Over_tag':'\0'}
    return render(request,'App/overview.html',context=my_de)

def Main(request):
    return HttpResponse("Main")

#def dataset(request):
 #   my_data = {'Data_tag':'\0'}
  #  return render(request,)
