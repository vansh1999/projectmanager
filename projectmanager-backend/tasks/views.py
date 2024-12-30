from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm



def index(request):

	# list of all tasks from db. Doing Read here
	tasks = Task.objects.all()

	# if user submitting form , post method.
	if request.method == 'POST':
		# create a TaskForm instance via form  data is in request.POST
		form = TaskForm(request.POST)

		# if form is vaid , save the new task in db and Redirect to the main page index
		if form.is_valid():
			form.save()
			return redirect('index')

	# if user is not submitting form, just visiting form, empty form should display on page
	else:
		form = TaskForm()

	# pass tasks and form as context used in templates html 
	return render(request , 'index.html' , {'tasks' : tasks , 'form' : form })


def edit_task(request , pk ):

	# fetch task to be edited / clicked . get_object_or_404 fetches task from Task , with corresponds to primary key (pk) passed to the view. if no pk exist , django will return 404 error
	task = get_object_or_404(Task , pk=pk)

	# if user performs edit 
	if request.method == 'POST':

		# creates form TaskForm for the task to be edited, and instance task form is linked to task edited
		form = TaskForm(request.POST , instance=task)

		# if form is valid , save to db and redirect to home
		if form.is_valid():
			form.save()
			return redirect('index')

	# if user is not submitting form, display form only, this time with pre existing data too !
	else:
		form = TaskForm(instance=task)

	# renders to edit_task.html page, pass form in context for html templates
	return render( request , 'edit_task.html' , {'form' : form})


def delete_task(request, pk):

    task = get_object_or_404(Task , pk=pk)

    task.delete()

    return redirect('index')

