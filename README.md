**GrowDataApplication - Hackathon**

Team Name - Tech Titans
Team Members - Kavya Kotagiri

**Problem Statement: 
Developing a Banking Application Code with Integrated Modules for Loan, Savings Account, and Credit Cards Management**

**Description:** You are tasked with developing a comprehensive banking application that manages customer accounts across three departments: Loan, Savings Account, and Credit Cards. The application's primary function is to provide a financial summary of any customer, including loan status, credit status, and current balance. Additionally, the application should identify potential Non-Performing Asset (NPA) customers and determine which customers should be offered increased credit card balances. Your solution should emphasize code efficiency and utilize Linked Lists and Object-Oriented Programming (OOP) concepts.

Data File – GrowDataBank.xlsx

**Problem Components:**
**1.	Data Understanding and Cleaning:**
	* Read and integrate data from three CSV files: Loan Account Data, Credit Card Data, and Savings Account Transactions Data.
	* Create classes to represent customer accounts for each department, ensuring data integrity.
	* Clean the data, to read it properly in CSV format tabular format.(hint- create separate columns from the uncleaned 1st column in salary transactions)
 
**2.	Account Management Modules:**
	* Develop separate modules for Loan, Savings Account, and Credit Card management, each implementing relevant functions. (The class will have methods that takes the data as attribute and other arguments 	and summarizes the insights for the user.)
	Example- takes a user id as input or a month as input in salary transaction month and outputs the summary for that in a readable format.
	* Utilize OOP principles to create classes for account types with methods for account updates and status calculations.
	Make classes for three different account data.
 
**3.	Financial Summary Function:**
	* Create a centralized function that takes a customer ID as input and provides a financial summary, including loan status, credit status, and current balances.
	* This function basically calls all the methods that you defined in the class earlier.
	* Update the customer's account information by invoking the respective modules.
 
**4.	Transaction History:**
	* Implement a module to retrieve and display the last 10 transactions for each customer's savings account.
	* Organize transaction data efficiently using Linked Lists for quick access.
 
**5.	NPA Identification:**
	* Develop an algorithm to identify potential Non-Performing Asset (NPA) customers based on predefined criteria, such as missed EMI payments.
	* Generate a list of NPA customers for further action.

**6.	Credit Card Offering:**
	* Create a mechanism to determine which customers are eligible for increased credit card balances.
	* Implement an algorithm considering factors like credit limit, outstanding bills, and transaction history.

**7.	Code Efficiency and Optimization:**
	* Assess and optimize the code for efficiency, focusing on time complexity.
 	* Implement efficient data structures like Linked Lists for transaction history storage and retrieval.
	* Employ appropriate algorithms for NPA identification and credit card offering.

**8.	Documentation and Reporting:**
	* Maintain detailed documentation explaining the code structure, algorithms, and classes used.
	* Generate reports summarizing NPA customers, credit card offerings, and code efficiency improvements.

In summary, this project challenges you to develop a banking application with integrated modules for Loan, Savings Account, and Credit Cards management. The application should provide financial summaries for customers, identify NPAs, and determine credit card offerings while emphasizing code efficiency and utilizing Linked Lists and OOP principles. The success of the project will be judged based on the accuracy of financial summaries, the effectiveness of NPA identification, and the efficiency of the code.

**Compulsory Submission-**
Following functionality is mandatory in Code-
-	Summary for individual Customer Saving Account for whole duration
-	Code that gives me monthly report for each customer- report will have spent on both account – credit and savings.
-	Account analysis for customer who have taken loans and have high missed EMI’s.
-	
**Judgement Criteria-**
The judgement would be taken by both the panel and votes, following will be the criteria for judging.
-	Modularity of code i.e., have you used classes and methods in your code.
-	Have you used correct data structure for the correct task considering the Big0 notation in mind.
-	How clean and readable your code is.
-	Do you have the relevant graphs to support your arguments.

**Rules**
-	There is no limit to what resource you are using Google. I won’t recommend using AI tools like ChatGPT to create the whole code. Sure you can use to correct syntax of to find a logic.
-	Submission in the Time limit of 24 hr will be considered for judgements.
-	Put all your work to a GitHub repo. PPT, document, Code file whatever you make.
-	Code file is compulsory in GitHub, rest depends on your choice and the time left for you.
  
Good Luck!
