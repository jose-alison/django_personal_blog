from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('new/', views.user_create_view, name='create'),
    path('', views.user_list_view, name='list'),
    path('<int:pk>/detail/', views.user_detail_view, name='detail'),
    path('<int:pk>/update/', views.user_update_view, name='update'),
    path('<int:pk>/delete/', views.user_delete_view, name='delete'),
]
