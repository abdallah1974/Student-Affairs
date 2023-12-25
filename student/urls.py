from django.urls import path
from django.contrib import admin
from . import views
from student.views import add_student

urlpatterns = [
    #path('get_data/', views.get_data,name='get_data'),
    path('admin/', admin.site.urls),
    path('add_student/', views.add_student, name = 'add_student'),
]