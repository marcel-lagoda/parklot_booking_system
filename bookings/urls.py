from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('update/<int:pk>/', views.UpdateRezView.as_view(), name='update'),
    path('booking/<int:pk>/', views.DetailRezView.as_view(), name='booking'),
]
