from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    todoList = Todo.objects.order_by('id')


    context = {'todoList': todoList}
    return render(request, 'todo/index.html', context)