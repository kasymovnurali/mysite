
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('ToDo/<int:pk>/', views.detail, name='detail'),
	path('ToDo/new/', views.new, name='new'),
	path('ToDo/<int:pk>/edit>', views.edit, name='edit'),
]