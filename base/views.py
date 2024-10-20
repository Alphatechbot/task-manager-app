from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import MyUser
from .models import TodoList
from .forms import UpdateForm, MyUserCreationForm


# Create your views here.
@login_required(login_url='base:login')
def index(request):
    q = request.user
    print(q)
    todo = TodoList.objects.all().order_by('-created_at')
    if q in todo:
        if request.method == 'POST':
            task = request.POST.get("task")
            task = todo.create(name=task)
            task.save()
        if request.POST.get('edit'):
            return redirect('base:update')

    context = {'todo': todo}

    return render(request, 'index.html', context)


def todoUpdate(request, id):
    task = TodoList.objects.get(id=id)
    form = UpdateForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('base:home')
    context = {
        'form': form,
        'task': task
    }
    return render(request, 'update.html', context)


def todoDelete(request, id):
    task = TodoList.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('base:home')
    context = {
        'task': task
    }
    return render(request, 'delete.html', context)


def registerview(request):
    form = MyUserCreationForm
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            user.name = user.username.lower()
            user.save()
            return redirect('base:login')
        else:
            messages.error(request, 'An error occurred during registration')
    else:
        form = MyUserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def loginview(request):
    user = MyUser.objects.all()
    if request.user.is_authenticated:
        return redirect('base:home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('base:home')
        else:
            messages.error(request, 'Username or Password does not exist ')

    return render(request, 'login.html', {'user': user})


def logoutview(request):
    logout(request)
    return redirect('base:login')
