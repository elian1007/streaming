from django.urls import path
from . import views
# importar imagenes
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.login ,name="login"),

]
