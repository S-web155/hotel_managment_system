room_price = {
    'single': 500,
    'double': 900,
    'suite': 1500,
    'deluxe': 2500,
}

def get(room_type: str) -> int | None:
    """Get the price for a given room type, or None if not found."""
    return room_price.get(room_type)
