import csv

# Hardcoded dictionary containing several stock symbols and their predefined prices
STOCKS = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 150.0,
    "MSFT": 400.0,
    "AMZN": 180.0,
    "META": 300.0,
    "NFLX": 500.0,
    "NVDA": 800.0
}

def display_menu():
    """Displays the main menu interface."""
    print("\n========================================")
    print("       STOCK PORTFOLIO TRACKER")
    print("========================================")
    print("1. View available stocks")
    print("2. Add stock to portfolio")
    print("3. View portfolio")
    print("4. Remove stock from portfolio")
    print("5. Save portfolio to CSV")
    print("6. Exit")
    print("========================================")

def display_stocks():
    """Displays available stock symbols and their predefined prices."""
    print("\n--- Available Stocks ---")
    for symbol, price in STOCKS.items():
        print(f"{symbol:<6} - ${price:.2f}")

def add_stock(portfolio):
    """Allows the user to add a stock and its quantity to their portfolio."""
    symbol = input("Enter stock symbol: ").strip().upper()
    
    if symbol not in STOCKS:
        print(f"Error: '{symbol}' is not a valid stock symbol or is not available.")
        return

    try:
        quantity = float(input("Enter quantity: "))
        if quantity <= 0:
            print("Error: Quantity must be a positive number.")
            return
    except ValueError:
        print("Error: Invalid quantity. Please enter a numeric value.")
        return

    # Add or update the stock in the portfolio dictionary
    # If the stock already exists, we combine the quantities
    if symbol in portfolio:
        portfolio[symbol] += quantity
        print(f"Updated {symbol} quantity to {portfolio[symbol]:.2f}.")
    else:
        portfolio[symbol] = quantity
        print(f"Successfully added {quantity:.2f} shares of {symbol} to your portfolio.")

def remove_stock(portfolio):
    """Allows the user to remove a stock completely from the portfolio."""
    symbol = input("Enter stock symbol to remove: ").strip().upper()
    
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Successfully removed {symbol} from your portfolio.")
    else:
        print(f"Error: '{symbol}' is not currently in your portfolio.")

def display_portfolio(portfolio):
    """Displays the current portfolio in a table format and calculates total value."""
    if not portfolio:
        print("\nYour portfolio is currently empty.")
        return 0.0

    print("\n------------------------------------------------")
    print(f"{'Stock':<10} {'Price':<10} {'Quantity':<12} {'Value':<10}")
    print("------------------------------------------------")
    
    total_investment = 0.0
    
    for symbol, quantity in portfolio.items():
        price = STOCKS[symbol]
        value = price * quantity
        total_investment += value
        print(f"{symbol:<10} ${price:<9.2f} {quantity:<12.2f} ${value:<10.2f}")
        
    print("------------------------------------------------")
    print(f"Total Investment: ${total_investment:.2f}")
    return total_investment

def save_portfolio(portfolio):
    """Saves the current portfolio and total value to a CSV file."""
    if not portfolio:
        print("Error: Portfolio is empty. Nothing to save.")
        return

    filename = "portfolio.csv"
    
    try:
        # Using context manager 'with' to ensure the file is properly closed
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Write header row
            writer.writerow(["Stock", "Price", "Quantity", "Value"])
            
            total_investment = 0.0
            
            # Write data rows
            for symbol, quantity in portfolio.items():
                price = STOCKS[symbol]
                value = price * quantity
                total_investment += value
                writer.writerow([symbol, price, quantity, value])
            
            # Write total row at the bottom
            writer.writerow([]) # Empty row for spacing
            writer.writerow(["Total Investment", "", "", total_investment])
            
        print(f"\nPortfolio successfully saved to '{filename}'!")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def main():
    """Main function to run the program loop."""
    # Dictionary to hold user's portfolio in format { 'AAPL': 5.0, 'TSLA': 2.0 }
    portfolio = {} 
    
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            display_stocks()
        elif choice == '2':
            add_stock(portfolio)
        elif choice == '3':
            display_portfolio(portfolio)
        elif choice == '4':
            remove_stock(portfolio)
        elif choice == '5':
            save_portfolio(portfolio)
        elif choice == '6':
            print("\nExiting Stock Portfolio Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
