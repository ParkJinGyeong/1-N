from django.urls import path
from .import views

app_name = 'articles'

#articles는 Django 애플리케이션의 이름을 의미. 
#Django에서 URL 패턴을 정의할 때, URL을 식별하기 위해 이름을 붙일 수 있음. 
#app_name = 'articles'는 이 애플리케이션의 이름을 articles로 지정. 
#그런 다음 URL 패턴에 name='index'와 name='create'를 사용하여 각 URL에 이름을 붙임
# --> 이게 html의 url 패턴에도 쓰이는데, 
#템플릿에서 {% url 'articles:index' %}와 
#{% url 'articles:create' %}를 사용하여 해당 URL을 참조할 수 있습니다. 
#첫 번째 링크는 index 뷰로, 두 번째 링크는 create 뷰로 연결됩니다. 
#articles:index와 articles:create는 articles 애플리케이션의 index 및 create URL 패턴을 나타냅니다.





urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name = 'detail'),
    path('create/', views.create, name='create'),
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:article_id>/comments/<int:id>/delete', views.comment_delete, name ='comment_delete'),
    
]