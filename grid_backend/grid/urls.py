from django.urls import path
from .views import test_view, autocomplete_cards, ValidateCardAPIView

urlpatterns = [
    path('test-view/', test_view, name='test_view'),
    path('autocomplete/', autocomplete_cards, name='autocomplete_cards'),
    path('validate-card/', ValidateCardAPIView.as_view(), name='validate_card'),
]
