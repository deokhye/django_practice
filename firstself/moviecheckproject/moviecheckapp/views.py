from django.shortcuts import render

# Create your views here.

def home(request):
    chat = 'Hello'
    name = 'juwon'

    return render(request, 'home.html', {'user_chat':chat, 'user_name':name})



movies = ['spiderman', 'lala-land','begin-again', 'about-time']

def result(request):
    title = request.POST['titlename']

    if title in movies:
        is_exist = True
    else:
        is_exist = False

    return render(request, 'result.html', {"title_name" : title, "is_exist": is_exist})