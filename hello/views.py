
from django.shortcuts import render

from django.contrib.auth.decorators import login_required


def hello_world(request):
    # return HttpResponse("Hello, World!")
    return render(request, 'hello.html')

# @login_required
def home_page(request):
    # return HttpResponse("Hello, World!")
    return render(request, 'home.html')


