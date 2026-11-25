from django.urls import path
from . import views
app_name = "reservas"
urlpatterns = [
path("", views.lista, name="lista"),
path("espacios/<int:pk>/", views.detalle, name="detalle"),
]

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from reservas.api import EspacioViewSet, ReservaViewSet
router = DefaultRouter()
router.register("espacios", EspacioViewSet, basename="espacio")
router.register("reservas", ReservaViewSet, basename="reserva")
urlpatterns = [
path("admin/", admin.site.urls),
path("cuentas/", include("django.contrib.auth.urls")),
path("api/", include(router.urls)),
path("api-auth/", include("rest_framework.urls")),
path("", include("reservas.urls")),
]