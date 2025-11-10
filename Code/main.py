'''''
Methods Data Analytics Assignment
Ayemhenre Isikhuemhen
March 14, 2025
File Descirption: 
'''''
# Library imports
import sys
import time
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Package imports
from client_data import load_csv, client_data
import visuals

# UTITILITY FUNCTIONS

# slow_print function: Allows program to imitate human typing
def slow_print(str):
    for i in str:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.11)

# run_all: Runs all of the visual.py functions at once
def run_all():
    visuals.pie_devices()
    visuals.bar_multiDevices()
    visuals.bar_catDevices()
    visuals.bex_deviceTimes()
    visuals.box_deviceSatis()
    visuals.pie_payment()
    visuals.box_payCoupon()
    visuals.bar_payCoupon()
    visuals.pie_payChurn()
    visuals.box_payOrder()
    visuals.box_catTime()
    visuals.bar_catCoupon()
    visuals.bar_catSatis()

# MAIN PROGRAM
def main():
    # fields
    run = bool
    file_path = r"C:\Users\Owner\Documents\GitHub\E-Commerce-Clustering\Data Files\dohtem_ecommerce_customers.csv"

    # Start: User Interface Header
    print()
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("|        DOTHEM'S E-COMERCE ANALYSIS        |")
    print("| Author: Ayemhenre Isikhuemhen, 03/14/2025 |")
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print()

    # Load Data
    slow_print("Loading client data from CSV...\n")
    clients_data = load_csv(file_path)
    
    # Count client_data_entries
    c_d_entries = len(clients_data)
    print("------------------------")
    print(str(c_d_entries) + " Entries Recieved")
    print("------------------------")

# Sequence for user to call data analysis functions from other classes
    
    run = True
    while run:
        print("\nSelect an option:")
        print("1. Run all functions")
        print("2. Run specific function(s)")
        print("3. Exit")

        try:
            user_input = int(input("Enter your choice: "))

            if user_input == 1:
                run_all()

            elif user_input == 2:
                print("\nSelect the function(s) to run (Enter numbers separated by commas):")
                print("[1] pie_devices()")
                print("[2] bar_multiDevices()")
                print("[3] bar_catDevices()")
                print("[4] bex_deviceTimes()")
                print("[5] box_deviceSatis()")
                print("[6] pie_payment()")
                print("[7] box_payCoupon()")
                print("[8] bar_payCoupon()")
                print("[9] pie_payChurn()")
                print("[10] box_payOrder()")
                print("[11] box_catTime()")
                print("[12] bar_catCoupon()")
                print("[13] bar_catSatis()")
                print("[14] Cancel and return to main menu")

                user_choices = input("Enter your choices (e.g. 1,3,5): ").split(',')
                user_choices = [choice.strip() for choice in user_choices]

                for choice in user_choices:
                    if choice == '1':
                        visuals.pie_devices()
                    elif choice == '2':
                        visuals.bar_multiDevices()
                    elif choice == '3':
                        visuals.bar_catDevices()
                    elif choice == '4':
                        visuals.bex_deviceTimes()
                    elif choice == '5':
                        visuals.box_deviceSatis()
                    elif choice == '6':
                        visuals.pie_payment()
                    elif choice == '7':
                        visuals.box_payCoupon()
                    elif choice == '8':
                        visuals.bar_payCoupon()
                    elif choice == '9':
                        visuals.pie_payChurn()
                    elif choice == '10':
                        visuals.box_payOrder()
                    elif choice == '11':
                        visuals.box_catTime()
                    elif choice == '12':
                        visuals.bar_catCoupon()
                    elif choice == '13':
                        visuals.bar_catSatis()
                    elif choice == '14':
                        print("Returning to main menu...")
                        break
                    else:
                        print(f"Invalid choice: {choice}")

            elif user_input == 3:
                print("Exiting the program. Goodbye!")
                run = False

            else:
                print("Invalid input. Please enter 1, 2, or 3.")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()