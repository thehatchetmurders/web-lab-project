from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comments, Messages, Consult, Doctors, Department, Blogs
from .forms import CommentsForm, MessagesForm, ConsultsForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic import DeleteView
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def home_page(request):
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            fname = request.POST['name']
            femail = request.POST['email']
            fsubject = request.POST['subject']
            fmessage = request.POST['message']

            addr_from = "aaysar@mail.ru"  # Адресат
            addr_to = "aaysar@mail.ru"  # Получатель
            password = "AISAR260202"  # Пароль
            subject_theme = 'Hello my name is ' + fname + ' and email: ' + femail + '. I am writing about ' + fsubject + '; MESSAGE FROM MEDIPLUS SITE'

            msg = MIMEMultipart()  # Создаем сообщение
            msg['From'] = addr_from  # Адресат
            msg['To'] = addr_to  # Получатель
            msg['Subject'] = subject_theme  # Тема сообщения

            body = fmessage
            msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст

            server = smtplib.SMTP('smtp.mail.ru', 25)  # Создаем объект SMTP
            server.starttls()  # Начинаем шифрованный обмен по TLS
            server.login(addr_from, password)  # Получаем доступ
            server.send_message(msg)  # Отправляем сообщение
            server.quit()  # Выходим

            form.save()
    doctors = Doctors.objects.all()[:8]
    blogs = Blogs.objects.all()[:6]
    form = MessagesForm()
    context = {
        'doctors' : doctors,
        'blogs' : blogs,
        'form' : form
    }
    return render(request, "testapp/index.html", context)

def appointment(request):
    if request.method == 'POST':
        form = ConsultsForm(request.POST)
        if form.is_valid():
            form.save()
    form = ConsultsForm()
    context = {
        'form' : form
    }
    return render(request, "testapp/appointment.html", context)

def blog(request, pk):
    blog = Blogs.objects.get(id=pk)

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()

    comments = Comments.objects.all()[:10]
    form = CommentsForm()
    context = {
        'blog' : blog,
        'comments' : comments,
        'form' : form
    }
    return render(request, "testapp/blog-single.html", context)


def create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'registration/create.html', context)

def doctors_list(request, department_slug=None):
    department = None
    departments = Department.objects.all()
    doctors = Doctors.objects.filter(available=True)
    if department_slug:
        department = get_object_or_404(Department, slug=category_slug)
        departments = doctors.filter(category=category)
    return render(request, "testapp/index.html",
                  {
                        'department': department,
                        'departments': departments,
                  })


def updateComment(request, pk):
	comment = Comments.objects.get(id=pk)
	form = CommentsForm(instance=comment)

	if request.method == 'POST':
		form = CommentsForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'testapp/update.html', context)

def deleteComment(request, pk):
	comment = Comments.objects.get(id=pk)
	if request.method == "POST":
		comment.delete()
		return redirect('/')
	context = {'item':comment}
	return render(request, 'testapp/delete.html', context)

