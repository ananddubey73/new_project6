from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='This data is our assumpion'
    d={'assumpion':data}
    return render(request,'data_render.html',context=d)

def new_render(request):
    s='Hello googol how are you'
    f={'google':s}
    return render(request,'new_render.html',f)