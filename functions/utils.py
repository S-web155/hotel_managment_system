"""Utility functions that use the price data from `database/price.py`.

Notes on imports:
- When running scripts from the project root (where `main.py` sits), the
  `database` package will be importable because we added an `__init__.py`
  under `database/`.
"""

# Import the price dict directly for simpler access. This assumes the
# project is executed from the repository root (so the parent directory of
# `database/` is on sys.path). If you run modules differently, see notes
# below about package execution.
from database import price



hotel_rooms = {}


def add_room(room_type: str, room_number: str | int, default_price: float | None = None):
    """Add a room using the price lookup from `database.price`.

    If the room_type isn't found in the price map, `default_price` is used
    (if provided) or 0.0.
    """
    key = str(room_number)
    p = price.get(room_type)
    if p is None:
        if default_price is not None:
            p = float(default_price)
        else:
            p = 0.0

    hotel_rooms[key] = {
        'type': room_type,
        'price': float(p),
        'booked': False,
        'guest': None,
        'check_in_time': None,
        'check_out_time': None,
    }


def book_room(room_number, name, check_in_time, check_out_time):
    """Book a room; raises ValueError if the room doesn't exist."""
    key = str(room_number)
    if key in hotel_rooms:
        hotel_rooms[key]['booked'] = True
        hotel_rooms[key]['guest'] = name
        hotel_rooms[key]['check_in_time'] = check_in_time
        hotel_rooms[key]['check_out_time'] = check_out_time
    else:
        raise ValueError("Room number does not exist.")


def display_rooms(room_number):
    """Return room details or raise ValueError if not found."""
    key = str(room_number)
    if key in hotel_rooms:
        return hotel_rooms[key]
    raise ValueError("Room number does not exist.")


def list_available_rooms():
    """Return a list of (room_number, details) for rooms not booked."""
    return [(rn, det) for rn, det in hotel_rooms.items() if not det['booked']]



if __name__ == '__main__':
    # Example usage guarded so importing this module doesn't execute it.
    add_room('single', 101)
    add_room('double', 102)
    book_room(101, 'Alice', '2024-07-01', '2024-07-05')
    print(display_rooms(101))
    print(list_available_rooms())
