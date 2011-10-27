# Create your views here.
from django.http import HttpResponse
from gerenciadorprojetos.models import Project, ProjectForm
from django.template import Context, loader


def index(request):
	project_list = Project.objects.all()
	t = loader.get_template('index.html')
	c = Context({
		'project_list': project_list,
    	})
    	
	return HttpResponse(t.render(c))

def create(request):
	if request.POST:
		formset = ProjectForm(request.POST)
        	if formset.is_valid():
            		formset.save()
		else:
			pass
	else:
		project_form = ProjectForm()
		t = loader.get_template('create.html')
		c = Context({'project_form': project_form,})
		return HttpResponse(t.render(c))
