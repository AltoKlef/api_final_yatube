from rest_framework_nested import routers
from django.urls import include, path
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'follow', FollowViewSet, basename='follow')

posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(posts_router.urls)),
]