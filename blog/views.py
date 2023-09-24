from django.shortcuts import render, redirect 
from django.db.models import Q 
from django.contrib import messages  #to show message when registration of user created.
from django.contrib.auth import authenticate, login, logout #to do login, logout 

#import paginator stuff
from django.core.paginator import Paginator 

#Login requred to create form
from django.contrib.auth.decorators import login_required


from .models import Blog
from .forms import BlogForm, RegisterUser
from .filters import BlogFilter


# Create your views here.
def home(request):
    #set up pagination
    p = Paginator(Blog.objects.all(), 2)
    page = request.GET.get('page')
    blog = p.get_page(page)
    context ={
        'blog': blog,
    }
    return render(request, 'blog/home.html', context)

def detail(request, pk):
    blog = Blog.objects.get(id=pk)
    context={
        'blog':blog
    }
    return render(request, 'blog/detail.html', context)
#----------------------------------------------------------------------------------

# BEGIN of Create, Update, Detele (CRUD) funcion
@login_required(login_url='login')
def create(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST or None, request.FILES or None)
        if form.is_valid:
            form.save()
            return redirect('/')
    context= {
        'form': form,
    }
    return render(request, 'blog/create.html', context)

def update(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'blog/create.html', context)

def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method =="POST":
        blog.delete()
        return redirect('/')
    context = {'blog': blog}
    return render(request, 'blog/delete.html', context)
# END of CRUD. 
#-----------------------------------------------------------------------------------

#BEGIN of Search function
#method number 1 using Q
def search(request):
    query = request.GET.get('q')
    queryset = Blog.objects.all()
    if query is not None:
        lookups = Q(id__icontains=query)|Q(title__icontains=query)|Q(category__icontains=query)
        query_set = Blog.objects.filter(lookups)
    context = {
        'blog': query_set
    }
    return render(request, 'blog/home.html', context)

#method number 2 using django_filter extension
def detail_search(request):
    blog = Blog.objects.all()
    myFilter = BlogFilter(request.GET,queryset=blog)
    blog = myFilter.qs
    context = {
        'blog': blog,
        'myFilter': myFilter,
    }
    return render(request, 'blog/detail_search.html', context)
#END of Search function. 
#------------------------------------------------------------------------------------

#BEGIN Register User Function
def register_user(request):
    form = RegisterUser()
    if request.method == "POST":
        form = RegisterUser(request.POST or None)
        if form.is_valid:
            form.save()
            user = form.cleaned_data.get('username') #to get the username just created. 
            messages.success(request, f'Account created for {user}')
            return redirect('/')
    context={
        'form':form
    }
    return render(request, 'blog/register.html', context)
#-------------------------------------------------------------------------------

#login function
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return redirect('/')
    return render(request, 'blog/login.html')

#logout function
def logout_user(request):
    logout(request)
    return redirect('/')
#-----------------------------------------------------------------------------------

