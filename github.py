import os
import sys
import time
from datetime import datetime

# Global list to store calculations
history = []

# Header function
def print_header():
    print("=" * 50)
    print(" SIMPLE INTEREST CALCULATOR ".center(50, "-"))
    print("=" * 50)

# Main menu
def main_menu():
    while True:
        print_header()
        print("1. Calculate Simple Interest")
        print("2. View History")
        print("3. Save History to File")
        print("4. Clear History")
        print("5. Help")
        print("6. Exit")
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '1':
            calculate_interest()
        elif choice == '2':
            view_history()
        elif choice == '3':
            save_history()
        elif choice == '4':
            clear_history()
        elif choice == '5':
            help_section()
        elif choice == '6':
            print("\nThank you for using the calculator. Bye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
        input("\nPress Enter to continue...")

# Validate float input
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid non-negative number.")

# Core calculation function
def calculate_interest():
    print("\n--- Calculate Simple Interest ---")
    principal = get_valid_float("Enter Principal Amount: ₹ ")
    rate = get_valid_float("Enter Annual Interest Rate (%): ")
    time_years = get_valid_float("Enter Time (in years): ")

    interest = (principal * rate * time_years) / 100
    total_amount = principal + interest

    print(f"\n✅ Simple Interest = ₹ {interest:.2f}")
    print(f"💰 Total Amount Payable = ₹ {total_amount:.2f}")

    record = {
        'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'principal': principal,
        'rate': rate,
        'time': time_years,
        'interest': interest,
        'total': total_amount
    }
    history.append(record)

# View history
def view_history():
    print("\n--- Calculation History ---")
    if not history:
        print("No records found.")
    else:
        for i, rec in enumerate(history, 1):
            print(f"{i}. [{rec['datetime']}] ₹{rec['principal']} @ {rec['rate']}% for {rec['time']} years -> Interest: ₹{rec['interest']:.2f}, Total: ₹{rec['total']:.2f}")

# Save history to file
def save_history():
    if not history:
        print("\nNothing to save. History is empty.")
        return

    filename = "simple_interest_history.txt"
    with open(filename, "w") as f:
        f.write("Simple Interest Calculation History\n")
        f.write("=" * 50 + "\n")
        for rec in history:
            line = (f"[{rec['datetime']}] Principal: ₹{rec['principal']}, "
                    f"Rate: {rec['rate']}%, Time: {rec['time']} years, "
                    f"Interest: ₹{rec['interest']:.2f}, Total: ₹{rec['total']:.2f}\n")
            f.write(line)
    print(f"\n✅ History saved to {filename}")

# Clear history
def clear_history():
    if not history:
        print("\nHistory is already empty.")
    else:
        confirm = input("Are you sure you want to clear all history? (y/n): ").strip().lower()
        if confirm == 'y':
            history.clear()
            print("✅ History cleared.")
        else:
            print("Cancelled.")

# Help section
def help_section():
    print("\n--- Help ---")
    print("This is a CLI-based Simple Interest Calculator.")
    print("You can:")
    print("- Calculate simple interest using Principal, Rate, and Time.")
    print("- View past calculations.")
    print("- Save your session to a text file.")
    print("- Clear history when needed.")
    print("\nFormula Used:")
    print("Simple Interest (SI) = (P × R × T) / 100")
    print("Where P = Principal, R = Rate, T = Time (in years)")

# Entry point
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nExiting. Thank you!")
