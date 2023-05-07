from django.contrib import admin

from films.models import Media,MediaViews , MediaRating

# Register your models here.
admin.site.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display={'name','genre','type'}
    
admin.site.register(MediaViews)
class MediaViewsAdmin(admin.ModelAdmin):
    list_display={'id','userId','mediaId'}

admin.site.register(MediaRating)
class MediaRatingAdmin(admin.ModelAdmin):
    list_display={'id','userId','mediaId','rate'}
# admin.site.register(InventariosItems)
# admin.site.register(Ciudades)
