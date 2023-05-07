from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class Media(models.Model):
        name=models.CharField(max_length=50,blank=True,null=True)
        genre=models.CharField(max_length=25, null=False)
        type=models.CharField(max_length=30, null=False)

        


class MediaViews(models.Model):
        userId=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
        mediaId=models.ForeignKey(Media,on_delete=models.CASCADE)


# class MediaRating(models.Model):
#         userId=models.ForeignKey('')
#         mediaId=models.ForeignKey('')
#         rate=models.IntegerField('') 


# codigo_departamento = models.ForeignKey('Departamentos', models.DO_NOTHING, db_column='codigo_departamento', blank=True, null=True)







