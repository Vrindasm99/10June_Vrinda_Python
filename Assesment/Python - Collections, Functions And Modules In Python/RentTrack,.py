# RentTrack - A Simple Library Rental Management System

from datetime import datetime

# Global list to hold current rentals
rentals = []

# Fixed late fee per day
LATE_FEE_PER_DAY = 10

# Function to record a new rental
def book_rental():
    print("\n--- New Book Rental ---")
    customer = input("Enter Customer Name: ").strip()
    book = input("Enter Book Title: ").strip()
    rental_date = input("Enter Rental Date (DD-MM-YYYY): ").strip()
    due_date = input("Enter Expected Return Date (DD-MM-YYYY): ").strip()

    rental = {
        "customer": customer,
        "book": book,
        "rental_date": rental_date,
        "due_date": due_date,
        "returned": False
    }
    rentals.append(rental)
    print(f"\n Rental recorded successfully for '{book}' by {customer}!\n")

# Function to calculate days between two dates
def date_diff(d1, d2):
    d1 = datetime.strptime(d1, "%d-%m-%Y")
    d2 = datetime.strptime(d2, "%d-%m-%Y")
    return (d2 - d1).days

# Function to return a rented book
def book_return():
    print("\n--- Book Return ---")
    customer = input("Enter Customer Name: ").strip()
    book = input("Enter Book Title: ").strip()
    return_date = input("Enter Actual Return Date (DD-MM-YYYY): ").strip()

    found = False
    for rental in rentals:
        if rental["customer"].lower() == customer.lower() and rental["book"].lower() == book.lower() and not rental["returned"]:
            found = True
            rental["returned"] = True

            # Calculate late fee
            days_late = date_diff(rental["due_date"], return_date)
            late_fee = LATE_FEE_PER_DAY * days_late if days_late > 0 else 0

            print("\n--- Return Receipt ---")
            print(f"Customer Name   : {rental['customer']}")
            print(f"Book Title      : {rental['book']}")
            print(f"Rented On       : {rental['rental_date']}")
            print(f"Due Date        : {rental['due_date']}")
            print(f"Returned On     : {return_date}")
            print(f"Late Fee        : ₹{late_fee}")
            print("---------------------------")
            print("Book return recorded successfully!\n")
            break

    if not found:
        print("\n No active rental found for this book and customer.\n")

# Function to show all rentals
def show_rentals():
    print("\n--- Current Rental Records ---")
    if not rentals:
        print("No rentals recorded yet.\n")
        return

    for i, r in enumerate(rentals, 1):
        status = "Returned" if r["returned"] else "Rented"
        print(f"{i}. {r['customer']} - {r['book']} ({status})")
    print()

# Main menu
def main():
    while True:
        print("========== RentTrack Library ==========")
        print("1. Record New Rental")
        print("2. Return a Book")
        print("3. View Rental Summary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            book_rental()
        elif choice == '2':
            book_return()
        elif choice == '3':
            show_rentals()
        elif choice == '4':
            print("\n Thank you for using RentTrack. Goodbye!")
            break
        else:
            print("\n Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
