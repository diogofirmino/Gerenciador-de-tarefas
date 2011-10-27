from django.db import models
from django.forms import ModelForm

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=255)

class ProjectForm(ModelForm):
	class Meta:
		model = Project
