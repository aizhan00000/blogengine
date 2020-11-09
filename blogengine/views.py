from django.http import HttpResponse

def hell0(request):
    return HttpResponse('<h1>Hello mir</h1>')
