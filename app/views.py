from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.forms import *

def Form(request):
    form=New_Form()
    if request.method=="POST":
        form_data=New_Form(request.POST)
        if form_data.is_valid():
            #return HttpResponse(str(form_data.cleaned_data))
            
            #name=form_data.cleaned_data['name']
            #age=form_data.cleaned_data['age']
            #email=form_data.cleaned_data['email']
            #url=form_data.cleaned_data['url']
            #date=form_data.cleaned_data['date']
            #datetime=form_data.cleaned_data['datetime']
            #time=form_data.cleaned_data['time']
            password=form_data.cleaned_data['password']
            address=form_data.cleaned_data['address']
            gender=form_data.cleaned_data['gender']
            course=form_data.cleaned_data['course']
            gender1=form_data.cleaned_data['gender1']
            checkbox=form_data.cleaned_data['checkbox']


            #d={'name':name,'age':age,'email':email,'url':url,'date':date,'datetime':datetime,'time':time}
            d={'password':password,'address':address,'gender':gender,'course':course,'gender1':gender1,'checkbox':checkbox}
            return render(request,'form_data.html',context=d)

            
    return render(request,'form.html',context={'form':form})