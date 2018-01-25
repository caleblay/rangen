from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
unique_id = get_random_string(length=14)
unique_id
u'heretakeit'

def index(request):
	if 'count' not in request.session:
		request.session['count'] =1
	if 'count' in request.session:
		request.session['count'] +=1
	if 'word' in request.session:
		del request.session['word']
	else:
		request.session['word']=unique_id



	return render(request, 'ranword_app/index.html')


