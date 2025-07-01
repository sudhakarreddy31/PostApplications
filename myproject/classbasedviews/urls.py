from django.urls import path
from . import views

urlpatterns = [
    path('cbvlists/', views.CBVListView.as_view(), name='cbv_list'),
    path('create/', views.CBVCreateView.as_view(), name='cbv_create'),
    path('<int:pk>/', views.CBVDetailView.as_view(), name='cbv_detail'),
    path('<int:pk>/update/', views.CBVUpdateView.as_view(), name='cbv_update'),
    path('<int:pk>/delete/', views.CBVDeleteView.as_view(), name='cbv_delete'),
]
