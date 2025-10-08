from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def home(request):

	if request.method == 'POST':
		taskForm = TaskForm(request.POST or None)
		if(taskForm.is_valid()):
			taskForm.save()

	all_tasks = Task.objects.order_by('-id')[:5]
	return render(request, 'home.html', {'all_tasks': all_tasks})

def about(request):
	return render(request, 'about.html', {})

