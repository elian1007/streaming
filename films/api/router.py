from rest_framework.routers import DefaultRouter
from films.api.views import MediaApiViewSet,MediaViewsApiViewSet

router_posts=DefaultRouter()
router_post=DefaultRouter()

router_posts.register(prefix='films',basename='films',viewset=MediaApiViewSet)

router_post.register(prefix='films',basename='films',viewset=MediaViewsApiViewSet)
