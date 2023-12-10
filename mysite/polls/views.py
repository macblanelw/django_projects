from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World. You are at df50a2f7 in the polls index.")