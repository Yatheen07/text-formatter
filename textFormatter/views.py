from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import re

def boldThis(data):
    listt = re.findall(r'\*\*([a-zA-Z\\__,.\s]+)\*\*',data)
    if listt:
        for i in listt:
            temp = '<b>'+i+'</b>'
            data = data.replace(i,temp)
            data = data.replace("**",'')
            print(i)
        return data
    else:
        return data
    
def italicThis(data):
    listt = re.findall(r'\\\\([a-zA-Z\*,__.\s]+)\\\\',data)
    if listt:
        for i in listt:
            temp = '<em>'+i+'</em>'
            data = data.replace(i,temp)
            data = data.replace("\\",'')
            print(i)
        return data
    else:
        return data
    
def underLineThis(data):
    listt = re.findall(r'__([a-zA-Z\*\\,.\s]+)__',data)
    if listt:
        for i in listt:
            temp = '<u>'+i+'</u>'
            data = data.replace(i,temp)
            data = data.replace("__",'')
            print(i)
        return data
    else:
        return data

def homepage(request):
    return render(request,'textFormatter/index.html')

def handshake(request):
    inputData = request.POST.get("Data") 
    print("Input received is: " + inputData)
    return HttpResponse("<strong>"+inputData+"</strong>")

def makeItBold(request):
    inputData = request.POST.get("Data") 
    resultData = boldThis(inputData)
    resultData = italicThis(resultData)
    resultData = underLineThis(resultData)
    return HttpResponse(resultData)







