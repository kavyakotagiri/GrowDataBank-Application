# GrowDataApplication
GrowDataApplication - Hackathon

Files details :

Data File – GrowDataBank.xlsx
GrowDataBankApplication.py – Code file which has all the logic
GrowDataBankApplication.ibynp – Same code file but to run on Jupyter Notebook
GrowDataBank_Application.ppt – PPT with all the Application details
README.md – contains details of each class and method in the application code.

GrowDataApplication can be run using Visual Studio code or using Jupyter Notebook
Separate files for VSCode and Jupyter Notebook are provided

Run the below file to run the application in VS Code :
GrowDataBankApplication.py

Run the below file to run the application in Jupyter Notebook:
GrowDataBankApplication.ipynp

Make sure DataGrowBank.xlsx file is available in the same folder the above code file is.

Also make sure all the required libraries are installed on VSCode/Jupyter Notebook

Problem Statements:

Separate excel sheets data into different CSV files
Cleaning of data
Separate Modules for each Department
Savings Account
Loan Account
Credit Card
Utilize OOPS principles
Financial Summary Data
Transaction History Data using Linked List Data Structure
NPA Identification
Credit Card Offering
High Missed EMI’s Customers
Monthly Spends of each customer
Data Visualization

Now let us explore the data.

1. Separate excel sheets data into different CSV files
2. Cleaning of Data

class ExcelToCSV is created to perform this task.
Excel file D=GrowData.xlsx file, sheet “Savings Accoun Transaction Data “ data is cleaned using dropna() and str.strip() funtions.

3. Separate Modules for each Department
4. Utilize OOPS principles


Class SavingsTransaction – For Savings Account Transaction Data

Class LoanTransaction – For Loan Account Data

Class CreditCardTransaction – For Credit Card Data

5. Financial Summary Data

This can take user id as input or a month as input.

Created separate classes methods based on the argument passed.

Created a centralized class FinancialSummary which calls the modules of each department and gets the financial summary based on the argument passed.

when customer id is passed as argument:

Class SavingsTransaction Method get_current_balance_cid is used to calculate the Current Balance of savings account.

Class LoanTransaction Method get_loan_rem_cid is used to calculate the Current Balance of savings account.

Class CreditCardTransaction Method get_credit_rem_cid is used to calculate the Current Balance of savings account.

when month is passed as argument:

Class SavingsTransaction Method get_current_balance_month is used to calculate the Current Balance of savings account.

Class LoanTransaction Method get_loan_rem_month is used to calculate the Current Balance of savings account.

Class CreditCardTransaction Method get_credit_rem_month is used to calculate the Current Balance of savings account.

6. Transaction History Data using Linked List Data Structure

Class Node is created for Linked List Node

Class LinkedList_SavingsTransaction is created for storing savings account transactions.

	append() method is used to add each row of the file data to LL data structure.

	filter_by_column_value() is used to filter the transactiosn based on customer id argument. 	This method is dynamic and can be used to filter any column. Here I used it to filter data 	based on customer_id

	getlength() is used to find the legth of the LL datastructure.

7. NPA Identification

Class NPAIdentification is created to identify NPA accounts and lists all the details of these accounts.

8. Credit Card Offering

Class CreditCardOffering is created to identify customers eligible for increased credit card balances and lists all the details of these accounts.

9. High Missed EMI’s Customers

Class LoanTransaction method get_max_missed_emi is created to identify high missed EMIs customer accounts and lists all the details of these accounts.

10. Monthly Spends of each customer

Class MonthlySpends method get_monthly_data is created to identify customers eligible for increased credit card balances and lists all the details of these accounts.
