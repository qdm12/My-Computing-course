# 9. Python, currencies and OOP

## Definitions
- *OOP*: Object oriented programming, just means you some *classes* in your code (to make *"objects"*)

## Excel spreadsheets, just to remind you...
- **transactions.xlsx** is a record of all the client quantity purchases since the beginning of the year
- **costs_and_prices.xlsx** indicates the following information:
    - The cost of an item
        - It is the cost to manufacture and ship the item
        - It is in *CNY* :yen: because our products are all made in China :blush:
    - The price of an item is the price at which it is sold to the client (with 15% tax :weary:)
        - So we need to deduce these 15% we have to pay to the state from our gains
        - These are in *EUR* :euro: because we ship to European countries
    - The fixed costs
        - This indicates the costs of the warehouse, the web server etc. per week
        - This one is in *GBP* :pound: because the company is actually based in UK :gb:
    - Note that our final revenues or profits are in *GBP*
    - **Assume** we exchange all revenues and costs inn GBP on the day of the transaction automatically

## What is wanted from us
1. Find and write the variable profit in *GBP* of each transaction, only taking into account:
    - The cost of an item and the GBPCNY exchange rate at the date of transaction, UK timezone
    - Price of an item and the past EURGBP exchange rate at the date of transaction, UK timezone
    - Write the results in an extra column "Variable Profit" on the right most side in *transactions.xlsx*
    - **DO NOT TAKE INTO ACCOUNT** the *fixed costs*
2. Write to *transactions.xlsx* the overall profit in GBP since the beginning of the year, assuming today is the last transaction's date.
    - Take the fixed costs into account
    - Use the column previously created in part 1

## PART 1 OF 2: Variable profit of each transaction
- One key element is to obtain historical exchange rates of GBPCNY and EURGBP.
	- We want to write a function following this skeleton:
	```python
	def get_historical_exchange_rate(currency_pair, date):
		rate = 1.00
		if currency_pair[0:2] == currency_pair[3:]:
			return rate
		# get the historical exchange rate somehow here...
		return rate
	```
	- The *arguments* (inputs) are the currency pair (*such as GBPCNY*) and the date (*such as 05/01/2017*)
	- The *return value* (output) should be the actual exchange rate we are searching for
	- Now, there are nice Python packages for getting stock data, current exchange rates such as *yahoo-finance* but
	  unfortunately, for historical exchange rates it's pretty bad.

## PART 2 OF 2: Overall profit since year's start

	
## What did you learn?
- More use of packages like for *yahoo-finance*
- More currency formatting for Excel
- Some bases for **OOP** which is very useful soon
	
## To add to your resume
- Yahoo Finance (Python)
- OOP or *Object oriented programming*