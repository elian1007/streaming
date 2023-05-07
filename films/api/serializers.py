from rest_framework.serializers import ModelSerializer
from films.models import Media,MediaViews,MediaRating

class Mediaserializer(ModelSerializer):
    class Meta:
        model = Media
        fields=['id','name','genre','type']

class MediaViewSerializer(ModelSerializer):
    class Meta:
        model= MediaViews
        fields=['id','userId','mediaId']

class MediaRatingSerializer(ModelSerializer):
    class Meta:
        model=MediaRating
        fields=['userId','mediaId','rate']

class MediaRandomSerializer(ModelSerializer):
    class Meta:
        model=Media
        fields=['userId','mediaId','rate']
