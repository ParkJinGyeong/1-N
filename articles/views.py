from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.

def index(request):

    articles = Article.objects.all() #Article 객체에서 모든 데이터베이스를 끌고 와서 article이라는 변수에 저장해라 
 
    context = {
        'articles':articles, #articles 데이터를 context사전에 담고 
    }

    return render(request, 'index.html', context) #html이라는 요리책을 바탕으로 context라는 원재료를 활용하여 렌더링 

def detail(request, id): #한 게시물을 나타내는 거니까 id가 또 필요함 

    article = Article.objects.get(id=id) #Article 객채의 데이터베이스 중에서 요청하는 id를 끌어오기
    
    form = CommentForm() 
    #CommentForm은 댓글을 작성하기 위한 폼을 정의하는 Django 폼 클래스.


    comments = Comment.objects.filter(article_id=id)


    context = {
        'article': article,
        'form':form,
        'comments':comments,
    }

    return render(request, 'detail.html', context)

def create(request):
    if request.method == 'POST':

        form = ArticleForm(request.POST)

        if form.is_valid():

            article = form.save()

            return redirect('articles:detail', id = article.id)
    else:
        form = ArticleForm()

    context = {
        'form':form,
    }

    return render(request, 'form.html', context)

def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            
            #1.객체를 저장하는 방법 
            #article = Article.objects.get(id=article_id)
            #comment.article = article
            #comment.save
            
            #2. 숫자를 integer를 저장하는 방법 
            comment.article_id = article_id
            comment.save() 


            return redirect('articles:detail', id=article_id)

    else: 
        return redirect('articles:index')
    
def comment_delete(request, article_id, id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=id)
        comment.delete()

        return redirect('articles:detail', id = article_id)