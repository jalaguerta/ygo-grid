from django.urls import path
from .views import test_view, ValidateCardAPIView, autocomplete_cards


urlpatterns = [
    path('validate-card/', ValidateCardAPIView.as_view(), name='validate_card'),
    path('autocomplete/', autocomplete_cards, name='autocomplete_cards'),
    path('test-view/', test_view, name='test_view'),
]
