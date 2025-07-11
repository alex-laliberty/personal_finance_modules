import csv
from datetime import datetime
from copy import deepcopy

def load_transactions(print_message=True, filename="financial_transactions.csv:"):
    transactions = []
    try:
        with open("financial_transactions.csv", "r") as my_file:
            reader = csv.DictReader(my_file)
            
            for row in reader:
                try:
                # Parsing datetime and checking date format; will throw error if format is incorrect   
                    row["date"] = datetime.strptime(row["date"], "%Y-%m-%d").date()
                # Changing transaction_id,customer_id, amount keys to int/float values
                    row["transaction_id"] = int(row["transaction_id"])
                    row["customer_id"] = int(row["customer_id"])    
                    row["amount"] = float(row["amount"])
                # Changing debit type transaction amounts to negative numbers IF debit has not been entered as a negative number
                # Considered raising ValueError for negative "amount" values for debit, but this may handle better
                    if row["type"] == "debit" and row["amount"] > 0:
                        row["amount"] = -abs(row["amount"])
                except (ValueError, TypeError) as add_error_log:
                    print(f"Transaction {row["transaction_id"]} is invalid.  Skipping.")
                    print(add_error_log)
                    with open("errors.txt", "a") as my_file:
                        my_file.write(f"{add_error_log}\n")
                    continue
                # Adding each transaction dictionary to a list
                transactions.append(row)
        # Returning the list with the function load_transactions
        if print_message:
            print("Transactions loaded successfully!")
        return transactions
    except FileNotFoundError:
        return "File not found."
    
def add_transaction(transactions):
    if not transactions:
        print("Transactions empty. Load transactions and try again.")
    else:
        new_transaction = {}    
        while True:
            try:
                new_transaction["transaction_id"] = transactions[-1]["transaction_id"] + 1
                new_transaction["date"] = datetime.strptime(input("Enter transaction date (YYYY-MM-DD): "), "%Y-%m-%d")
                new_transaction["customer_id"] = int(input("Enter customer ID: "))
                new_transaction["amount"] = float(input("Enter transaction amount: "))
                new_transaction["type"] = input("Enter transaction type (debit/credit/transfer): ")
                if new_transaction["type"] not in {"debit", "credit", "transfer"}:
                    raise ValueError
                if new_transaction["type"] == "debit":
                    new_transaction["amount"] = -abs(new_transaction["amount"])
                elif new_transaction["type"] == "credit" or new_transaction["type"] == "transfer":
                    new_transaction["amount"] = abs(new_transaction["amount"])
                new_transaction["description"] = input("Enter a transaction memo: ")       
                if not new_transaction["description"].strip():
                    raise ValueError
                transactions.append(new_transaction)
                break
            except (ValueError, TypeError):
                    print("Invalid input.  Please try again.")
        
        print("Transaction added successfully!")

def delete_transaction(transactions):
    
    if not transactions:
        print("Transactions empty. Load transactions and try again.")

    else:
        while True:
            try:
                for index, transaction in enumerate(transactions, start=1):
                    print(f"{index}: transaction ID: {transaction["transaction_id"]}; date: {transaction["date"]}; amount: {transaction["amount"]}")
                transaction_id = int(input(f"Select the transaction you wish to delete (1-{len(transactions)}): "))
                if transaction_id not in range(1,len(transactions)+1):
                    raise IndexError
                print(f"You have selected transaction {transactions[transaction_id-1]["transaction_id"]} (date: {transactions[transaction_id-1]["date"]}; amount: {transactions[transaction_id-1]["amount"]})")
                are_you_sure = input("Are you sure you want to delete this transaction? (yes/no): ")
                if are_you_sure not in {"yes", "no"}:
                    raise ValueError
                if are_you_sure == "yes":
                    transactions.pop(transaction_id-1)
                    print("Transaction deleted successfully!")
                elif are_you_sure == "no":
                    print("Transaction will not be deleted.")
                break
            except ValueError:
                print("Invalid input.  Please try again.")
            except IndexError:
                print(f"This index value is out of range.  Please choose a valid index (1-{len(transactions)}).")

def update_transaction(transactions):
    if not transactions:
        print("Transactions empty. Load transactions and try again.")
    else:
        while True:
            try:
                transaction_id = int(input(f"Select transaction to update ({transactions[0]["transaction_id"]}-{transactions[-1]["transaction_id"]}): "))-1
                if transaction_id not in range(len(transactions)):
                    raise IndexError
                change_field = input("Select field to change (amount/type/description): ")
                if change_field not in {"amount", "type", "description"}:
                    raise ValueError
                if change_field == "amount":
                    change_amount = input("Enter the updated amount: ")
                    transactions[transaction_id]["amount"] = change_amount
                elif change_field == "type":
                    change_type = input("Enter the updated transaction type (debit/credit/transfer): ")
                    if change_type not in {"debit", "credit", "transfer"}:
                        raise ValueError
                    if change_type == "debit":
                        transactions[transaction_id]["amount"] = -abs(transactions[transaction_id]["amount"])
                    elif change_type == "credit" or change_type == "transfer":
                        transactions[transaction_id]["amount"] = abs(transactions[transaction_id]["amount"])
                    transactions[transaction_id]["type"] = change_type
                elif change_field == "description":
                    change_description = input("Enter an updated transaction description: ")
                    if not change_description.strip():
                        raise ValueError
                    transactions[transaction_id]["description"] = change_description
                break
            except ValueError:
                print("Invalid input. Please try again.")
            except FileNotFoundError:
                print("File not found.")
            except IndexError:
                print("This transaction ID is out of range.")
        
        print("Transaction updated!")

def view_transactions(transactions):
    if not transactions:
        print("Transactions empty. Load transactions and try again.")
    else:
        transactions_copy = deepcopy(transactions)
        
        transactions_header_id = "ID     |"
        transactions_header_date = " Date       |"
        transactions_header_customer_id = " Customer |"
        transactions_header_amount = " Amount   |"
        transactions_header_type = " Type     |"
        transactions_header_description = " Description "

        # Formatting header and establishing width of each column
        print(transactions_header_id+
            transactions_header_date+
            transactions_header_customer_id+
            transactions_header_amount+
            transactions_header_type+
            transactions_header_description)
        
        # Formating table border
        print((len(transactions_header_id)-1)*"-"+"|"+
            (len(transactions_header_date)-1)*"-"+"|"+
            (len(transactions_header_customer_id)-1)*"-"+"|"+
            (len(transactions_header_amount)-1)*"-"+"|"+
            (len(transactions_header_type)-1)*"-"+"|"+
            (len(transactions_header_description)-1)*"-")
        
        # Iterating through rows and adding each transaction to the table in format
        for transaction in transactions_copy:
                transaction["amount"] = (f"{float(transaction["amount"]):.2f}")
                print(str(transaction["transaction_id"])+(len(transactions_header_id)-len(str(transaction["transaction_id"]))-1)*" "+"| "+
                    str(transaction["date"])+" | "+
                    str(transaction["customer_id"])+(len(transactions_header_customer_id)-len(str(transaction["customer_id"]))-2)*" "+"| "+
                    str(transaction["amount"])+(len(transactions_header_amount)-len(str(transaction["amount"]))-2)*" "+"| "+
                    transaction["type"]+(len(transactions_header_type)-len(transaction["type"])-2)*" "+"| "+
                    transaction["description"])

def analyze_finances(transactions):
    if not transactions:
        print("Transactions empty. Load transactions and try again.")
    else:
        transactions_from_year = []
        
        todays_date = datetime.now()

        credit_sum = 0
        debit_sum = 0
        transfer_sum = 0

        try:
            transaction_by_year = input("Would you like to analyze transactions from a single year? (yes/no): ")
            
            if transaction_by_year == "yes":
                transaction_year = int(input("Please enter the year (YYYY): "))
                for transaction in transactions:
                    if transaction["date"].year == transaction_year:
                        transactions_from_year.append(transaction)
                for transaction in transactions_from_year:
                    if transaction["type"] == "credit":
                        credit_sum += transaction["amount"]
                    elif transaction["type"] == "debit":
                        transaction["amount"] *= -1
                        debit_sum += transaction["amount"]
                    elif transaction["type"] == "transfer":
                        transfer_sum += transaction["amount"]
            if transaction_by_year not in {"yes", "no"}:
                raise ValueError
            
            elif transaction_by_year == "no":
                for transaction in transactions:
                    if transaction["type"] == "credit":
                        credit_sum += transaction["amount"]
                    elif transaction["type"] == "debit":
                        transaction["amount"] *= -1
                        debit_sum += transaction["amount"]
                    elif transaction["type"] == "transfer":
                        transfer_sum += transaction["amount"]
            
            net_balance = (credit_sum - debit_sum)

            if transaction_by_year == "no":
                print(f"Financial Summary: {todays_date.strftime("%d-%m-%Y")}")
            else:
                print(f"Financial Summary for {transaction_year}: {todays_date.strftime("%d-%m-%Y")}")
            print(f"Total Credits: ${credit_sum:.2f}")
            print(f"Total Debits: ${debit_sum:.2f}")
            print(f"Total Transfers: ${transfer_sum:.2f}")
            print(f"Net Balance: ${net_balance:.2f}")
        except ValueError:
            print("An error has occurred. Please try again.")

def save_transactions(transactions, filename = "financial_transactions.csv"):
    if not transactions:
        print("Transactions empty. Load transactions and try again.")
    else:
        try:
            with open("financial_transactions.csv", "w", newline="") as my_file:
                writer = csv.DictWriter(my_file, fieldnames=transactions[0].keys())
                writer.writeheader()
                writer.writerows(transactions)
        except FileNotFoundError:
            print("File not found.")

    print("Transactions saved successfully!")

def generate_report(transactions, filename="financial_summaries.txt"):
    if not transactions:
        print("Transactions empty. Load transactions and try again.")
    
    else:
        todays_date = datetime.now()

        credit_sum = 0
        debit_sum = 0
        transfer_sum = 0

        try:
            for transaction in transactions:
                if transaction["type"] == "credit":
                    credit_sum += transaction["amount"]
                elif transaction["type"] == "debit":
                    transaction["amount"] *= -1
                    debit_sum += transaction["amount"]
                elif transaction["type"] == "transfer":
                    transfer_sum += transaction["amount"]
        
            net_balance = (credit_sum - debit_sum)
        
            with open(filename, "a", newline="") as my_file:
                my_file.write(f"Financial Summary: {todays_date.strftime("%m-%d-%Y")}\n")
                my_file.write(f"Total Credits: ${credit_sum:.2f}\n")
                my_file.write(f"Total Debits: ${debit_sum:.2f}\n")
                my_file.write(f"Total Transfers: ${transfer_sum:.2f}\n")
                my_file.write(f"Net Balance: ${net_balance:.2f}\n")
                my_file.write(f"\n")
        except (ValueError, FileNotFoundError):
            print("An error has occurred.")

        print("Report generated to financial_summaries.txt")