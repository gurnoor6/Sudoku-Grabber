from django.shortcuts import render,redirect
from .forms import *
from django.http import HttpResponse
from .models import ImageForm
from .signals import returnPath
from .make_sudoku import make_sudoku
# Create your views here.
list =[]
def formpage(request):
	if request.method=='POST':
		name = request.POST['name']
		age = request.POST['age']
		dictionary =  {'name': name, 'age':age}
		list.append(dictionary)
		print(list)
		return render(request, 'formhtml.html')
	else:
		return render(request,'formhtml.html')

def image_view(request):
	if request.method=='POST':
		farm = generalImageForm();
		form = generalImageForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			img_path,full_img_path = returnPath();

		if(img_path!=None):
			detected_sudoku,answer_sudoku = make_sudoku(full_img_path)


		dictionary = {
		"form":farm,
		"img":img_path,
		"uploaded":detected_sudoku,
		"answer":answer_sudoku
		}
		return render(request,'djangoform.html',dictionary) 

	else:
		form = generalImageForm()
		return render(request,'djangoform.html',{"form":form})

def result(request):
	return render(request,'result.html')

