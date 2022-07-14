from django.urls import path
from . import views
from .views import HomeView, DetailPostView, AddPostView, EditPostView, DeletePostView, CategoryView, LikeView, \
    AddCommentView, AddCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<slug>/', DetailPostView.as_view(), name='detail-post'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>/', EditPostView.as_view(), name='edit-post'),
    path('article/delete/<int:pk>/', DeletePostView.as_view(), name='delete-post'),
    path('categories/<str:cats>/', CategoryView, name='categories'),
    path('like/<int:pk>/', LikeView, name='like-post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),
]
