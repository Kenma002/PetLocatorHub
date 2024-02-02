from django.shortcuts import render, redirect
from django.contrib .auth import authenticate, login, logout
from .forms import *
from .forms import PostForm
from .forms import ReportForm



# Create your views here.

def base(request):
    return render(request, 'pages/home.html')

def register_user(request):
    return render(request, 'pages/register.html')

def form(request):
    return render(request, 'pages/form.html')

def Login_user(request):
    if request.user.is_authenticated is not None:
        return render(request,'pages/login.html')
    return redirect(to='base')

def Logout_user(request):
    if request.user.is_authenticated is not None:
         logout(request)
    return redirect(to='login')

def posts(request):
    return render(request, 'pages/posts.html')

def posts_create(request):
    return render(request, 'pages/posts_create.html')

def profile(request):
    return render(request, 'pages/profile.html')

def reports(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='posts')
    context = {
        'form': form
    }
    return render(request, 'pages/reports.html',context)

def post_detail(request, pk):
     
     reports = Report.objects.filter(post_id=pk)
     post = Post.objects.filter(pk=pk).first() 
     return render(request, 'pages/post_detail.html',{'post': post, 'reports': reports})  
 
def post_update(request, pk):
         
     posts = Post.objects.get(pk=pk)
     postForm=PostForm(instance=posts)
     if request.method == 'POST':
         postForm = PostForm(request.POST,request.FILES, instance=posts)
         if postForm.is_valid():
             postForm.save()
             return redirect(to="posts")
     
     return render(request, 'pages/post_update.html', {'posts': posts, 'form': postForm})

def post_delete(request, pk):
    
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect(to="posts")

def posts_list(request,):
    posts = Post.objects.all()
    return render(request, 'pages/post_list.html',{'posts': posts})
    
def Login_store(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    
    if user is not None:
        login(request, user)
        return redirect(to='base')
    else:
        return redirect(to='login')

def found_create(request):
    
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='posts')
    context = {
        'form': form
    }
    return render(request, 'pages/found_create.html',context)

def found_update(request, pk):    
     report = Report.objects.get(pk=pk)
     reportForm=ReportForm(instance=report)
     if request.method == 'POST':
         reportForm = ReportForm(request.POST,request.FILES, instance=report)
         if reportForm.is_valid():
             reportForm.save()
             return redirect(to="posts")
     
     return render(request, 'pages/found_update.html', {'report': report, 'form': reportForm})
 
def found_delete(request, pk):
    
    post = Report.objects.get(pk=pk)
    post.delete()
    return redirect(to="posts")
