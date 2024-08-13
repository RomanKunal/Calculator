from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'index.html')
def add(request):
    val1 = int(request.POST['input1'])
    val2 = int(request.POST['input2'])
    res = val1 + val2
    return render(request, 'output.html', {'output': res})
def sub(request):
    val1 = int(request.POST['input1'])
    val2 = int(request.POST['input2'])
    res = val1 - val2
    return render(request, 'output.html', {'output': res})
def mul(request):
    val1 = int(request.POST['input1'])
    val2 = int(request.POST['input2'])
    res = val1 * val2
    return render(request, 'output.html', {'output': res})
def div(request):
    val1 = int(request.POST['input1'])
    val2 = int(request.POST['input2'])
    res = val1 / val2
    return render(request, 'output.html', {'output': res})
