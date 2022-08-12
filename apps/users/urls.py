from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.users import views


urlpatterns = [
    path('users/', views.UserListApiView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
    path('', views.Login.as_view(), name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)