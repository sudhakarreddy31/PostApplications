from django.urls import  path
from dynamicforms import views

urlpatterns = [
    path('form',views.dynamic_form,name='formsdata'),

]
