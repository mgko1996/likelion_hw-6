from django.shortcuts import render, redirect, get_object_or_404
from .models import Post,Comment


def new(request):
    return render(request, 'posts/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        user = request.user
        Post.objects.create(title=title,user=user,content=content,image=image)
        return redirect('posts:main')

def main(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html', {'posts': posts})


def show(request, id):
    post = Post.objects.get(pk=id)
    post.view_count += 1
    post.save()
    all_comments =post.comments.all().order_by('-created_at')
    return render(request, 'posts/show.html', {'post': post, 'comments':all_comments})


def update(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content'] 
        post.image = request.FILES.get('image') 
        post.save()
        return redirect('posts:show',post.id)
    return render(request, 'posts/update.html',{"post":post})


def delete(request,id):
    post = get_object_or_404(Post,pk=id)
    post.delete()
    return redirect("posts:main")


def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, post=post)
    return redirect('posts:show', post.pk)


def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        comment.content = request.POST['content'] 
        comment.save()
        return redirect('posts:show', comment.post.id)  
    return render(request, 'posts/update_comment.html', {"comment":comment})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment,pk= comment_id)
    comment.delete()
    return redirect("posts:show", comment.post.id)