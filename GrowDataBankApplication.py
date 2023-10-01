import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import csv
from datetime import datetime


class ExcelToCSV:
	# Specify the path to Excel file
	excel_file_path = 'GrowDataBank.xlsx'
	
	# Read the Excel file and get sheet names
	excel_data = pd.ExcelFile(excel_file_path)
	sheet_names = excel_data.sheet_names
	
	# folder to save CSV files
	output_folder = '' 
	
	#clean up Savings Accoun Transaction Data sheet data
	df=pd.read_excel('GrowDataBank.xlsx',sheet_name='Savings Accoun Transaction Data')
	df = df[' Customer_ID     Amount   Transaction_Type  Transaction_Date '].str.strip()
	savings = df.str.split('\s+', expand=True)
	savings.columns = ['Customer_ID','Amount','Transaction_Type','Transaction_Date']
	savings.dropna(inplace=True)
	savings.to_csv('Savings Accoun Transaction Data.csv', index=False)
	
	# Loop through each sheet, read it, and export as a CSV file
	for sheet_name in sheet_names:
		if sheet_name != 'Savings Accoun Transaction Data':
			df = pd.read_excel(excel_data, sheet_name)
			csv_file_path = f'{output_folder}{sheet_name}.csv'
			df.to_csv(csv_file_path, index=False)
			file_name = sheet_name+'.csv'
			df1 = pd.read_csv(file_name)
			df1 = df1.dropna(how='all')
			df1.to_csv(csv_file_path, index=False)
			df1 = pd.read_csv(file_name)
			df1.to_csv(csv_file_path, index=False)

# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class for storing Savings Account Transactions
class LinkedList_SavingsTransaction:
    def __init__(self):
        self.head = None

    #Adds each row to LL
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    #Filters LL data based on condition
    def filter_by_column_value(self, column_name, value):
        filtered_list = LinkedList_SavingsTransaction()
        current = self.head

        while current:
            data = current.data
            if column_name in data and data[column_name] == value:
                filtered_list.append(data)
            current = current.next

        return filtered_list
    
    #Gets the length of LL
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count 

# Calculates Current Balance calculation for Savings Account
class SavingsTransaction:
    def __init__(self,c_id):
        self.c_id=c_id

    #Calculation based on Customer_Id
    def get_current_balance_cid(self):

        #Credit and Debit amounts for given customer
        CAmount = savings_transactions.loc[savings_transactions['Transaction_Type'] == 'Credit'].groupby('Customer_ID')['Amount'].sum().reset_index()
        DAmount = savings_transactions.loc[savings_transactions['Transaction_Type'] == 'Debit'].groupby('Customer_ID')['Amount'].sum().reset_index()
        if CAmount.empty or DAmount.empty:
            return 0
        else:
            #Merge Credit and Debit amount DFs based on Customer Id
            merged_df = CAmount.merge(DAmount, on='Customer_ID', how='outer')

            #Rename Credit and Debit Amount columns
            merged_df = merged_df.rename(columns={'Amount_x': 'CreditAmount', 'Amount_y': 'DebitAmount'})

            #Fill with 0 if merged DF data columns have no value
            merged_df['CreditAmount'].fillna(0, inplace=True)
            merged_df['DebitAmount'].fillna(0, inplace=True)

            #Calculate Current Balance based on Credit and Debit Amounts
            merged_df['Current Balance'] = merged_df['CreditAmount'] - merged_df['DebitAmount']
            c_balance = merged_df[merged_df['Customer_ID'] == self.c_id]
    
            #Return Current Balance of Customer
            return c_balance
    
    #Calculation based on Month
    def get_current_balance_month(self):
        #Credit and Debit amounts for all customers in given month
        CAmount = savings_transactions.loc[(savings_transactions['Transaction_Type'] == 'Credit') & (savings_transactions['Transaction_Date_Month'] == self.c_id)].groupby('Customer_ID')['Amount'].sum().reset_index()
        DAmount = savings_transactions.loc[(savings_transactions['Transaction_Type'] == 'Debit') & (savings_transactions['Transaction_Date_Month'] == self.c_id)].groupby('Customer_ID')['Amount'].sum().reset_index()
        if CAmount.empty or DAmount.empty:
            return 0
        else:
            #Merge Credit and Debit amount DFs based on Customer Id
            merged_df = CAmount.merge(DAmount, on='Customer_ID', how='outer')

            #Rename Credit and Debit Amount columns
            merged_df = merged_df.rename(columns={'Amount_x': 'CreditAmount', 'Amount_y': 'DebitAmount'})

            #Fill with 0 if merged DF data columns have no value
            merged_df['CreditAmount'].fillna(0, inplace=True)
            merged_df['DebitAmount'].fillna(0, inplace=True)

            #Calculate Current Balance based on Credit and Debit Amounts in given month
            merged_df['Current Balance'] = merged_df['CreditAmount'] - merged_df['DebitAmount']
            merged_df['TransactionMonth'] = self.c_id

            #Return Current Balance for all Customers in given month
            return merged_df
        
    #Call method based of datatype passed in the argument
    def get_current_balance(self):
        #argument is string when customer_id is passed. Call respective method.
        if isinstance(self.c_id, str):
            return SavingsTransaction.get_current_balance_cid(self)
        #argument is int when month is passed. Call respective method.
        elif isinstance(self.c_id, int):
            return SavingsTransaction.get_current_balance_month(self)
    
# Calculates Loand details for Loan Account
class LoanTransaction:
    def __init__(self,c_id=0):
        self.c_id=c_id

    #Calculation based on Account_id
    def get_loan_rem_cid(self):
        #Loan and Recovered amounts for given customer
        Loan_Amount = loan_transactions[loan_transactions['Account_id']==self.c_id].groupby('Account_id')['Loan Amount'].sum().reset_index()
        RecoveredTillNow = loan_transactions[loan_transactions['Account_id']==self.c_id].groupby('Account_id')['Recovered Till Now'].sum().reset_index()
        if Loan_Amount.empty or RecoveredTillNow.empty:
            return 0
        else:
            #Merge Loan and Recovered amount DFs based on Account_id
            merged_df1 = Loan_Amount.merge(RecoveredTillNow, on='Account_id', how='outer')
            merged_df1['Remaining Loan'] = merged_df1['Loan Amount']-merged_df1['Recovered Till Now'].values[0]

            #Calculate Loan Balance based on Loan and Recovered Amounts
            l_balance = merged_df1.loc[merged_df1['Account_id'] == self.c_id,'Remaining Loan'].values[0]

            #Return Loan Balance for given Account Id
            return l_balance
    
    #Calculation based on given month for all customers
    def get_loan_rem_month(self):
        #Loan and Recovered amounts for all customer who were given loan in specified month
        Loan_Amount = loan_transactions[loan_transactions['Loan Date_Month']==self.c_id].groupby('Account_id')['Loan Amount'].sum().reset_index()
        RecoveredTillNow = loan_transactions[loan_transactions['Loan Date_Month']==self.c_id].groupby('Account_id')['Recovered Till Now'].sum().reset_index()
        
        if Loan_Amount.empty or RecoveredTillNow.empty:
            return 0
        else:
            #Merge Loan and Recovered amount DFs based on Account_id
            merged_df1 = Loan_Amount.merge(RecoveredTillNow, on='Account_id', how='outer')
            #Calculate Loan Balance based on Loan and Recovered Amounts
            merged_df1['Remaining Loan'] = merged_df1['Loan Amount']-merged_df1['Recovered Till Now'].values[0]
            merged_df1['Loan Date_Month'] = self.c_id
            return merged_df1
    
    #Call method based of datatype passed in the argument
    def get_loan_rem(self):
        #argument is string when Account_id is passed. Call respective method.
        if isinstance(self.c_id, str):
            return LoanTransaction.get_loan_rem_cid(self)
        #argument is int when month is passed. Call respective method.
        elif isinstance(self.c_id, int):
            return LoanTransaction.get_loan_rem_month(self)
    
    #Accounts/Customers who missed maximum emi payments
    def get_max_missed_emi(self):
        emi_df = loan_transactions
        emi_df['MonthlyEMI'] = loan_transactions['Loan Amount']/loan_transactions['EMI count']
        today = datetime.now().date()
        emi_df['NoOfMonths'] = ((today.year - emi_df['Loan Date'].dt.year) * 12 +
                          (today.month - emi_df['Loan Date'].dt.month))
        emi_df['AmoutToBeRecovered'] = emi_df['MonthlyEMI']*emi_df['NoOfMonths']
        emi_df['EMIMissed'] = ((emi_df['AmoutToBeRecovered']-emi_df['Recovered Till Now'])/emi_df['MonthlyEMI']).astype(int)
        
        missed_emi = emi_df['EMIMissed'].max()
        return emi_df[emi_df['EMIMissed'] == missed_emi].reset_index()
        #return emi_df


class CreditCardTransaction:
    def __init__(self,c_id):
        self.c_id=c_id

    def get_credit_rem_cid(self):
        Credit_Limit = cc_transactions[cc_transactions['Account_Id']==self.c_id].groupby('Account_Id')['Card Limit'].sum().reset_index()
        Used_Amount = cc_transactions[cc_transactions['Account_Id']==self.c_id].groupby('Account_Id')['Current Outstanding Bill'].sum().reset_index()
        #print(Used_Amount)
        #loan_transactions[loan_transactions['Account_id'] == self.c_id]
        if Credit_Limit.empty or Used_Amount.empty:
            return 0
        merged_df2 = Credit_Limit.merge(Used_Amount, on='Account_Id', how='outer')
        merged_df2['Remaining Credit'] = merged_df2['Card Limit']-merged_df2['Current Outstanding Bill']
        merged_df2['Remaining Credit'] = merged_df2.loc[merged_df2['Account_Id'] == self.c_id,'Remaining Credit']
        return merged_df2
    
    def get_credit_rem_month(self):
        Credit_Limit = cc_transactions[cc_transactions['Credit Card Date_Month']==self.c_id].groupby('Account_Id')['Card Limit'].sum().reset_index()
        Used_Amount = cc_transactions[cc_transactions['Credit Card Date_Month']==self.c_id].groupby('Account_Id')['Current Outstanding Bill'].sum().reset_index()
        if Credit_Limit.empty or Used_Amount.empty:
            return 0
        merged_df2 = Credit_Limit.merge(Used_Amount, on='Account_Id', how='outer')
        merged_df2['Remaining Credit'] = merged_df2['Card Limit']-merged_df2['Current Outstanding Bill']
        return merged_df2
    
    def get_credit_rem(self):
        if isinstance(self.c_id, str):
            return CreditCardTransaction.get_credit_rem_cid(self)
        elif isinstance(self.c_id, int):
            return CreditCardTransaction.get_credit_rem_month(self)

class NPAIdentification:
    def __init__(self):
        pass
    def get_npa_accounts(self):
        NPA_Customers = cc_transactions[cc_transactions['Number of Missed Payments']>0].reset_index()
        return NPA_Customers

class CreditCardOffering:
    def __init__(self):
        pass
    def get_ccoffer_accounts(self):
        CC_Offer_Customers = cc_transactions[(cc_transactions['Card Limit']<=10000) & (cc_transactions['Number of Missed Payments']==0) & (cc_transactions['Number of Transactions']>=10)].reset_index()
        return CC_Offer_Customers
    
class MonthlySpends:
    def __init__(self,c_id):
        self.c_id=c_id
    def get_monthly_data(self):
        savings = SavingsTransaction(self.c_id).get_current_balance_month()
        credit = CreditCardTransaction(self.c_id).get_credit_rem_month()
        merged_df3 = savings.merge(credit, left_on='Customer_ID',right_on='Account_Id', how='outer')
        merged_df3['CreditAmount'].fillna(0, inplace=True)
        merged_df3['DebitAmount'].fillna(0, inplace=True)
        merged_df3['Current Balance'].fillna(0, inplace=True)
        merged_df3['Card Limit'].fillna(0, inplace=True)
        merged_df3['Current Outstanding Bill'].fillna(0, inplace=True)
        merged_df3['Remaining Credit'].fillna(0, inplace=True)
        merged_df3['Customer_ID'] = np.where(merged_df3['Customer_ID'].isna(), merged_df3['Account_Id'], merged_df3['Customer_ID'])
        required_columns = merged_df3[['Customer_ID', 'CreditAmount','DebitAmount','Card Limit','Current Outstanding Bill','Remaining Credit']]
        return required_columns

class FinancialSummary:

    def __init__(self, c_id):
        self.c_id=c_id

    def calculate_all_dept_data(self):

        FinancialSummary.current_balance = SavingsTransaction(self.c_id).get_current_balance()
        FinancialSummary.loan_amount_rem = LoanTransaction(self.c_id).get_loan_rem()
        FinancialSummary.credit_card_balance = CreditCardTransaction(self.c_id).get_credit_rem()

        # #Customer/Account Level details
        # if isinstance(self.c_id, str):
        #     pass
        # #Monthly Level Details
        # elif isinstance(self.c_id, int):

    def print_cus_report(self):
        #Customer/Account Level details
        if isinstance(self.c_id, str):
            print("\nFinancial Summary for Customer with Id: ", self.c_id)
        #Monthly Level Details
        elif isinstance(self.c_id, int):
            print("\nFinancial Summary for Month: ", self.c_id)

        print("\nCurrent Balance:\n", self.current_balance)
        print("\nRemaining Loan Amount:\n", self.loan_amount_rem)
        print("\nRemaining Credit Limit:\n", self.credit_card_balance)

    def print_monthly_report(self):
        pass

    def print_charts(self):

        # Savings Account Transaction Details
        self.current_balance.plot(kind='bar', x='Customer_ID', y=["CreditAmount", "DebitAmount","Current Balance"], figsize=(8, 6), title='Savings Account Transaction Details', color=['skyblue','orange','green'])
        plt.xlabel('Customer ID')
        plt.ylabel('Transaction Amount')
        plt.grid(True)
        plt.show()

        #Credit Card Transaction Details
        self.credit_card_balance.plot(kind='bar', x='Account_Id', y=["Card Limit", "Current Outstanding Bill"], figsize=(8, 6), title='Credit Card Transaction Details', color=['green','red'])
        plt.xlabel('Account_Id')
        plt.ylabel('Credit Limits')
        plt.grid(True)
        plt.show()


#Read excel data properly in CSV format
ExcelToCSV()

#Create separate Pandas DataFrames for each CSV file data
savings_transactions = pd.read_csv('Savings Accoun Transaction Data.csv')
loan_transactions = pd.read_csv('Loan Account Data.csv')
cc_transactions = pd.read_csv('Credit Card Data.csv')

#Convert date value columns in each CSV to proper datetime format
date_format = '%Y-%m-%d'
savings_transactions['Transaction_Date'] = savings_transactions['Transaction_Date'].apply(lambda x: datetime.strptime(x, date_format))
loan_transactions['Loan Date'] = loan_transactions['Loan Date'].apply(lambda x: datetime.strptime(x, date_format))
cc_transactions['Credit Card Date'] = cc_transactions['Credit Card Date'].apply(lambda x: datetime.strptime(x, date_format))

#Add new column to extract month from date in each DF
savings_transactions['Transaction_Date_Month'] = savings_transactions['Transaction_Date'].dt.month
loan_transactions['Loan Date_Month'] = loan_transactions['Loan Date'].dt.month
cc_transactions['Credit Card Date_Month'] = cc_transactions['Credit Card Date'].dt.month

#Convert CustomerId/AccountId value columns in each CSV to proper string format
savings_transactions['Customer_ID'] = savings_transactions['Customer_ID'].astype('string')
loan_transactions['Account_id'] = loan_transactions['Account_id'].astype('string')
cc_transactions['Account_Id'] = cc_transactions['Account_Id'].astype('string')


# Financial Summary details for a specific customer
Customer_Id = 'cust_idno_1004'
fs=FinancialSummary(Customer_Id)
fs.calculate_all_dept_data()
fs.print_cus_report()
fs.print_charts()

# Financial Summary details for all customer in given month
Month_Num = 2
fs=FinancialSummary(Month_Num)
fs.calculate_all_dept_data()
fs.print_cus_report()

fs.print_charts()

#Missed EMI payments
print("\nHigh Missed EMI Account:\n")
missed_emi_df = LoanTransaction().get_max_missed_emi()
print(missed_emi_df)
#High Missed EMIs Accounts
missed_emi_df.plot(kind='bar', x='Account_id', y=["NoOfMonths", "EMIMissed"], figsize=(8, 6), title='High Missed EMIs Accounts', color=['green','red'])
plt.xlabel('Account id')
plt.ylabel('EMI')
plt.grid(True)
plt.show()


#Monthly spends of each customer
msg = f"\nMonthly spends of each Customer for month: {Month_Num}\n"
print(msg)
monthly_spends = MonthlySpends(Month_Num).get_monthly_data()
print(monthly_spends)
#Monthly spends of each customer
monthly_spends.plot(kind='bar', x='Customer_ID', y=["CreditAmount", "DebitAmount","Card Limit","Current Outstanding Bill","Remaining Credit"], figsize=(8, 6), title=msg, color=['blue','yellow','green','red','purple'])
plt.xlabel('Customer ID')
plt.ylabel('Monthly spends')
plt.grid(True)
plt.show()

############ Linked List to get last 10 trasactions ############
sorted_df = savings_transactions.sort_values(by='Transaction_Date', ascending=False)
# Create a LinkedList to store CSV data
linked_list = LinkedList_SavingsTransaction()
# Iterate through each row of the DataFrame and add it to the linked list
for index, row in sorted_df.iterrows():
    linked_list.append(row)

#Customer_ID='cust_idno_1001'
filtered_data = linked_list.filter_by_column_value('Customer_ID', Customer_Id)
if filtered_data.get_length() == 0:
    print(f"There are no transactions for Customer_ID: {Customer_Id}\n")
else:
# Example: Print the linked list in a readable format
    current = filtered_data.head
    print(f"Last 10 Transactiosn for Customer_ID: {current.data['Customer_ID']}\n")
    record = 1
    while current and record<=10:
        record = record+1
        data = current.data
        print(f"Amount: {data['Amount']}, Transaction_Type: {data['Transaction_Type']}, Transaction_Date: {data['Transaction_Date']}")
        current = current.next
########################################################################
        
#NPA Identification
print("\nNon-Performing Asset(NPA) customer List:\n")
print(NPAIdentification().get_npa_accounts())

#Credit Card Offering
print("\nCredit Card Offering - Eligible for increased credit card balances:\n")
print(CreditCardOffering().get_ccoffer_accounts())