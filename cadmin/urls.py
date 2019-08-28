"""cadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
# 导入辅助函数get_schema_view
# from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token

from apps.app01 import views

# 导入两个类
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
# 利用辅助函数引入所导入的两个类
# schema_view = get_schema_view(title='API', renderer_classes=[SwaggerUIRenderer, OpenAPIRenderer])


schema_view = get_schema_view(
    openapi.Info(
        title="微课接口文档",
        default_version='v1',
        description="项目接口注释、接口功能详细描述",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.index, name='task'),
    path('search/', include('haystack.urls')),
    path('m/', views.multy, name='multy'),
    path('admin/', admin.site.urls),
    path('api/sliders/', include('apps.app01.restful.urls', namespace='customer')),
    path('api-token-auth/', obtain_jwt_token),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=100), name='schema-redoc'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=100), name='schema-swagger-ui'),
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
