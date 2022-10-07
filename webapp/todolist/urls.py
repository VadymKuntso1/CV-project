from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('', views.index, name='index'),
    path('exit',views.unlogin, name='exit')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
