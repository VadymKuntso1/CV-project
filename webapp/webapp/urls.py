from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls') ),
    path('dbproject/',include('dbproject.urls')),
    path('telegram/',include('telegram.urls')),
    path('parsing/',include('parsing.urls')),
    path('camera/', include('camera.urls'))
]
