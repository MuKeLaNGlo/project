from django.http import HttpResponse
  
def index(request):
    return HttpResponse("Hello qrfdwrf")

def second_view(request):
    return HttpResponse("кал какой то")