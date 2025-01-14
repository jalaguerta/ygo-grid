from django.urls import path
from .views import test_view, ValidateCardAPIView

urlpatterns = [
    path('validate-card/', ValidateCardAPIView.as_view(), name='validate_card'),
    path('test-view/', test_view, name='test_view'),
]
