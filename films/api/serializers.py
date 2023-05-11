from rest_framework.serializers import ModelSerializer
from films.models import Media,MediaViews,MediaRating
from rest_framework.fields import SerializerMethodField
from django.db.models import Avg
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers


class MediaViewSerializer(ModelSerializer):
    userId = serializers.HiddenField(
    default=serializers.CurrentUserDefault())
    class Meta:
        model= MediaViews
        fields = ['userId','mediaId']
        validators = [
            
            UniqueTogetherValidator(
                queryset=MediaViews.objects.all(),
                fields=['userId', 'mediaId']
            )
        ]


class Mediaserializer(ModelSerializer):
    views =SerializerMethodField()
    average = SerializerMethodField()
    
    class Meta:
        model = Media
        fields=['id','name','genre','type','views','average']

    def get_views(media,item):
        return MediaViews.objects.filter(
            mediaId__id=item.id).count()
    
    def get_average(media,item):
        rating=MediaRating.objects.filter(
            mediaId__id=item.id)
        stars_average = rating.aggregate(Avg('rate'))["rate__avg"]
        return stars_average
    

class MediaRatingSerializer(ModelSerializer):
    userId = serializers.HiddenField(
    default=serializers.CurrentUserDefault())
    class Meta:
        model=MediaRating
        fields=['userId','mediaId','rate']                
        validators = [
            UniqueTogetherValidator(
                queryset=MediaRating.objects.all(),
                fields=['userId', 'mediaId']
            )
        ]

class MediaRandomSerializer(ModelSerializer):
    class Meta:
        model=Media
        fields=['userId','mediaId','rate']

