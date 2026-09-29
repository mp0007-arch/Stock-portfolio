Stock Tracker
A simple Python console program to manage a stock portfolio, made for CSE1021 – Introduction to Problem Solving and Programming (VITyarthi Build Your Own Project).
Author: Kushagra Shekhar | Reg. No.: 26BAI10451
Overview
Beginners often note down their shares on paper and lose track of how much money they have invested. This program lets you record your stocks and quickly see each stock's value, your total investment and your biggest investment.
While the program runs, the portfolio is stored in a Python dictionary. Each stock name is a key, and its value is a list [quantity, price per share].
Features
•	Add a stock – name, quantity and price per share
•	View all stocks – quantity, price and total value of each stock
•	Calculate total investment – adds up quantity × price for every stock
•	Search for a stock – shows the details of a stock by name
•	Find the highest investment – shows the stock with the largest total value
•	Delete a stock
•	Input checking – rejects blank names, duplicate stocks, non-numeric input, and zero or negative quantity/price, without crashing
Concepts Used
Input and output, variables and data types, if / elif / else, while and for loops, functions with parameters, dictionaries, lists, try / except, and string methods (upper, strip).
Technologies
•	Python 3 (no external libraries required)
•	Git and GitHub
How to Install and Run
1.	Install Python 3 from https://www.python.org/downloads/ and check it with: 
2.	python --version
3.	Download or clone this repository: 
4.	git clone <your-repository-link>cd <repository-folder>
5.	Run the program (replace the file name if yours is different): 
6.	python stock_tracker.py
7.	Type a number from 1 to 7 to choose an option.
Menu
==============================
       STOCK TRACKER
==============================
1. Add stock
2. View all stocks
3. Calculate total investment
4. Search for a stock
5. Find highest investment
6. Delete a stock
7. Exit
==============================
How to Test
Run the program and try the cases below. The expected result is given for each one.
Test	Steps	Expected result
Add a stock	Option 1: aapl, 10, 150	"Stock added successfully."
Name is saved in capitals	Add aapl, then view stocks	Shown as AAPL
Blank name	Option 1, press Enter	"Stock name cannot be blank."
Duplicate stock	Add aapl twice	"This stock is already in your portfolio."
Letters instead of numbers	Enter abc as quantity or price	"Please enter valid numbers for quantity and price."
Zero or negative quantity	Enter 0 or -5 as quantity	"Quantity must be greater than zero."
Zero or negative price	Enter 0 or -10 as price	"Price must be greater than zero."
View stocks	Option 2	Shows each stock's total value (AAPL: 10 × 150 = 1500.0)
Empty portfolio	Option 2 before adding anything	"Your portfolio is empty."
Total investment	Add AAPL (10 × 150) and INFY (40 × 18.5), then option 3	Total money invested: 2240.0
Search	Option 4, type aapl	"Stock found!" with details
Search a missing stock	Option 4, type xyz	"Stock was not found in your portfolio."
Highest investment	Option 5 with the stocks above	AAPL with value 1500.0
Delete	Option 6, type aapl	"Stock deleted successfully."
Invalid menu choice	Type 9	"Invalid choice. Please enter a number from 1 to 7."
Exit	Option 7	"Thank you for using Stock Tracker. Goodbye!" and the program ends

   
Limitations and Future Improvements
•	Data is not saved when the program is closed.
•	Search needs the full stock name (partial names are not matched).
•	There is no option to update a stock; delete it and add it again.
•	Possible additions: current prices with profit/loss, saving to a file, and a graphical interface.
ement

