import json
from pathlib import Path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Card
from .utils import validate_guess

from django.http import JsonResponse

def autocomplete_cards(request):
    query = request.GET.get('q', '')  # Get the query string from the request
    if query:
        # Query the database for cards with names that match the query
        cards = Card.objects.filter(name__icontains=query).values_list('name', flat=True)[:10]
        return JsonResponse(list(cards), safe=False)  # Return the list of names as JSON
    return JsonResponse([], safe=False)  # Return an empty list if no query provided

def test_view(request):
    return JsonResponse({"message": "Test view is working!"})


class ValidateCardAPIView(APIView):
    
    def post(self, request):
        # Print the raw request data for debugging
        print("Raw Request Data:", request.data)

        # Get the card name from the request
        card_name = request.data.get("name")
        criteria = request.data.get("criteria", {})

        # Print extracted data
        print("Card Name:", card_name)
        print("Criteria Rule:", criteria)

        # Validate the guess using the criteria
        result = validate_guess(card_name, criteria)

        # Print the validation result
        print("Validation Result:", result)

        if result["success"]:
            card = result["card"]
            # Print card details for successful validation
            print("Valid Card Found:", card.name, "-", card.description)
            return Response({
                "message": "Valid guess!",
                "card_name": card.name,
                "card_desc": card.description
            }, status=status.HTTP_200_OK)
        else:
            # Print the error message for failed validation
            print("Validation Failed:", result["error"])
            return Response({"message": result["error"]}, status=status.HTTP_404_NOT_FOUND)
