# Password Manager

## Project Overview

This is a **Password Manager** application built using Python's **Tkinter** library for the graphical user interface (GUI). It allows users to:
- Generate strong random passwords.
- Save website credentials (website, email/username, password).
- Search for stored credentials by website name.
- Automatically copy the generated password to the clipboard.

All credentials are stored in a **JSON** file (`data_details.json`), and case-insensitive search functionality ensures that the website name is found, regardless of case differences.

## Features
1. **Password Generator**: Creates a strong password with a mix of letters, numbers, and symbols.
2. **Save Credentials**: Stores website credentials (website, email, and password) in a `data_details.json` file.
3. **Search for Credentials**: Allows searching for saved credentials by website name.
4. **Clipboard Copying**: Automatically copies the generated password to the clipboard.
5. **Error Handling**: Handles file not found errors and prevents empty fields from being saved.

## Installation & Setup

### Prerequisites
- **Python 3.x** installed on your system.
- Required Python libraries:
  - `tkinter` (for the GUI)
  - `json` (for reading/writing JSON data)
  - `pyperclip` (for clipboard functionality)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-manager.git
