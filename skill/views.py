from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render
from .models import *



def index(request):
    template = loader.get_template('skill/index.html')
    return HttpResponse(template.render())


def inside_view(request):
    template = loader.get_template('skill/inside.html')
    return HttpResponse(template.render())

def contact(request):
    if request.method == "POST":
        message = Message()
        message.name = request.POST.get("firstname")
        message.fname = request.POST.get("lastname")
        message.email = request.POST.get("email")
        message.mobile = request.POST.get("phone")
        message.body = request.POST.get("message")
        message.save()

        send_mail(message.mobile,"Имя пользователя: "+message.name+"\n"+"Фамилия пользователя: "+message.fname+"\n"+"Почта пользователя: "+message.email+"\n"+"Тело сообщения: "+"\n"+message.body, settings.EMAIL_HOST_USER, ['kpahomova@yandex.ru'])

        return render(request, "skill/contact.html")
    else:
        return render(request, "skill/contact.html")

def service(request):
    response = request.POST.get("categorylst")
    servic = Service.objects.all().filter(workArea = response)
    listCategory = ListService.objects.all()

    sourse = {'servic':servic, 'listcat':listCategory}
    return render(request,"skill/services.html", sourse)



