from rest_framework_nested import routers
from django.urls import include, path
from .views import PostViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet, basename='posts')

posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(posts_router.urls)),
]