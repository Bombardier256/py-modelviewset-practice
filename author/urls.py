from rest_framework import routers
from django.urls import path, include
from .views import AuthorViewSet


router = routers.DefaultRouter()
router.register("", AuthorViewSet)

urlpatterns = [
    path("authors/", include(router.urls)),
]

app_name = "author"
