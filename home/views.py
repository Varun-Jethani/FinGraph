from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from django.template import loader

#For creating Graph
from home.grfgenerater import generate_graph



def home(request):
    return render(request,'index.html')


@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        stock= request.POST.get('stock')
        # Process form data here
        return HttpResponse('Form submitted successfully')
    else:
        return render(request, 'index.html')
    
def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

@csrf_exempt
def content(request):
    if request.method == 'POST':
        stock = request.POST.get("stock")
        print(stock)
        html = generate_graph(stock)
        return render(request,'content.html',{'html':html})


    return render(request,'content.html',{'html':''})

