from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('works', views.WorkViewSet)
router.register('artists', views.ArtistViewSet)
router.register('register', views.RegistrationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
