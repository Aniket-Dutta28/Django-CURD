from django.urls import path
from . import views
urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('create/',views.create_post,name='create_post'),
    path('<int:post_id>/update/',views.update_post,name='update_post'),
    path('<int:post_id>/delete/',views.post_delete,name='post_delete'),
]
