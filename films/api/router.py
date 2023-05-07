from rest_framework.routers import DefaultRouter
from rest_framework import routers

from films.api.views import MediaApiViewSet,MediaViewsApiViewSet,MediaRatingAPiViewSet, MediaRandomApiViewSet,MediaOrderApiViewSet, MediaFilterApiViewSet

router_media=DefaultRouter()
# router_mediaviews=DefaultRouter()
# router_mediarating=DefaultRouter()
# router_mediarandom=DefaultRouter()
# router_mediaorder=DefaultRouter()
# router_mediafilter=DefaultRouter()



router_media.register(prefix='media',basename='media',viewset=MediaApiViewSet)

router_media.register(prefix='mediaview',basename='mediaview',viewset=MediaViewsApiViewSet)

router_media.register(prefix='mediarating',basename='mediarating',viewset=MediaRatingAPiViewSet)

router_media.register(prefix='mediarandom',basename='mediarandom',viewset=MediaRandomApiViewSet)

router_media.register(prefix='mediaorder',basename='mediaorder',viewset=MediaOrderApiViewSet)

router_media.register(prefix='mediafilter',basename='mediafilter',viewset=MediaFilterApiViewSet)

