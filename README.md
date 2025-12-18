# Hotel Management System

A terminal-based hotel room management application built with Python. This project demonstrates practical use of dictionaries, user input handling, and file organization for managing hotel rooms and bookings.

## 📋 Features

- **Add Rooms** - Create new hotel rooms with different room types (Single, Double, Suite, Deluxe)
- **Book Rooms** - Reserve available rooms with guest details and check-in/check-out dates
- **Display Room Details** - View detailed information about a specific room
- **List Available Rooms** - See all rooms currently available for booking
- **Colorized Interface** - User-friendly terminal UI with colored text for better readability

## 📦 Prerequisites

### Option 1: Running from Source (Recommended for Development)

- **Python 3.8 or higher**
- **pip** (Python package manager)

### Option 2: Running the Executable (No Prerequisites)

- **Windows OS**
- No Python installation required!

## 🚀 Installation & Usage

### Quick Start (Using Pre-built Executable)

1. Download the latest `hotel_manager.exe` from [GitHub Releases](https://github.com/S-web155/hotel_management_system/releases)
2. Run the executable:
   ```bash
   hotel_manager.exe
   ```
3. Follow the on-screen menu prompts

### Running from Source

#### 1. Clone the Repository

```bash
git clone https://github.com/S-web155/hotel_management_system.git
cd hotel-management-system
```

#### 2. Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install the required package:

```bash
pip install colorama
```

#### 4. Run the Application

```bash
python hotel_manager.py
```

## 📚 Project Structure

```
hotel-management-system/
├── hotel_manager.py          # Main application entry point
├── hotel_manager.spec        # PyInstaller configuration
├── requirements.txt          # Python dependencies
├── functions/
│   ├── __init__.py          # Package initialization
│   └── utils.py             # Core business logic functions
├── database/
│   ├── __init__.py          # Package initialization
│   └── price.py             # Room pricing data
├── LICENSE                   # Project license
└── README.md                # This file
```

## 🎮 How to Use

1. **Main Menu**: Select an option from 1-5
2. **Add a Room**: 
   - Choose room type (Single, Double, Suite, Deluxe)
   - Enter room number
3. **Book a Room**:
   - Enter room number
   - Enter guest name
   - Enter check-in date (YYYY-MM-DD format)
   - Enter check-out date (YYYY-MM-DD format)
4. **Display Room Details**: Enter room number to see full details
5. **List Available Rooms**: View all unbooked rooms
6. **Exit**: Quit the application

## 💰 Room Types & Pricing

| Room Type | Price (per night) |
|-----------|------------------|
| Single    | $500             |
| Double    | $900             |
| Suite     | $1,500           |
| Deluxe    | $2,500           |

## 🛠️ Development

### Building the Executable

To build the Windows executable from source:

```bash
pip install pyinstaller
pyinstaller hotel_manager.spec
```

The executable will be created in the `dist/` folder.

### Running Tests

Currently, this project uses manual testing. Future versions may include automated tests.

## 📝 Notes

- Room numbers are stored as strings but can accept integers
- All data is stored in-memory (not persisted between sessions)
- Dates should be entered in YYYY-MM-DD format for consistency
- Press `Ctrl+C` to interrupt and exit at any time

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created as a school project to learn Python fundamentals including:
- Dictionaries and data structures
- User input handling
- Terminal-based UI with colorama
- Function organization and imports
- Error handling

## 🔗 Links

- [GitHub Repository](https://github.com/S-web155/hotel_management_system)
- [Releases](https://github.com/S-web155/hotel_management_system/releases)
