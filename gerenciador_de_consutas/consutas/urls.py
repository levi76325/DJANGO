from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, cadastro
from rest_framework import routers
from .api.viewsets import ConsutaViewSet

router = routers.DefaultRouter()
router.register(r'cat_filmes', ConsutaViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('api_consutas', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

