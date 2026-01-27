from colorama import init, Fore, Style

ROOM_TYPES = {
    "1": "single",
    "2": "double", 
    "3": "suite",
    "4": "deluxe"
}

def print_header(title):
    print(Fore.CYAN + "=" * 60)
    print(title.center(60))
    print("=" * 60 + Style.RESET_ALL)

def print_separator():
    print(Fore.CYAN + "-" * 60 + Style.RESET_ALL)

def show_menu():
    print("\n" + Fore.GREEN + "=" * 60)
    print("MAIN MENU")
    print("=" * 60 + Style.RESET_ALL)
    print(Fore.MAGENTA + "1. Add a Room" + Style.RESET_ALL)
    print(Fore.BLUE + "2. Book a Room" + Style.RESET_ALL)
    print(Fore.RED + "3. Display Room Details" + Style.RESET_ALL)
    print(Fore.CYAN + "4. List Available Rooms" + Style.RESET_ALL)
    print(Fore.YELLOW + "5. Exit" + Style.RESET_ALL)
    print(Fore.GREEN + "-" * 60 + Style.RESET_ALL)


def show_room():
    print("\n" + Fore.GREEN + "=" * 60)
    print("SELECT A ROOM TYPE")
    print("=" * 60 + Style.RESET_ALL)
    print(Fore.MAGENTA + "1. Single" + Style.RESET_ALL)
    print(Fore.BLUE + "2. Double" + Style.RESET_ALL)
    print(Fore.RED + "3. Suite" + Style.RESET_ALL)
    print(Fore.CYAN + "4. Deluxe" + Style.RESET_ALL)
    print(Fore.GREEN + "-" * 60 + Style.RESET_ALL)




def main():
    print_intro()
    from functions.utils import add_room, book_room, display_rooms, list_available_rooms, hotel_rooms
    try:
        while True:
            show_menu()
            operation = input(Fore.CYAN + "Enter your choice (1-5): " + Style.RESET_ALL)
            
            if operation == "5":
                print("\n" + Fore.YELLOW + "=" * 60)
                print("Thank you for using Hotel Manager!")
                print("=" * 60 + Style.RESET_ALL)
                break

            if operation == "1":
                show_room()
                choice = input(Fore.CYAN + "Enter your choice (1-4): " + Style.RESET_ALL)
                room_number = input(Fore.CYAN + "Enter room number: " + Style.RESET_ALL).strip()
                
                if room_number in hotel_rooms:
                    print(Fore.RED + "Room number already exists." + Style.RESET_ALL)
                    continue

                room_type = ROOM_TYPES.get(choice)
                if room_type is None:
                    print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
                    continue

                add_room(room_type, room_number)
                print(Fore.GREEN + "Room added successfully!" + Style.RESET_ALL)
                continue

            if operation == "2":
                print_separator()
                room_number = input(Fore.CYAN + "Enter room number to book: " + Style.RESET_ALL).strip()
                
                if room_number not in hotel_rooms:
                    print(Fore.RED + "Room number does not exist." + Style.RESET_ALL)
                elif hotel_rooms[room_number]['booked']:
                    print(Fore.RED + "Room is already booked." + Style.RESET_ALL)
                else:
                    name = input(Fore.CYAN + "Enter guest name: " + Style.RESET_ALL).strip()
                    nights_in = input(Fore.CYAN + "Enter number of nights (press Enter for 1): " + Style.RESET_ALL).strip()
                    nights = 1
                    if nights_in:
                        try:
                            nights = int(nights_in)
                            if nights <= 0:
                                print(Fore.YELLOW + "Number of nights must be at least 1. Using 1." + Style.RESET_ALL)
                                nights = 1
                        except ValueError:
                            print(Fore.YELLOW + "Invalid number entered; using 1 night." + Style.RESET_ALL)
                            nights = 1
                    book_room(room_number, name, nights)
                    print(Fore.GREEN + "Room booked successfully!" + Style.RESET_ALL)
                continue

            if operation == "3":
                print_separator()
                room_number = input(Fore.CYAN + "Enter room number to display: " + Style.RESET_ALL).strip()
                try:
                    details = display_rooms(room_number)
                    print("\n" + Fore.GREEN + "=" * 60)
                    print(f"ROOM {room_number} DETAILS")
                    print("=" * 60 + Style.RESET_ALL)
                    print(Fore.MAGENTA + f"Type: {details.get('type')}")
                    print(Fore.BLUE + f"Price: {details.get('price')}")
                    print(Fore.CYAN + f"Status: {'Booked' if details.get('booked') else 'Available'}")
                    guest = details.get('guest')
                    if guest:
                        print(Fore.YELLOW + f"Guest: {guest}")
                        print(Fore.RED + f"Check-in: {details.get('check_in_time')}")
                        print(Fore.RED + f"Check-out: {details.get('check_out_time')}")
                    else:
                        print(Fore.YELLOW + "Guest: -" + Style.RESET_ALL)
                    print(Fore.GREEN + "-" * 60 + Style.RESET_ALL)
                except ValueError as e:
                    print(Fore.RED + str(e) + Style.RESET_ALL)
                continue

            if operation == "4":
                print("\n" + Fore.GREEN + "=" * 60)
                print("AVAILABLE ROOMS")
                print("=" * 60 + Style.RESET_ALL)
                available_rooms = list_available_rooms()
                
                if not available_rooms:
                    print(Fore.YELLOW + "No available rooms." + Style.RESET_ALL)
                else:
                    for rn, det in available_rooms:
                        print(Fore.CYAN + f"Room {rn}: " + Fore.MAGENTA + f"type={det.get('type')}, " + Fore.BLUE + f"price={det.get('price')}" + Style.RESET_ALL)
                print(Fore.GREEN + "-" * 60 + Style.RESET_ALL)
                continue

            print(Fore.RED + "Invalid operation. Valid options: 1-5" + Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.RED + "\nInterrupted. Exiting." + Style.RESET_ALL)

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
    print(Fore.YELLOW + "=" * 60)
    print("WELCOME TO HOTEL MANAGER")
    print("=" * 60 + Style.RESET_ALL)




if __name__ == "__main__":
    main()
