from __future__ import unicode_literals

from django.db import models



class Data(models.Model):
	"""
	Suggested 
		-name
		slug//just use id?
		created_on
		updated_on
		data_original_path
		data_path
		data_quality
		image_rep_path
		description
		owners/users
		public
		tags
		instrument
		collection
		characteristic
	"""
	
	name   		= models.CharField(max_length=200)
	public 		= models.BooleanField(default=False)
	created_on	= models.DateTimeField(auto_now=True)
	updated_on	= models.DateTimeField(auto_now=True)
	description	= models.TextField(max_length=2000,default="none")
	origin_path = models.FilePathField(max_length=100,default="none")
	path_to_file= models.FilePathField(max_length=100,default="none")

class Instrument(models.Model):
	"""
	Suggested 
		name
		slug
		created_on
		updated_on
		image_rep_path
		description
		users/admin_owners
		owners/users
		public
		characteristics
		tags
	"""
	name = models.CharField(max_length=200)

class Collection(models.Model):
	"""
	Suggested 
		name
		slug
		created_on
		updated_on
		description
		admin_owners
		owners/users
		public
		characteristics
		tags

	"""
	name = models.CharField(max_length=200)

class Analysis(models.Model):
	"""
	Suggested 
		name
		slug
		created_on
		updated_on
		path_to_script
		description
		admin_owners
		owners/users
		public
		characteristics
		tags

	"""
	name = models.CharField(max_length=200)