# Stock Portfolio Tracker

## Description
A beginner-friendly command-line Stock Portfolio Tracker built in Python. This educational project allows users to simulate building a stock portfolio by adding shares of predefined stocks. It calculates individual holding values, overall total investment, and offers the ability to save the portfolio report to a CSV file.

## Objective
To demonstrate the fundamental understanding of Python data structures (dictionaries, lists), control flow, user input validation, arithmetic operations, and basic file handling by building a cohesive console application.

## Features
- **View Available Stocks**: Displays a list of predefined stocks with their current fixed prices.
- **Add to Portfolio**: Add shares of available stocks. Combines quantities if a stock is added multiple times.
- **Remove from Portfolio**: Delete an entire stock holding from your portfolio.
- **View Portfolio**: Displays a clean, tabular summary of your holdings, prices, quantities, and individual values, along with the total portfolio value.
- **Save to CSV**: Exports the current portfolio and total value to a `portfolio.csv` file.
- **Input Validation**: Gracefully handles unknown symbols, invalid quantities (text or negative numbers), and menu mis-selections without crashing.

## Technologies Used
- **Python 3**: Core language.
- **Standard Library `csv` module**: Used for writing the portfolio data to a CSV file.

## Concepts Demonstrated
- **Dictionaries**: Used to store the available stock prices and the user's portfolio.
- **File Handling**: Using `with open()` and the `csv.writer` to safely export data.
- **String Manipulation & Formatting**: Tabular alignment using f-strings (e.g., `<10`).
- **Error Handling**: Using `try-except` blocks to catch `ValueError` during float conversion.

## The Stock Price Dictionary
**Disclaimer:** *The stock prices in this application are completely hardcoded and predefined for educational purposes. They do not reflect real-time market data. No external APIs are used in order to keep the scope of the project simple and beginner-friendly.*

## Project Structure
```text
Stock_Portfolio_Tracker/
│
├── portfolio_tracker.py    # Main script containing all logic
├── README.md               # Project documentation
├── requirements.txt        # Dependency information
└── portfolio.csv           # Generated dynamically when saving
```

## Installation
No external libraries are required. 
1. Ensure you have Python 3 installed.
2. Clone or download this repository.
3. Open your terminal and navigate to the project directory.

## How to Run
Execute the script using Python:
```bash
python portfolio_tracker.py
```

## How Calculations Work
When viewing the portfolio, the application iterates over the user's portfolio dictionary:
1. It retrieves the predefined price from the `STOCKS` dictionary.
2. It calculates the individual value: `Holding Value = Price * Quantity`.
3. It adds the individual value to a running total: `Total Investment += Holding Value`.

## Sample Output
```text
========================================
       STOCK PORTFOLIO TRACKER
========================================
1. View available stocks
2. Add stock to portfolio
3. View portfolio
4. Remove stock from portfolio
5. Save portfolio to CSV
6. Exit
========================================
Select an option (1-6): 3

------------------------------------------------
Stock      Price      Quantity     Value     
------------------------------------------------
AAPL       $180.00    5.00         $900.00   
TSLA       $250.00    2.00         $500.00   
------------------------------------------------
Total Investment: $1400.00
```

## File Export Explanation
When the user selects option 5, the application utilizes Python's built-in `csv` library. It opens (or creates) `portfolio.csv` in write mode, writes a header row, iterates through the user's holdings to write data rows, and appends a final row containing the calculated Total Investment.

## Future Improvements
- Integrate a real-time stock API (like Yahoo Finance or Alpha Vantage) to fetch live data.
- Add an option to manually enter purchase price vs. current price to track Profit/Loss.
- Implement database storage (SQLite) instead of a CSV file for long-term persistence.

## Author
Developed as part of the **CodeAlpha Python Programming Internship**.
