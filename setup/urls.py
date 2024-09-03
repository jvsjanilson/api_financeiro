"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ContatoViewSet, FormapagamentoViewSet, ContaViewSet, UserViewSet
from financeiro.views import ReceberViewSet, PagarViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import HttpResponseRedirect
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register("contatos", ContatoViewSet)
router.register("formapagamentos", FormapagamentoViewSet)
router.register("contas", ContaViewSet)
router.register("recebers", ReceberViewSet)
router.register("pagars", PagarViewSet, basename="pagar")


schema_view = get_schema_view(
    openapi.Info(
        title="Financeiro API",
        default_version="v1",
        description="API para controle financeiro",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="janilsonjvs@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
    path("auth/", include("rest_framework.urls")),
    path("api/user/me/", UserViewSet.as_view(), name="user_me"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("", lambda request: HttpResponseRedirect("/api/")),
]
