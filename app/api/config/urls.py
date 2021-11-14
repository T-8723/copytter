from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token  # 追加
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView  # 追加
from .views import index

urlpatterns = [
    path('auth/', obtain_jwt_token),
    path('accounts/', include('allauth.urls')),  # 追加
    path('api/', include('copytter.urls')),  # APIへのルーティング
    path('', index, name='index'),  # vueシングルページアプリへのルーティング
] + static(settings.STATIC_URL) + static(r'^media/(?P<path>.*)$', document_root=settings.MEDIA_ROOT)  # staticディレクトリにルーティング


if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
        path(
            'api/schema/',
            SpectacularAPIView.as_view(),
            name='schema'),
        path(
            'api/schema/swagger-ui/',
            SpectacularSwaggerView.as_view(
                url_name='schema'),
            name='swagger-ui'),
        path(
            'api/schema/redoc/',
            SpectacularRedocView.as_view(
                url_name='schema'),
            name='redoc'),
    ]
