from rest_framework.viewsets import ModelViewSet
from films.models import Media, MediaViews
from films.api.serializers import Mediaserializer,MediaViewSerializer

class MediaApiViewSet(ModelViewSet):
    serializer_class=Mediaserializer
    queryset=Media.objects.all()

class MediaViewsApiViewSet(ModelViewSet):
    serializer_class=MediaViewSerializer
    queryset=MediaViews.objects.all()