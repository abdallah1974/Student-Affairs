from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_of_all,name='first_of_all'),
    path('home/', views.home_page, name='home_page'),
    path('signin/', views.sign_in, name='sign_in'),
    path('signinforupdate/', views.sign_in_for_update, name = 'sign_in_for_update'),
    path('search_activity/', views.search_activity, name='search_activity'),
    path('allstatus/', views.all_status, name='all_status'),
    path('update_info/<int:id>/<str:email>/', views.update_info, name='update_info'),
    path('search', views.search, name="search"),
    path('update_status/', views.update_status, name='update_status'),
    path('remove_student/<int:student_id>/', views.remove_student, name='remove_student'),
]