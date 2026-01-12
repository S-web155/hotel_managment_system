from colorama import init, Fore, Style

ROOM_TYPES = {
    "1": "single",
    "2": "double", 
    "3": "suite",
    "4": "deluxe"
}

def show_menu():
    print(Fore.GREEN + "Please select an option:")
    print(Fore.MAGENTA + "1. Add a Room")
    print(Fore.BLUE + "2. Book a Room")
    print(Fore.RED + "3. Display room Details")
    print(Fore.CYAN + "4. List available Rooms")
    print(Fore.YELLOW + "5. Exit" + Style.RESET_ALL)


def show_room():
    print(Fore.GREEN + "Please select a Room:")
    print(Fore.MAGENTA + "1. Single")
    print(Fore.BLUE + "2. Double")
    print(Fore.RED + "3. Suite")
    print(Fore.CYAN + "4. Deluxe")




def main():
    print_intro()
    from functions.utils import add_room, book_room, display_rooms, list_available_rooms, hotel_rooms
    # Run until the user explicitly exits.
    try:
        while True:
            show_menu()
            operation = input(Fore.CYAN + "Enter your choice (1-5): " + Style.RESET_ALL)
            if operation == "5":
                print("Exiting.")
                break

            if operation == "1":
                show_room()
                choice = input(" Enter your choice(1-4): ")
                room_number = input(" Enter room number:").strip()
                if room_number in hotel_rooms:
                    print("Room number already exists.")
                    continue

                room_type = ROOM_TYPES.get(choice)
                if room_type is None:
                    print("Invalid choice.")
                    continue

                add_room(room_type, room_number)
                continue

            if operation == "2":
                room_number = input("Enter room number to book: ").strip()
                if room_number not in hotel_rooms:
                    print("Room number does not exist.")
                elif hotel_rooms[room_number]['booked']:
                    print("Room is already booked.")
                else:
                    name = input("Enter guest name: ").strip()
                    nights_in = input("Enter number of nights (press Enter for 1): ").strip()
                    nights = 1
                    if nights_in:
                        try:
                            nights = int(nights_in)
                            if nights <= 0:
                                print("Number of nights must be at least 1. Using 1.")
                                nights = 1
                        except ValueError:
                            print("Invalid number entered; using 1 night.")
                            nights = 1
                    book_room(room_number, name, nights)
                continue

            if operation == "3":
                room_number = input("Enter room number to display: ").strip()
                try:
                    details = display_rooms(room_number)
                    print(f"\nRoom {room_number} details:")
                    print(f"  Type: {details.get('type')}")
                    print(f"  Price: {details.get('price')}")
                    print(f"  Status: {'Booked' if details.get('booked') else 'Available'}")
                    guest = details.get('guest')
                    if guest:
                        print(f"  Guest: {guest}")
                        print(f"  Check-in: {details.get('check_in_time')}")
                        print(f"  Check-out: {details.get('check_out_time')}")
                    else:
                        print("  Guest: -")
                except ValueError as e:
                    print(e)
                continue

            if operation == "4":
                available_rooms = list_available_rooms()
                if not available_rooms:
                    print("No available rooms.")
                else:
                    print("Available rooms:")
                    for rn, det in available_rooms:
                        print(f"Room {rn}: type={det.get('type')}, price={det.get('price')}")
                continue

            print("Invalid operation. Valid: add, book, display, list, exit")
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")

def print_intro():
    init(autoreset=True)
    print(Fore.CYAN + r"""
 _   _       _        _     __  __                                 
| | | | ___ | |_ __ _| |   |  \/  | __ _ _ __   __ _  ___ _ __    
| |_| |/ _ \| __/ _` | |   | |\/| |/ _` | '_ \ / _` |/ _ \ '__|   
|  _  | (_) | || (_| | |   | |  | | (_| | | | | (_| |  __/ |      
|_| |_|\___/ \__\__,_|_|   |_|  |_|\__,_|_| |_|\__, |\___|_|      
                                               |___/              
    """)
    print(Fore.YELLOW + "Welcome to the Hotel Manager Terminal Interface!\n" + Style.RESET_ALL)




if __name__ == "__main__":
    main()
