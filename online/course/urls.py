from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course_details_bootstrap/', views.course_details_bootstrap, name='course_details_bootstrap'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('submit/', views.submit, name='submit'),
    path('result/', views.show_exam_result, name='show_result'),
]