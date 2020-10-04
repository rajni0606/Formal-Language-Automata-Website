from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [ path('', views.index , name="index"),
                path('home.html', views.home , name="home.html"),
                path('add',views.add,name="add"),
                path('grammar.html',views.grammar,name="grammar.html"),
                path('grammar',views.grammar,name="grammar")]
urlpatterns += staticfiles_urlpatterns()