# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from gerenciadorprojetos.models import Project, ProjectForm
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404



def project_index(request):
	project_list = Project.objects.all()
	t = loader.get_template('index.html')
	c = Context({
		'project_list': project_list,
    	})
    	
	return HttpResponse(t.render(c))

def project_new(request):
	project_form = ProjectForm()
	t = loader.get_template('new.html')
	c = Context({'project_form': project_form,})
	return HttpResponse(t.render(c))

def project_create(request):
	formset = ProjectForm(request.POST)
       	if formset.is_valid():
		formset.save()
		return HttpResponseRedirect('/projects/')
	else:
		pass

def project_edit(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	p = TaskForm(instance=project)
	t = 'projects/edit.html'
	dic = {'ProjectForm':p,'id':project_id}
	return render_to_response(t,dic)
