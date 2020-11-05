from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('people/', include('people.urls')),
    path('', include('webpage.urls')),
    path('admin/', admin.site.urls),
]
