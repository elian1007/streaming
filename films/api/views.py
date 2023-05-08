from rest_framework.viewsets import ModelViewSet
from films.models import Media, MediaViews,MediaRating
import random
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.forms.models import model_to_dict
from films.api.serializers import Mediaserializer,MediaViewSerializer,MediaRatingSerializer

class MediaApiViewSet(ModelViewSet):
    serializer_class=Mediaserializer
    queryset=Media.objects.all()


class MediaViewsApiViewSet(ModelViewSet):
    serializer_class=MediaViewSerializer
    queryset=MediaViews.objects.all()

    # falta validad una unica visualizacion 

class MediaRatingAPiViewSet(ModelViewSet):
    serializer_class=MediaRatingSerializer
    queryset=MediaRating.objects.all()

class MediaRandomApiViewSet(ModelViewSet):
    serializer_class=Mediaserializer
    
    def get_queryset(self):
        items = list(Media.objects.all())
        random_item = random.choice(items)
        random_dict=model_to_dict(random_item)
        return Media.objects.filter(id=random_dict['id'])

class MediaOrderApiViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = Mediaserializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

class MediaFilterApiViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = Mediaserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'




