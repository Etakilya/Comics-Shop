from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import PostForm, CommentForm
from django.shortcuts import render , get_object_or_404, redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from posts.models import Post, Comment
from django.contrib.auth.forms import UserCreationForm




def post_detail(request, id = None):
    instance = get_object_or_404(Post,id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request,"main/post_detail.html", context)


def post_list(request):
    form = PostForm()
    queryset= Post.objects.all()
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post')
    else:
        form = PostForm()
    context = {
        'posts': queryset,
        'form': form,
        "object_list": queryset,
        "title": "List"
    }

    return render(request,"main/index.html", context)

def user(request):
    return render(request,'main/user.html')

def post_update(request):
    return HttpResponse("<h1>Update</h1>")
def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")


def login(request):
    args = {}
    args.update(csrf(request))

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('post')
        else:
            args['login_error'] = "No such username"
            return render_to_response('main/login.html', args)

    else:
        return render_to_response('main/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("login")


def comment(request):
    comment_by_id = Comment.objects.all()
    if request.POST :
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comment')
    else:
        form = CommentForm()
    context = {
        'comments' : comment_by_id,
        'form' : form,
    }
    return render(request,'main/comments.html',context)


def reg(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():

            newuser = auth.authenticate(Username=newuser_form.cleaned_data['username'],
                                        Password=newuser_form.cleaned_data['password2'])
            newuser_form.save()
            auth.login(request, newuser)
            return redirect('post')
        else:
            args['form'] = newuser_form
    return render_to_response('main/reg.html', args)


def teacher(request):
    return render(request,'teacher.html')