from django.urls import path
from .views import (
    predict_view_2
)

urlpatterns = [
    path('predict-v2/', predict_view_2),
]