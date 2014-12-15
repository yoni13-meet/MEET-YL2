from django.shortcuts import render
from django.http import HttpResponse

from models import Question, Answer
# Create your views(functions) here.
# Remember each function/view the first argument/input has to be request

def pizza(request):
	poll_id = 2;
	return render(request, 'index.html', {'my_poll_num': poll_id})

def burger(request):
	poll_ud = 2;
	return render(request, 'Robots.html', {'my_poll_num': poll_ud})

def hotdog(request):
	poll_wd = 2;
	return render(request, 'contact_me.html', {'my_poll_num': poll_wd})