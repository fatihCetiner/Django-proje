from django.shortcuts import render, HttpResponse, get_object_or_404 ,HttpResponseRedirect,redirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def post_index(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
      post_list = post_list.filter(title__icontains= "q")
    
    paginator = Paginator(post_list ,5) # Show 25 contacts per page

    page = request.GET.get('sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post/index.html' , {'posts' : posts})

def post_detail(request, id):
    post = get_object_or_404(Post,id=id)
    context = {
            'post': post,
            
            }
    return render(request, 'post/detail.html',context)

def post_create(request):

  #if not request.user.is_authenticated():
  #  return Http404()
      
   # if request.method == "POST":
   #     print(request.POST)
  # *************************************************************** 
  # title = request.POST.get('title')
  # content = request.POST.get('conrtent')
  # Post.objects.create(title = title , content = content)
  # ****************************************************************
   # if  request.method == "POST":
        # Formdan gelen bilgileri kaydet
   #     form = PostForm(request.POST)
   #     if form.is_valid() : # formun düzgn doldurulup doldurulmadığını kontrol eder
   #         form.save()
        
   # else:
        #Formu kullanıcıya göster
   #     form = PostForm()
    
    form = PostForm(request.POST or None ,request.FILES or None)
    if form.is_valid() : # formun düzgn doldurulup doldurulmadığını kontrol eder
            post = form.save()
            messages.success(request , 'Başarılı bir şekilde oluşturdunuz.')
            return HttpResponseRedirect(post.get_absolute_url())
      
        
    context = {
            'form': form ,
            
     }
    
    return render(request, 'post/form.html',context)


def post_update(request, id):

  #if not request.user.is_authenticated():
    #return Http404()

    post = get_object_or_404(Post,id=id) # post getirme kodu
    form = PostForm(request.POST or None, request.FILES or None, instance= post) # form getirme kodu
    if form.is_valid() : 
            form.save()
            messages.success(request , 'Başarılı bir şekilde düzenlediniz.')
            return HttpResponseRedirect(post.get_absolute_url())
    context = {
            'form': form ,
            
     }
    return render(request, 'post/form.html',context)


def post_delete(request, id):

  #if not request.user.is_authenticated():
   # return Http404()
    
    post = get_object_or_404(Post,id=id)
    post.delete()
    return redirect('post:index')


def post_download(request):

  return render(request, 'vrekle.html',{})

