from django.shortcuts import render, redirect
from .models import Email
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request, 'main_app/index.html')

def create(request):
    if request.method =="POST":
        result= Email.objects.register(request.POST['email'])
        if result[0]==False:
            messages.error(request,result[1])
            return redirect('/')
        else:
            return redirect('/success')

def success(request):
    context = {
        "emails" : Email.objects.all(),
    }
    return render (request, 'main_app/success.html', context)


def destroy(request, id):
        Email.objects.get(id=id).delete()
        return redirect('/')
