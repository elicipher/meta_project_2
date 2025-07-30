from django.urls import path , re_path
from .views import BlogView, PostDetailView ,LikePostView , CommentReplyView

app_name ='blog'
urlpatterns = [
    path('blog/',BlogView.as_view(), name='blog'),
    re_path(r'^post-detail/(?P<slug>[-\wآ-ی]+)/(?P<id>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    re_path(r'^like/(?P<slug>[-\wآ-ی]+)/(?P<id>\d+)/$', LikePostView.as_view(), name='post_like'),
    path('reply/<int:post_id>/<int:comment_id>/' , CommentReplyView.as_view() , name="reply_comment")

   
]
