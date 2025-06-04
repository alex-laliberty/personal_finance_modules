import financial_functions

def main():
    while True:
        print("\nSmart Personal Finance Analyzer")
        print("1. Load Transactions")
        print("2. Add Transaction")
        print("3. View Transactions")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. Analyze Finances")
        print("7. Save Transactions")
        print("8. Generate Report")
        print("9. Exit")
        option = input("Select an option: ")
        if option == "9":
            print("Exiting your Smart Personal Finance Analyzer.  Good-bye!")
            break
        elif option == "1":
            financial_functions.load_transactions()
        elif option == "2":
            financial_functions.add_transaction()
        elif option == "3":
            financial_functions.view_transactions()
        elif option == "4":
            financial_functions.update_transaction()
        elif option == "5":
            financial_functions.delete_transaction()
        elif option == "6":
            financial_functions.analyze_finances()
        elif option == "7":
            financial_functions.save_transactions()
        elif option == "8":
            financial_functions.generate_report()

if __name__ == "__main__":
    main()