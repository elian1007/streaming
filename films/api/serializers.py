from rest_framework.serializers import ModelSerializer
from films.models import Media,MediaViews

class Mediaserializer(ModelSerializer):
    class Meta:
        model = Media
        fields=['id','name','genre','type']

class MediaViewSerializer(ModelSerializer):
    class Meta:
        model= MediaViews
        fields=['id','userId','mediaId']