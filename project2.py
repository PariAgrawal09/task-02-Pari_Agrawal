# ==========================================
#        PROFESSIONAL EXPENSE TRACKER
# ==========================================

print("=" * 55)
print("        PERSONAL EXPENSE TRACKER")
print("=" * 55)

# Budget Input
while True:
    try:
        budget = float(input("\nEnter Your Monthly Budget (₹): "))
        if budget <= 0:
            print("Budget must be greater than 0!")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

expenses = []
total_spent = 0

while True:

    print("\n" + "=" * 55)
    print("1. Add Expense")
    print("2. View Expense History")
    print("3. View Summary")
    print("4. Exit")
    print("=" * 55)

    choice = input("Choose an option: ")

    # Add Expense
    if choice == "1":
        category = input("Enter Expense Category: ")

        try:
            amount = float(input("Enter Expense Amount (₹): "))

            if amount <= 0:
                print("Amount must be positive!")
                continue

            expenses.append({
                "category": category,
                "amount": amount
            })

            total_spent += amount

            print("\n✅ Expense Added Successfully!")

        except ValueError:
            print("❌ Invalid Amount!")

    # View History
    elif choice == "2":

        if not expenses:
            print("\nNo expenses recorded yet.")
            continue

        print("\n========== EXPENSE HISTORY ==========")

        for i, expense in enumerate(expenses, start=1):
            print(
                f"{i}. {expense['category']:<20} ₹{expense['amount']:.2f}"
            )

    # View Summary
    elif choice == "3":

        remaining = budget - total_spent

        print("\n========== FINANCIAL SUMMARY ==========")
        print(f"Monthly Budget     : ₹{budget:.2f}")
        print(f"Total Expenses     : ₹{total_spent:.2f}")
        print(f"Remaining Balance  : ₹{remaining:.2f}")

        if remaining > 0:
            print("✅ You are within budget.")
        elif remaining == 0:
            print("⚠ Budget Fully Utilized.")
        else:
            print("❌ Budget Exceeded!")

    # Exit
    elif choice == "4":

        remaining = budget - total_spent

        print("\n" + "=" * 55)
        print("FINAL REPORT")
        print("=" * 55)

        print(f"Monthly Budget    : ₹{budget:.2f}")
        print(f"Total Expenses    : ₹{total_spent:.2f}")
        print(f"Remaining Balance : ₹{remaining:.2f}")

        print("\nThank You for Using Expense Tracker!")
        break

    else:
        print("❌ Invalid Choice! Please try again.")