from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='main'),
    path('registration/', views.create, name = 'create'),
    path('appointment/', views.appointment, name = 'appointment'),
    path('blog/<str:pk>/', views.blog, name = 'blog'),
    path('update_comment/<str:pk>/', views.updateComment, name="update_comment"),
    path('delete_comment/<str:pk>/', views.deleteComment, name="delete_comment"),
    # path('delete_comment/', views.DeleteCommentView, name = 'blog')

]