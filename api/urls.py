from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import (
    predict_view_2
)

urlpatterns = [
    # Schema YAML/JSON
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('predict-v2/', predict_view_2),
]