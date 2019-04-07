from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render
from .models import *
import pyrebase


config = {
    'apiKey': "AIzaSyD-rMTsJP9loNbVy3vvAJk22Mo-Swt-h2Q",
    'authDomain': "one16-fca86.firebaseapp.com",
    'databaseURL': "https://one16-fca86.firebaseio.com",
    'projectId': "one16-fca86",
    "storageBucket": "one16-fca86.appspot.com",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()



def index(request):

    task_count =db.child("Tasks").get()

    count = len(task_count.each())
    return render(request, "skill/index.html", {'count':count})


def inside_view(request):
    template = loader.get_template('skill/inside.html')
    return HttpResponse(template.render())

def blog_view(request):
    list_blog = Blog.objects.all()

    return render(request, "skill/blog.html", {"listblog":list_blog})

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

    #servic = Service.objects.all().filter(workArea = response)
    #listCategory = ListService.objects.all()

    #sourse = {'servic':servic, 'listcat':listCategory}

    list_category = []
    list_id_category = []
    list_name_category = []
    list_body_task = []
    list_cost_task = []
    list_name_task = []
    list_place_task = []
    list_category_task = []


    cathegory = db.child("Categories").get().val()

    for i in cathegory[1:]:
        list_name_category.append(i['catName'])
        list_id_category.append(i['catNum'])

    list_category = zip(list_name_category,list_id_category)


    tasks = db.child("Tasks").get()

    count = len(tasks.each())



    for i in tasks.each():
        list_name_task.append(i.val()['name'])
        list_body_task.append(i.val()['desc'])
        list_cost_task.append(i.val()['cost'])
        list_place_task.append(i.val()['place'])

        if (i.val()['catNum'] == response):
            list_category_task.append(i.val()['catNum'])


    tasks_all = zip(list_name_task,list_body_task,list_cost_task,list_place_task, list_category_task)


    sourse = {'tasks': tasks_all, 'cathegory': list_category}

    #print(tasks.values)


    return render(request,"skill/services.html", sourse)



