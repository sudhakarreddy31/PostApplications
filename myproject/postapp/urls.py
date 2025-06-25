from django.urls import path
from postapp import views


urlpatterns = [
    path('home',views.home, name='home'),
    path('lists',views.post_lists, name='lists'),
    path('<slug:slug>/',views.post_detail, name='detail'),
    
]
