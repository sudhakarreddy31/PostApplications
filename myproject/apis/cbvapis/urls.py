from django .urls import path
from apis.cbvapis import views

urlpatterns = [
    path('familymembers/', views.FamilyMemberLists.as_view(), name='family_member_list'),
    path('familymembers/<int:pk>/', views.FamilyMemberDetail.as_view(), name='family_member_detail'),

]