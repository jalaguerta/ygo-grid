from .models import Card

def validate_guess(card_name, criteria):
    """
    Validates the card guess based on dynamic criteria.

    :param card_name: Name of the card to validate
    :param criteria: Dictionary of criteria (e.g., {"atk__gte": 3000, "type": "Normal Monster"})
    :return: Dictionary with success status and card or error message
    """
    if not card_name:
        return {"success": False, "error": "Card name is required."}
    if not criteria:
        return {"success": False, "error": "Criteria are required."}

    # Build the query filters
    filters = {"name": card_name}
    filters.update(criteria)

    try:
        card = Card.objects.get(**filters)
        return {"success": True, "card": card}
    except Card.DoesNotExist:
        return {"success": False, "error": "No matching card found."}
