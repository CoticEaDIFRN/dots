from django.contrib import admin
# from django.urls import path, include
from django.conf.urls import url, include

from dots.entrypoints import router

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/v1', include((router.urls, 'app_name'))),
    # url(r'^api/auth/', include('rest_framework.urls'))
]
