import re
from django.shortcuts import render
from .models import medical,shoppingmall
# Create your views here.
def home(request):
    return render(request,"index.html")

def search(request):
    if request.method=='POST':
        #med=medical()
        catch=request.POST.get('search')
        if catch=='medical'or catch=='med' or catch=='nearby medical shop':
            med1=medical.objects.all()
            return render(request,'base.html',{'med1':med1})
        elif catch=='shopping':
            shop=shoppingmall.objects.all()
            return render(request,'base.html',{'med1':shop})
        return render(request,'index.html')
        
    else:
        return render(request,'index.html')
def adddetails(request):
    return render(request,'add.html')
def medic(request):
    med=medical()
    med.name=request.POST.get('name')
    med.address=request.POST.get('address')
    med.image=request.POST.get('image')
    med.url=request.POST.get('url')
    med.save()
    med1=medical.objects.all()
    return render(request,'base.html',{'med1':med1})