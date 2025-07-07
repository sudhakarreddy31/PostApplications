from django.urls import path

from fbvapis import views


urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('student_creation/', views.student_create, name='student_create'),
    path('student_detailaton/<int:pk>', views.student_detail, name='student_detail'),
    path('student_updation/<int:pk>', views.student_update, name='student_update'),
    path('student_delation/<int:pk>', views.student_delete, name='student_delete'),
    



]