from types import NoneType
from colorama import init, Fore, Style

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
    print(Fore.YELLOW + "5. Exit" + Style.RESET_ALL)




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
                choice = input("Enter your choice(1-4): ")
                room_type = None
                room_number = input(" Enter room number:").strip()

                if choice == 1:
                    room_type = 'single'
                elif choice == 2:
                    room_type = 'double'
                elif choice == 3:
                    room_type = 'suite'
                elif choice == 4:
                    room_type = 'deluxe'

                add_room(room_type, room_number)
                continue

            if operation == "2":
                room_number = input("Enter room number to book: ").strip()
                if room_number not in hotel_rooms:
                    print("Room number does not exist.")
                else:
                    name = input("Enter guest name: ").strip()
                    check_in_time = input("Enter check-in time (YYYY-MM-DD): ").strip()
                    check_out_time = input("Enter check-out time (YYYY-MM-DD): ").strip()
                    book_room(room_number, name, check_in_time, check_out_time)
                continue

            if operation == "3":
                room_number = input("Enter room number to display: ").strip()
                try:
                    details = display_rooms(room_number)
                    print(f"Room {room_number} details: {details}")
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
                        print(f"Room {rn}: {det}")
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
