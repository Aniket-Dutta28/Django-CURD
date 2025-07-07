from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from.models import Post
from .forms import PostForms
from django.contrib.auth.decorators import login_required
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request,'post_list.html',{'posts':posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForms(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    
    else:
        form = PostForms()
    return render(request,'create_post.html',{'form':form})

def update_post(request,post_id):
    post = get_object_or_404(Post,pk = post_id,user = request.user)
    if request.method == 'POST':
        form = PostForms(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
         form = PostForms(instance=post)
    return render(request,'create_post.html',{'form':form})


def post_delete(request,post_id):
    post = get_object_or_404(Post,pk=post_id,user= request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_delete.html')
