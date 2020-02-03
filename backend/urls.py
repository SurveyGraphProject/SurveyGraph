from django.urls import include, path
from rest_framework import routers
from backend.quickstart import views
from backend.api_dev import views

router = routers.DefaultRouter()

router.register(r'api_dev', views.ArticleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
