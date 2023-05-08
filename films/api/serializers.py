from rest_framework.serializers import ModelSerializer
from films.models import Media,MediaViews,MediaRating
from rest_framework.fields import SerializerMethodField

class MediaViewSerializer(ModelSerializer):
    class Meta:
        model= MediaViews
        fields=['id','userId','mediaId']

class Mediaserializer(ModelSerializer):
    views =SerializerMethodField()
    class Meta:
        model = Media
        fields=['id','name','genre','type','views']

    def get_views(media,item):
        return MediaViews.objects.filter(
            mediaId__id=item.id).count()

class MediaRatingSerializer(ModelSerializer):
    class Meta:
        model=MediaRating
        fields=['userId','mediaId','rate']

class MediaRandomSerializer(ModelSerializer):
    class Meta:
        model=Media
        fields=['userId','mediaId','rate']

