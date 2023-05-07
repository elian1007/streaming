from rest_framework.routers import DefaultRouter
from films.api.views import MediaApiViewSet,MediaViewsApiViewSet,MediaRatingAPiViewSet, MediaRandomApiViewSet,MediaOrderApiViewSet, MediaFilterApiViewSet

router_media=DefaultRouter()
router_mediaviews=DefaultRouter()
router_mediarating=DefaultRouter()
router_mediarandom=DefaultRouter()
router_mediaorder=DefaultRouter()
router_mediafilter=DefaultRouter()



router_media.register(prefix='films',basename='films',viewset=MediaApiViewSet)

router_mediaviews.register(prefix='films',basename='films',viewset=MediaViewsApiViewSet)

router_mediarating.register(prefix='films',basename='films',viewset=MediaRatingAPiViewSet)

router_mediarandom.register(prefix='films',basename='films',viewset=MediaRandomApiViewSet)

router_mediaorder.register(prefix='films',basename='films',viewset=MediaOrderApiViewSet)

router_mediafilter.register(prefix='films',basename='films',viewset=MediaFilterApiViewSet)

