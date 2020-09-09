from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    chat = 'Hello'
    name = 'juwon'

    return render(request, 'home.html', {'user_chat':chat, 'user_name':name})

students=['세령', '세준', '서진', '지우']

def result(request):
    name = request.POST['username']

    if name in students:
        is_exist = True
    else:
        is_exist = False
    
    return render(request, 'result.html', {'user_name' : name, 'is_exist': is_exist})



# stu = ['세령', '세준', '지우', '서진']

# def result(request):
#     name = request.POST['username']
    
#     if name in stu:
#         is_exist = True
#     else:
#         is_exist = False

#     return render(request, 'result.html', {'user_name' : name, 'is_exist': is_exist})