from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='homepage'),
    path('about', views.about, name='about'),
    path('message', views.message, name='message'),
    path('table', views.table, name='table'),
path('change', views.switcher, name='change')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
