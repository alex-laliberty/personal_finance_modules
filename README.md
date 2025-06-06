Thank you for using this Smart Personal Finance Analyzer!
-

To begin, the following files are required for the proper function of this program:
  1. financial_functions.py
  2. financial_analyzer.py
  3. financial_transactions.csv
  4. errors.txt
  5. financial_summaries.txt

Start by running financial_analyzer.py and load your transactions using option 1.  This will make all transactions in your financial_transactions.csv file available for viewing, updating, deleting, and analyzing in a working list; you may also add transactions to this working list.  Once finished, you may save all changes to the working list to your financial_transactions file. All these functions are described in greater detail below.

As transactions are loaded, any transactions with erroneous data will be excluded from analysis and will be unavailable for viewing.  Descriptions of the errors encountered by the program will be available in errors.txt and will also be displayed after loading transactions within the program.

Use the personal finance analyzer to perform the following functions:
- 
  1. Load transactions: This makes transactions stored on file available to the program.  It is your first step.
  2. View transactions: All valid transactions and their details will be displayed in a table
  3. Add transactions: Add new transactions to the working list by providing transaction details when prompted.
  4. Update transactions: Change any transaction detail.
  5. Delete transactions: Remove transactions from the working list.
  6. Save transactions: Once finished, save your transactions to update the financial_transactions file with your changes.
  7. Analyze finances: Create a report of credit, debit, and transfer totals, as well as your net balance; you may even create reports by year.
  8. Generate reports: The program will also generate the report in a text file if requested.  Reports are date-stamped so you may keep track of changes over time.

Special considerations
-
  1.  Flexibility in handling inconsistent user input was desired, so debit transactions are displayed as negative values whether they have been entered as a positive or negative value (unless they are being used by the analyze_finances() function).
  2.  The table produced when viewing transactions is somewhat dynamic.  Formatting should adjust with string length.
  3.  Future updates should provide a way to fix erroneous data so "bad" transactions can be fixed and included when loading transactions.  Dynamic transaction IDs are another consideration for improvement.
