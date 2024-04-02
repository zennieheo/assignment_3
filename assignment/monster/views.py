from django.shortcuts import render

# Create your views here.

def hello (request):
    return render(request, 'hello.html')


#hello라는 함수를 define하고.... h
