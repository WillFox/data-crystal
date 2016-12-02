from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from data_crystal.settings import URL_PREFIX
from data_manager.models import Data
###############################################################################
def about(request):
	template = loader.get_template('data_crystal/about.html')
	context={
	  'prefix':URL_PREFIX,
	}
	return HttpResponse(template.render(context,request)) 

def contact(request):
	template = loader.get_template('data_crystal/contact.html')
	context={
	  'prefix':URL_PREFIX,
	}
	return HttpResponse(template.render(context,request)) 
