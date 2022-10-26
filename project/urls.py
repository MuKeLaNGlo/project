from django.urls import include, path
from django.contrib import admin
# from core import views


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
