from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    data = {
        "hello",
        "bye"
    }
    return HttpResponse(data)