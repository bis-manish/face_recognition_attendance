import os
import subprocess
from colorama import init, Fore, Style
from tabulate import tabulate
import csv

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print(Fore.CYAN + "============================================")
    print(Fore.YELLOW + "    FACE RECOGNITION ATTENDANCE SYSTEM")
    print(Fore.CYAN + "============================================")
    print()

def register_face():
    print_header()
    print(Fore.GREEN + "REGISTER NEW FACE")
    print("--------------------------------------------")
    name = input(Fore.WHITE + "Enter person's name: ").strip()
    
    if not name:
        print(Fore.RED + "Error: Name cannot be empty!")
        input("\nPress Enter to continue...")
        return
    
    try:
        print(Fore.YELLOW + "\nStarting face registration...")
        subprocess.run(["python", "register_face.py", name], check=True)
        print(Fore.GREEN + f"\nSuccessfully registered {name}!")
    except subprocess.CalledProcessError:
        print(Fore.RED + "\nFailed to register face. Check console for errors.")
    input("\nPress Enter to continue...")

def train_model():
    print_header()
    print(Fore.GREEN + "TRAINING FACE RECOGNITION MODEL")
    print("--------------------------------------------")
    print(Fore.YELLOW + "Training may take a few minutes...")
    
    try:
        subprocess.run(["python", "train_model.py"], check=True)
        print(Fore.GREEN + "\nModel trained successfully!")
    except subprocess.CalledProcessError:
        print(Fore.RED + "\nTraining failed. Check console for errors.")
    input("\nPress Enter to continue...")

def start_recognition():
    print_header()
    print(Fore.GREEN + "STARTING FACE RECOGNITION")
    print("--------------------------------------------")
    print(Fore.YELLOW + "Press 'q' in the OpenCV window to stop.")
    
    try:
        subprocess.run(["python", "recognize_face.py"], check=True)
        print(Fore.GREEN + "\nAttendance marked successfully!")
    except subprocess.CalledProcessError:
        print(Fore.RED + "\nRecognition failed. Check console for errors.")
    input("\nPress Enter to continue...")

def view_attendance():
    print_header()
    print(Fore.GREEN + "ATTENDANCE RECORDS")
    print("--------------------------------------------")
    
    csv_file = "attendance/attendance.csv"
    if not os.path.exists(csv_file):
        print(Fore.RED + "No attendance records found!")
        input("\nPress Enter to continue...")
        return
    
    records = []
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            records.append(row)
    
    if not records:
        print(Fore.YELLOW + "No attendance data available.")
    else:
        print(Fore.CYAN + tabulate(records, headers=headers, tablefmt="grid"))
    
    input("\nPress Enter to continue...")

def main_menu():
    while True:
        print_header()
        print(Fore.WHITE + "MAIN MENU")
        print("--------------------------------------------")
        print(Fore.CYAN + "1. Register New Face")
        print(Fore.CYAN + "2. Train Model")
        print(Fore.CYAN + "3. Start Recognition & Attendance")
        print(Fore.CYAN + "4. View Attendance Records")
        print(Fore.RED + "5. Exit")
        print("--------------------------------------------")
        
        choice = input(Fore.YELLOW + "Select an option (1-5): ").strip()
        
        if choice == "1":
            register_face()
        elif choice == "2":
            train_model()
        elif choice == "3":
            start_recognition()
        elif choice == "4":
            view_attendance()
        elif choice == "5":
            print(Fore.GREEN + "\nExiting system. Goodbye!")
            break
        else:
            print(Fore.RED + "\nInvalid choice! Try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()