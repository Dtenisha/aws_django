from django.shortcuts import render

# Create your views here

from django.http import HttpResponse

def home(request):
    return render(request,'index.html')
  
def add(request):
  global l1,l2,l3,l4,l5,l6,l7
  #l1,l2 = ''
  l1 = request.GET['file']
  l2 = request.GET.getlist('Type_of_Analysis')
  l3 = request.GET.getlist('Size_of_data')
  l4 = request.GET['count1']
  l5 = request.GET.getlist('correlation')
  l6 = request.GET['Dep_feature']
  l7 = request.GET.getlist('Model')
  # return render(request,'result.html',{'l1':l1,'l2':l2,'l3':l3,'l4':l4,'l5':l5,'l6':l6,'l7':l7})
  return render(request,'result.html',{'l2':l2,'l3':l3,'l4':l4,'l5':l5,'l6':l6,'l7':l7})



