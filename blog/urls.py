from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('cv/', views.cv_home, name='cv_home'),
    path('cv/edit_cv/', views.edit_cv, name='edit_cv'),
    path('cv/<int:pk>/edit_experience', views.edit_experience, name='edit_experience'),
    path('cv/new_experience', views.new_experience, name='new_experience'),
    path('cv/<pk>/remove/', views.remove_experience, name='remove_experience'),
]


