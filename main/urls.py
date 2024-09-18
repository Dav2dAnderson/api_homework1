from django.urls import path

from .views import CarAPIView, CarDetailsAPIView


urlpatterns = [
    path('api/v1/', CarAPIView.as_view()),
    path('api/v1/<int:pk>/', CarDetailsAPIView.as_view())
]

