from django.urls import path
from . import views
# importar imagenes
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.login ,name="authentication"),

]
urlpatterns = [
    # path('',views.VRegistro.as_view() ,name="authentication"),
    # path('cerrar_sesion',views.cerrar_sesion ,name="cerrar_sesion"),
    path('',views.login ,name="login"),
]