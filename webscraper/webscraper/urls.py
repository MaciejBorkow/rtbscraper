from django.urls import include, path
from rest_framework import routers
from scraper import views

router = routers.DefaultRouter()
router.register(r'scrapped_url', views.ScrappedUrlViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
