def main():
    from functions.utils import add_room, book_room, display_rooms, list_available_rooms, hotel_rooms
    # Run until the user explicitly exits.
    try:
        while True:
            operation = input("Enter operation (add, book, display, list, exit): ").strip().lower()
            if operation == "exit" or operation == "quit":
                print("Exiting.")
                break

            if operation == "add":
                room_type = input("Enter room type (single, double, suite, deluxe): ").strip()
                room_number = input("Enter room number: ").strip()
                add_room(room_type, room_number)
                continue

            if operation == "book":
                room_number = input("Enter room number to book: ").strip()
                if room_number not in hotel_rooms:
                    print("Room number does not exist.")
                else:
                    name = input("Enter guest name: ").strip()
                    check_in_time = input("Enter check-in time (YYYY-MM-DD): ").strip()
                    check_out_time = input("Enter check-out time (YYYY-MM-DD): ").strip()
                    book_room(room_number, name, check_in_time, check_out_time)
                continue

            if operation == "display":
                room_number = input("Enter room number to display: ").strip()
                try:
                    details = display_rooms(room_number)
                    print(f"Room {room_number} details: {details}")
                except ValueError as e:
                    print(e)
                continue

            if operation == "list":
                available_rooms = list_available_rooms()
                if not available_rooms:
                    print("No available rooms.")
                else:
                    print("Available rooms:")
                    for rn, det in available_rooms:
                        print(f"Room {rn}: {det}")
                continue

            print("Invalid operation. Valid: add, book, display, list, exit")
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")

if __name__ == "__main__":
    main()