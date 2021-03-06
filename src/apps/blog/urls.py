from django.conf.urls import include
from django.urls import path

from apps.blog import views
from apps.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path("all_posts/", views.AllBlogPostsView.as_view(), name="all_posts"),
    path("posts/<int:pk>/", views.BlogPostView.as_view(), name="post"),
    path("posts/<int:pk>/comment/", views.CommentView.as_view(), name="comment"),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]
