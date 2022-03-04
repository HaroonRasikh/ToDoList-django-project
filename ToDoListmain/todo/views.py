from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def index(request):
	todo = Todo.objects.all() # 5-a now we want also our new added data shoud be showed in home page so
	if request.method == 'POST': # 1
		new_todo = Todo(title = request.POST['title']) # 2 
		new_todo.save() # 3
		return redirect('/')  # 4  from one to 4 it all its doing is saving ourt adding data from home page to admin
	return render(request, 'index.html',{'todos':todo}) # 5-b {}
def delete(request,pk): # 7
	todo = Todo.objects.get(id=pk) # 8
	todo.delete() # 9 
	return redirect('/') # amd return back to our main page
