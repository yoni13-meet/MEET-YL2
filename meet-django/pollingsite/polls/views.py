from django.shortcuts import render
from django.http import HttpResponse

from models import Question, Answer
# Create your views(functions) here.
# Remember each function/view the first argument/input has to be request

def pizza(request):
	return HttpResponse("I love Pizza")