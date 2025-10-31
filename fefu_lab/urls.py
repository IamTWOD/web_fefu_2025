from django.urls import path
from . import views

urlpatterns = [
    # Существующие маршруты из лабораторной №1
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('student/<int:student_id>/', views.student_profile, name='student_detail'),
    path('course/<slug:course_slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    
    # Новые маршруты для лабораторной №2
    path('feedback/', views.feedback_view, name='feedback'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),  # ← ДОБАВЬТЕ ЭТУ СТРОЧКУ
]