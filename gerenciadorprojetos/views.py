# Create your views here.
from django.http import HttpResponse
from gerenciadorprojetos.models import Project
from django.template import Context, loader


def index(project_id):
	project_list = Project.objects.all()
	t = loader.get_template('index.html')
	c = Context({
		'project_list': project_list,
    	})
    	
	return HttpResponse(t.render(c))
