# enrollment/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollment, name='enrollment'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('success/', views.success, name='success'),
]
