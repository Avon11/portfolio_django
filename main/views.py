from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView
from django.views import View
# Create your views here.
def index(request):
    context={
        'name':'Abhinav Rana',
        'email':'abhinavrana132000@gmail.com',
        'address':'121/3 Rana Mansion Ch. Charan Singh colony,Roorkee,Uttarakhand',
        'mobile':'9897367795',
        'linkedin':'https://www.linkedin.com/in/abhinav-jrana',
        'github':'https://github.com/Avon11',
        'instagram':'https://instagram.com/abhinavjatrana',
        'education':['Senior Secondary Kendriya Vidyalaya No 2,Roorkee,Uttarakhand','Bachelor of technology Computer Science Lovely Professional University'],
        'skills':['C', 'C++', 'Python' ,'HTML', 'CSS','JavaScript', 'Django'],
        'projectlinks':[
        'https://github.com/Avon11/INT-213-FloodRelief-Project',
        'https://avon11.github.io/FoodDelivery/',
        'https://avon11.github.io/Dice-Game-TwoPlayers/',
        'https://avon11.github.io/GuessMyNumber/'
        ],
        'languages':['English','Hindi'],
        'interests':['Photography','Web development','Application development','Cricket']
    }
    return render(request,'main\index.html',context)