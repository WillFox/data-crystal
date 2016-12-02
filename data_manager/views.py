from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from data_crystal.settings import URL_PREFIX
from data_manager.models import Data
###############################################################################
def app_home(request):
	template = loader.get_template('data_manager/home.html')
	if request.user.is_authenticated():
		#display "novel" data or new data/collections
		data=Data.objects.all()
		return HttpResponse(template.render(context,request)) 
	else:
		data=Data.objects.all()
		data=data.filter(public=True)
		context={
		  'prefix':URL_PREFIX,
		  'datas':data,
		}
		#display interesting public data
		return HttpResponse(template.render(context,request)) 

def data(request):
	print "loading here"
	template = loader.get_template('data_manager/home.html')
	if request.user.is_authenticated():
		#display "novel" data or new data/collections
		data=Data.objects.all()
		return HttpResponse(template.render(context,request)) 
	else:
		data=Data.objects.all()
		data=data.filter(public=True)
		context={
		  'prefix':URL_PREFIX,
		  'datas':data,
		}
		#display interesting public data
		return HttpResponse(template.render(context,request)) 

def data_view(request,dataid):
	print dataid
	data_id=request.GET#.get('data_id')
	template = loader.get_template('data_manager/data_simple.html')
	print data_id
	if request.user.is_authenticated():
		#display "novel" data or new data/collections
		data=Data.objects.get(id=dataid)
		context={
		  'prefix':URL_PREFIX,
		  'datas':data,
		  'data_id':data_id,
		}
		return HttpResponse(template.render(context,request)) 
	else:		
		#data=data.filter(id=data_id)
		data=Data.objects.get(id=dataid)
		print data
		
		context={
		  'prefix':URL_PREFIX,
		  'data':data,
		  'data_id':data_id,
		}
		#display interesting public data
		return HttpResponse(template.render(context,request)) 

def instrument(request):
	pass


def collection(request):
	pass


def analysis(request):
	pass

